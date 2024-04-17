# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Class to manage interactions with appliance"""
import dataclasses
import functools
import itertools
import multiprocessing
import multiprocessing.dummy
import multiprocessing.pool
import os
import re
import shutil
import site
import sys
import textwrap
import threading
import time
from abc import ABC, abstractmethod
from contextlib import contextmanager
from numbers import Real
from pathlib import Path
from typing import (
    Any,
    Callable,
    Generator,
    Iterable,
    List,
    Literal,
    Optional,
    Set,
    Tuple,
    Union,
)

import dill
import grpc
import numpy as np
from tqdm import tqdm

from cerebras.appliance import __version__, log
from cerebras.appliance.appliance_client import (
    ApplianceClient,
    HeartBeatOptions,
)
from cerebras.appliance.cluster.client import (
    ClusterJobInitError,
    ClusterManagementClient,
    MountDir,
)
from cerebras.appliance.CSConfig import CSConfig
from cerebras.appliance.environment import appliance_environ
from cerebras.appliance.errors import (
    ApplianceClientException,
    ApplianceCompilationError,
    ApplianceDropModeComplete,
    ApplianceNanError,
    ApplianceResourceExhausted,
    ApplianceStallError,
    ApplianceTensorDropped,
    ApplianceUnknownError,
    ApplianceVersionError,
    register_grpc_error_pickler,
)
from cerebras.appliance.log import ClassLogger, named_class_logger
from cerebras.appliance.pb.framework.appliance_service_pb2 import (
    CarryOverFromPTRRequest,
    CompileRequest,
    CompileResponse,
    DeleteFromPTRRequest,
    FinalizeRequest,
    GetFromPTRRequest,
    InitRequest,
    LoadRequest,
    MoveToPTRRequest,
    RunRequest,
    SendCheckRequest,
)
from cerebras.appliance.pb.workflow.appliance.cluster_mgmt.cluster_pb2 import (
    CompileJobResponse,
    ComponentName,
    ExecuteJobResponse,
    ImageBuildResponse,
    JobEvent,
    JobStatus,
)
from cerebras.appliance.pb.workflow.appliance.common.common_config_pb2 import (
    _CLUSTERDETAILS_TASKINFO_TASKTYPE,
    ClusterDetails,
    DebugArgs,
    ExecutionStrategy,
    FrameworkType,
    JobMode,
    LogSettings,
    ResourceInfo,
)
from cerebras.appliance.pb.workflow.appliance.common.message_queue_pb2 import (
    MsgStatus,
    ValidTopics,
)
from cerebras.appliance.run_utils import set_ini
from cerebras.appliance.run_utils import (
    update_debug_args_with_job_labels as update_job_labels,
)
from cerebras.appliance.utils import (
    limit_mp_threads,
    short_temp_dir,
    version_check,
)
from cerebras.appliance.utils.pip import pip_config_list, pip_freeze


@dataclasses.dataclass
class TensorSendPayload:
    """
    The payload for sending weight tensor one at a time or in groups:
    A tensor's identity and either its contents or the means to produce it.

    Args:
        rt_name: Tensor name in the Cerebras Runtime, used for sending and
            receiving it
        fw_name: Tensor name in the framework, used for loading it from a
            checkpoint
        tensor: The actual tensor if it is available.
        ckpt_file: If the sending process hasn't yet loaded the tensor into the
            tensor field, this holds the filename to read the tensor from.
    """

    rt_name: str
    fw_name: str
    tensor: Union[None, np.ndarray, np.number, "torch.Tensor"] = None
    ckpt_file: Optional[str] = None


@dataclasses.dataclass
class TensorGroup:
    """
    A grouping of tensors to send together, with optional modification.

    Args:
        tensors: The (lazy) tensors included in the group. These will all be
            loaded (into numpy tensors) before sending any of them.
    """

    tensors: List[TensorSendPayload]


# Typing hint for send_weights_grouper argument
TensorGrouper = Callable[[Iterable[TensorSendPayload]], Iterable[TensorGroup]]


@named_class_logger("ApplianceManager")
class ApplianceManager(ABC, ClassLogger):
    """Manage Appliance Interactions"""

    # Value to signal to client to send all weight tensors
    SEND_ALL_WGTS = "__123_send_all_weight_tensors_321__"

    def __init__(
        self,
        config: CSConfig,
        compile_dir: str,
        artifact_dir: str,
        framework_type: FrameworkType,
        op_profiler_config: Optional[LoadRequest.OpProfilerConfig] = None,
    ):
        super().__init__()
        self._compile_dir = Path(compile_dir)
        if self._compile_dir.is_absolute():
            self.logger.warning(
                "Passing an absolute path as the compile directory "
                "may lead to undesirably long paths as the directory "
                "is used on the server side, not on the client side. "
                "Please consider passing in a relative directory instead."
            )

        artifact_dir = Path(artifact_dir)
        artifact_dir.mkdir(parents=True, exist_ok=True)

        self._cs_config = config
        self._framework_type = framework_type
        self.output_names = []

        self._credentials = None
        self._certificate_bytes = None
        if self._cs_config.credentials_path:
            self._set_credentials(
                Path(self._cs_config.credentials_path).read_bytes()
            )
        self._debug_args = ApplianceManager._init_debug_args(self._cs_config)
        self._mgmt_address = self._cs_config.mgmt_address
        self._mgmt_namespace = self._cs_config.mgmt_namespace
        self._mgmt_mount_dirs = self._cs_config.mount_dirs
        self._mgmt_python_paths = self._cs_config.python_paths
        self._num_csx = self._cs_config.num_csx
        self._max_wgt_servers = self._cs_config.max_wgt_servers
        self._num_workers_per_csx = self._cs_config.num_workers_per_csx
        self._max_act_per_csx = self._cs_config.max_act_per_csx

        self._coord_address = None
        self._default_authority = None
        self._grpc_client = None
        self._grpc_client_cv = threading.Condition()
        self._transfer_threads = self._cs_config.transfer_processes
        self._mgmt_client_args = {
            "server": self._mgmt_address,
            "crt_file": self._cs_config.credentials_path,
            "namespace": self._mgmt_namespace,
            "job_timer": self._cs_config.job_timer,
            "workdir": artifact_dir,
            "fabric_type_blacklist": self._cs_config.fabric_type_blacklist,
        }

        self._skipped_weights = None
        self.recv_groups = []

        # When custom worker image build was unsuccessful, we would mount
        # the user node Python environment to the worker environment to
        # gain dependency parity.
        self._mount_user_venv = False
        self._user_cv_path = None

        # Clean these up
        self.tracker_execute = None
        self._op_profiler_config = op_profiler_config

        if op_profiler_config:
            self._debug_args.ini.bools["ws_perf_tsc_enable"] = True
            self._debug_args.ini.bools["ws_add_tsc_ctx_switch"] = True
            self._debug_args.ini.ints["ws_perf_tsc_number"] = 30

        if not self._debug_args.debug_usr.disable_stall_detection:
            self.logger.verbose("Stall detection is enabled")
            set_ini(self._debug_args, ws_rt_enable_stall_check=True)

        # Log some settings to console
        self.logger.verbose(
            f"Credentials path: {self._cs_config.credentials_path}"
        )
        self.logger.debug(f"Debug args: {self._debug_args}")

    def __del__(self):
        if getattr(self, "_user_cv_path", None) is None:
            return
        if os.path.exists(self._user_cv_path):
            self.logger.info(
                f"Cleaning up user environment copy at {self._user_cv_path}"
            )
            shutil.rmtree(self._user_cv_path)

    @classmethod
    def _init_debug_args(cls, cs_config: CSConfig) -> DebugArgs:
        """Initialize job labels."""
        args = cs_config.debug_args
        if not args.debug_mgr:
            args.debug_mgr = DebugArgs.DebugMGR()
        if args.debug_mgr.labels is None:
            args.debug_mgr.labels = dict()
        update_job_labels(args, cs_config.job_labels)

        # In release 1.9, the appliance heartbeat is moved from USR<->CRD to USR<->MGR.
        # USR<->CRD heartbeat will be disabled in 1.9 and be deprecated post 1.9.
        args.debug_crd.disable_heartbeat_check = True

        # For Release 2.0, we are disabling the Disk Mapping for large tensors by default
        # It needs to be enabled explicitly for now
        if not args.debug_crd.vlt_tensor_size_disk_rw:
            args.debug_crd.vlt_tensor_size_disk_rw = -1

        # If the strategy is seen as unspecified, it means the call was issued from an old client.
        if args.debug_mgr.message_broker_strategy == (
            DebugArgs.DebugMGR.MessageBrokerStrategy.MESSAGE_BROKER_STRATEGY_UNSPECIFIED
        ):
            args.debug_mgr.message_broker_strategy = (
                DebugArgs.DebugMGR.MessageBrokerStrategy.MESSAGE_BROKER_STRATEGY_ENABLED
            )

        # In Release 2.2, we introduced streamer/worker separation. Framework defines the
        # resource separation between the two containers.
        args.debug_mgr.streamer_cpu_percent = 35
        args.debug_mgr.streamer_mem_percent = 65

        # In Release 2.2, we introduced a workflow id for all jobs launched from a single
        # user-side invocation. Jobs that are queued inherit the job priority of most recent
        # running job if any in the same workflow.
        args.debug_mgr.workflow_id = cs_config.workflow_id
        args.debug_mgr.job_priority = cs_config.job_priority
        return args

    def _set_credentials(self, value: bytes):
        """Sets the credentials from a certificate byte string."""
        if value:
            self._certificate_bytes = value
            self._credentials = grpc.ssl_channel_credentials(value)

    @property
    def cs_config(self):
        """Returns the CS Config."""
        return self._cs_config

    @property
    def grpc_client(self):
        """Client the FWK User Uses to connect to CRD"""
        with self._grpc_client_cv:
            if self._grpc_client is not None:
                return self._grpc_client

            self.logger.debug(
                f"Creating a framework GRPC client: {self._coord_address}, "
                f"with{'out' if self._credentials is None else ''} TLS, "
                f"{self._default_authority}"
            )

            heartbeat_options = None
            if not self._debug_args.debug_crd.disable_heartbeat_check:
                heartbeat_options = HeartBeatOptions()

            self._grpc_client = ApplianceClient(
                self._coord_address,
                credentials=self._credentials,
                default_authority=self._default_authority,
                execution_strategy=ExecutionStrategy.ES_WEIGHT_STREAMING,
                heartbeat_options=heartbeat_options,
                disable_version_check=self._cs_config.disable_version_check,
                retry_small_payload=self._debug_args.debug_usr.retry_small_payload,
                max_transfer_bytes=self._debug_args.debug_usr.max_transfer_bytes,
            )
            self._grpc_client_cv.notify_all()
            return self._grpc_client

    def wait_for_grpc_client(self):
        """Waits for a grpc client to become available"""
        with self._grpc_client_cv:
            self._grpc_client_cv.wait_for(lambda: self._grpc_client is not None)

    @property
    def skipped_weights(self) -> Set[str]:
        """Returns set of FW weights that are not needed by runtime.

        During lowering, some weights might be pruned from the graph. They exist
        and are needed for FW checkpoints, but are not needed by the runtime.
        We keep track of these during initialization and save them separately
        when saving checkpoints later on.
        """
        if self._skipped_weights is None:
            raise RuntimeError(
                "Attempting to access list of skipped weights, but weights "
                "have not been initialized yet."
            )
        return self._skipped_weights

    def remove_grpc_client(self):
        """Delete existing client to allow new connection"""
        with self._grpc_client_cv:
            if self._grpc_client is not None:
                self.logger.info(
                    f"Removing a framework GRPC client: {self._coord_address}"
                )
                self._grpc_client.close()
                del self._grpc_client
                self._grpc_client = None

    def _prep_cluster_details_resource(
        self, cluster_details: ClusterDetails, job_type: JobMode.Job
    ):
        """
        Updates resource requirements based on debug args.
        This is currently limited only to the coordinator role.

        Args:
            cluster_details: ClusterDetails object passed with at least 1 task.
            job_type: JobMode.Job enum which can be one of {JobMode.COMPILE, JobMode.EXECUTE}
        """
        # Cluster details memory and thread restrictions influenced
        # by debug args
        # Defaults are set during init/compile
        assert len(cluster_details.tasks) > 0, (
            f"Expected at least one task in cluster details when populating "
            f"resource info."
        )

        def task_type_str(enumval):
            return _CLUSTERDETAILS_TASKINFO_TASKTYPE.values_by_number[
                enumval
            ].name

        def bytes_str(b):
            if b == 0:
                return "unlimited"
            gi = b >> 30
            if gi > 0:
                return f"{int(gi)}Gi"
            mi = b >> 20
            if mi > 0:
                return f"{int(mi)}Mi"
            return f"{b} bytes"

        task_mode_override_map = {
            ClusterDetails.TaskInfo.TaskType.ACT: {
                JobMode.EXECUTE: self._debug_args.debug_usr.activation_resource,
            },
            ClusterDetails.TaskInfo.TaskType.BR: {
                JobMode.EXECUTE: self._debug_args.debug_usr.broadcastreduce_resource,
            },
            ClusterDetails.TaskInfo.TaskType.CHF: {
                JobMode.EXECUTE: self._debug_args.debug_usr.chief_resource,
            },
            ClusterDetails.TaskInfo.TaskType.CMD: {
                JobMode.EXECUTE: self._debug_args.debug_usr.command_resource,
            },
            ClusterDetails.TaskInfo.TaskType.CRD: {
                JobMode.COMPILE: self._debug_args.debug_usr.compile_coord_resource,
                JobMode.EXECUTE: self._debug_args.debug_usr.execute_coord_resource,
            },
            ClusterDetails.TaskInfo.TaskType.WGT: {
                JobMode.EXECUTE: self._debug_args.debug_usr.weight_resource,
            },
            ClusterDetails.TaskInfo.TaskType.WRK: {
                JobMode.EXECUTE: self._debug_args.debug_usr.worker_resource,
            },
        }
        for task in cluster_details.tasks:
            if task.task_type not in task_mode_override_map:
                continue
            if job_type not in task_mode_override_map[task.task_type]:
                continue
            task_type = task_type_str(task.task_type)
            original = ResourceInfo()
            original.CopyFrom(task.resource_info)
            task.resource_info.MergeFrom(
                task_mode_override_map[task.task_type][job_type]
            )
            if task.resource_info.memory_bytes != original.memory_bytes:
                # When user sets override to < 0, they unset the limit entirely
                # allowing tasks of that replica type to use all node's memory
                task.resource_info.memory_bytes = max(
                    task.resource_info.memory_bytes, 0
                )
                old_mem = bytes_str(original.memory_bytes)
                new_mem = bytes_str(task.resource_info.memory_bytes)
                warning_msg = ""
                if task.resource_info.memory_bytes == 0:
                    warning_msg = str(
                        ". Warning: allowing unlimited memory usage can disrupt "
                        "other tasks on shared nodes!"
                    )
                self.logger.warning(
                    f"User override set for task {task_type} resource memory "
                    f"from {old_mem} to {new_mem}"
                    f"{warning_msg}"
                )

            if task.resource_info.cpu_millicore != original.cpu_millicore:
                # When user sets override to < 0, they unset the limit entirely.
                # Not showing a warning here as unlike memory, unlimited CPU is
                # less risky than unlimited memory
                task.resource_info.cpu_millicore = max(
                    task.resource_info.cpu_millicore, 0
                )
                self.logger.warning(
                    f"User override set for task {task.task_type} resource cpu from "
                    f"{original.cpu_millicore}m to {task.resource_info.cpu_millicore}m"
                )

            # unset upper bound if override is greater than requested memory or
            # requested memory is unset
            if (
                task.resource_info.memory_bytes == 0
                or task.resource_info.memory_bytes
                >= task.resource_info.memory_bytes_upper_bound
            ):
                task.resource_info.memory_bytes_upper_bound = 0

    def construct_debug_args(self) -> DebugArgs:
        """Constructs a DebugArgs object to be sent to the appliance."""
        debug_args = DebugArgs()
        debug_args.CopyFrom(self._debug_args)

        # Inject Appliance environment variables to be set by workers
        for k, v in appliance_environ.items():
            debug_args.debug_wrk.env_vars[k] = v

        return debug_args

    def request_execute_job(
        self,
        mgmt_client: ClusterManagementClient,
        compile_response: CompileResponse,
    ) -> dict:
        """Requests an allocation of resources to run on appliance.

        Args:
            mgmt_client: Client to communicate for resources.
            compile_response: Context from compilation that determines resources required.

        Returns:
            reponse: Protobuf message ExecuteJobResponse as a dict appended with the
                'certificate_bytes' field which the caller can use to configure the coordinator grpc
                channel.
        """
        cluster_details = compile_response.cluster_details
        self._prep_cluster_details_resource(cluster_details, JobMode.EXECUTE)

        debug_args = self.construct_debug_args()

        # Apply log settings for servers
        apply_wsc_log_settings("execute", debug_args)

        # Set up additional mount dirs and python paths if we need to mount the user venv
        if (
            self._mount_user_venv
            and not debug_args.debug_usr.skip_user_venv_mount
        ):
            self._mgmt_python_paths += [
                os.path.realpath(site.getsitepackages()[0])
            ]

            import cerebras.appliance

            # Gets the realpath of the source venv
            venv_src = Path(cerebras.appliance.__path__[0]).parents[3].resolve()

            (
                requires_venv_copy,
                cv_path,
            ) = mgmt_client.get_user_venv_cluster_volume_path(venv_src)
            if not requires_venv_copy:
                self._mgmt_mount_dirs += [
                    MountDir(path=str(venv_src), container_path=str(venv_src)),
                ]
            else:
                uid = os.getuid()
                process_id = os.getpid()
                venv_dst = f"{cv_path}/venv-{uid}-{process_id}"
                self.logger.info(
                    f"Copying the user environment from {venv_src} to {venv_dst}"
                )

                if os.path.exists(venv_dst):
                    self.logger.warning(
                        f"Deleting a stale venv {venv_dst} on the cluster volume"
                    )
                    shutil.rmtree(venv_dst)

                shutil.copytree(
                    venv_src,
                    venv_dst,
                    dirs_exist_ok=False,
                    copy_function=shutil.copy2,
                    symlinks=True,
                )
                self._mgmt_mount_dirs += [
                    MountDir(path=venv_dst, container_path=str(venv_src))
                ]

                self._user_cv_path = venv_dst

                # Plumbs through the user venv path so that cluster management can check if
                # user venvs are stale and clean up accordingly. Note that we should only
                # plumb this through if venv copy is needed. This plumbing effectively would
                # result in a access marker file in the copied venv and would be used to
                # identify if a venv is a copied venv.
                debug_args.debug_mgr.user_venv_path = str(venv_src)

        job_mode = JobMode(job=JobMode.EXECUTE, cluster_details=cluster_details)
        try:
            return mgmt_client.init_execute_job(
                compile_response.cache_compile_dir,
                job_mode,
                debug_args,
                mount_dirs=self._mgmt_mount_dirs,
                python_paths=self._mgmt_python_paths,
            )
        except ClusterJobInitError as e:
            ApplianceManager.try_log_failed_job(mgmt_client, e.job_id)
            raise

    def stage_execute_coordinator(
        self,
        resource_response: ExecuteJobResponse,
    ):
        """Prepares connection details for FWK<->CRD Communication.

        Args:
            resource_response: Cluster mgmt response message.

        Returns:
            None
        """
        service_authority = resource_response["service_authority"]
        self.set_default_authority(service_authority)
        self.remove_grpc_client()
        self._update_coordinator_addr(resource_response["service_url"])
        self._set_credentials(resource_response["certificate_bytes"])
        # Make intial connection to provided coordinator
        self.grpc_client.ping()

    def set_default_authority(self, default_authority: Optional[str]):
        """Manage what authority is used in grpc client"""
        self._default_authority = default_authority

    def initialize_servers(self):
        """Perform servers initialization"""
        self.grpc_client.monitor_error_async()
        with self.tracker_execute.entry("execute_init_request"):
            self.grpc_client.init_servers(InitRequest())

    def initialize_session(
        self,
        run_request: RunRequest,
        compile_response: CompileResponse,
    ):
        """Perform initial connection handshake for execute mode.

        Args:
            run_request: Run request object.
            compile_response: Compile data from appliance.
        """
        self.logger.info(f"Preparing to execute using {self._num_csx} CSX")
        self.grpc_client.monitor_error_async()
        with self.tracker_execute.entry("execute_load_request"):
            load_request = LoadRequest(
                cache_compile_dir=compile_response.cache_compile_dir
            )

            if self._op_profiler_config:
                load_request.op_profiler_config.CopyFrom(
                    self._op_profiler_config
                )
            self.grpc_client.load_rtir(load_request)
        with self.tracker_execute.entry("execute_run_info"):
            self.grpc_client.run_deferred(run_request)

    def execute_session(
        self,
        initial_checkpoint_files: Optional[List[str]] = None,
        appliance_weights: Optional[List[Tuple[str, int]]] = None,
        skipped_weights: Optional[Set[str]] = None,
        send_weights_grouper: Optional[TensorGrouper] = None,
    ):
        """Perform initial connection handshake for execute mode.

        Args:
            initial_checkpoint_files: Saved checkpoint values to initialize model on appliance.
            appliance_weights: List of weights that need to be carried over from PTR.
            skipped_weights: Set of weights that are not needed by runtime.
            send_weights_grouper: Callable to process TensorSendPayloads into TensorGroups
        """
        with self.tracker_execute.entry("execute_send_weights"):
            self.logger.info("About to send initial weights")
            self.send_weights(
                self._weight_iterator(initial_checkpoint_files),
                appliance_weights,
                skipped_weights,
                send_weights_grouper,
            )
            self.logger.info("Finished sending initial weights")
        with self.tracker_execute.entry("execute_start_streaming"):
            self.logger.info("Finalizing appliance staging for the run")
            self.start_streaming()
            self.logger.info("Appliance staging is complete")

        self.logger.info("Beginning appliance run")

    def carry_over_from_ptr(
        self,
        iteration: int,
        tensor_name: str,
        tensor_id: int,
        keep_in_repo: bool = False,
    ) -> None:
        """In case if we have weights PTR, they can be carried over for the next session."""
        self.logger.debug(
            f"Carrying over tensor {tensor_name=}, {tensor_id=}, {iteration=}"
        )
        request = CarryOverFromPTRRequest(
            iteration=iteration,
            tensor_name=tensor_name,
            ptid=tensor_id,
            keep_in_repo=keep_in_repo,
        )
        self.grpc_client.carry_over_from_ptr(request)

    def move_to_ptr(self, tensor_name: str, tensor_id: int) -> None:
        """Move a tensor to PTR which makes is available for the next session."""
        self.logger.debug(f"Moving to PTR {tensor_name=}, {tensor_id=}")
        request = MoveToPTRRequest(
            tensor_name=tensor_name,
            ptid=tensor_id,
        )
        self.grpc_client.move_to_ptr(request)

    def get_from_ptr(
        self, tensor_id: int, keep_in_repo: bool = False
    ) -> np.ndarray:
        """Get a tensor from PTR."""
        self.logger.debug(f"Getting from PTR {tensor_id=}")
        request = GetFromPTRRequest(
            ptid=tensor_id,
            keep_in_repo=keep_in_repo,
        )
        return self.grpc_client.get_from_ptr(request)

    def delete_from_ptr(self, tensor_id: str) -> None:
        """Delete a tensor from PTR."""
        self.logger.debug(f"Deleting from PTR {tensor_id=}")
        request = DeleteFromPTRRequest(ptid=tensor_id)
        self.grpc_client.delete_from_ptr(request)

    def start_streaming(self):
        """Command to put Runtime in streaming mode"""
        self.grpc_client.sync()
        self.grpc_client.start_streaming()
        self.grpc_client.sync()

    def receive_activations(self, iteration):
        """Get activations from appliance."""
        return {
            output_name: self.receive_output(iteration, output_name)
            for output_name in self.output_names
        }

    def receive_output(self, iteration, name):
        """Get output from appliance."""
        return self.grpc_client.recv_output(iteration, name)

    @staticmethod
    def try_log_failed_job(mgmt_client, job_id):
        """
        Best effort to log information about a failed job.
        """
        num_tries = 12
        sleep_time = 5
        timeout = num_tries * sleep_time
        logger = ApplianceManager.logger

        logger.info(
            f"Trying to fetch failure info from the cluster for job {job_id}. "
            f"This may take up to {timeout} seconds."
        )

        try:
            # There is a time gap between the exception is thrown at the appliance client and
            # the job status change on the server. We attempt to retrieve the job status for
            # 60s and log the errors.
            while True:
                response = mgmt_client.get_job(job_id)
                if response.status == JobStatus.JOB_STATUS_IN_PROGRESS:
                    num_tries -= 1
                    if num_tries > 0:
                        logger.debug(
                            f"Job {job_id} is still in progress. Retrying in "
                            f"{sleep_time} seconds."
                        )
                        time.sleep(sleep_time)
                    else:
                        logger.info(
                            f"Job {job_id} is still in progress after "
                            f"{timeout} seconds. Giving up trying to fetch "
                            f"info about the job."
                        )
                        break
                else:
                    logger.error(
                        f"Job {job_id} failed due to: {response.message}"
                    )
                    log_failed_job_events(logger, response.job_events)
                    break
        except Exception as e:  # pylint: disable=broad-except
            logger.warning(
                f"Failed to fetch failure info for job {job_id} due to: {e}"
            )

    @contextmanager
    def compile_cluster(
        self,
    ) -> Union[ClusterManagementClient, CompileJobResponse]:
        """Context manager for requesting resource for a compile job"""
        # defaults to 0 which is no op currently (unlimited memory/cpu)
        # once restrictions are known, update the value
        compile_memory_bytes = 67 << 30  # current default ram memory for coord
        compile_cpu_millicore = 24000  # current default num of cpus for coord
        cluster_details_compile = ClusterDetails()
        task_info = ClusterDetails.TaskInfo(
            task_type=ClusterDetails.TaskInfo.TaskType.CRD,
            resource_info=ResourceInfo(
                memory_bytes=compile_memory_bytes,
                cpu_millicore=compile_cpu_millicore,
            ),
        )
        cluster_details_compile.tasks.append(task_info)  # pylint: disable=E1101
        self._prep_cluster_details_resource(
            cluster_details_compile, JobMode.COMPILE
        )
        job_mode = JobMode(
            job=JobMode.COMPILE, cluster_details=cluster_details_compile
        )
        with ClusterManagementClient(**self._mgmt_client_args) as mgmt_client:
            try:
                mgmt_versions = mgmt_client.get_server_versions()
                # Handle in manager because cluster management test don't include appliance
                # SW-91475
            except grpc.RpcError as rpc_error:
                rpc_error_code = rpc_error.code()  # pylint: disable=no-member
                if rpc_error_code == grpc.StatusCode.UNIMPLEMENTED:
                    # Catch version 1.7 where we didn't have version checks
                    release_version = __version__.split("+")[0]
                    raise ApplianceVersionError(
                        "Cluster management server version is out of date. "
                        f"Please install version: {release_version}"
                    ) from rpc_error
                raise

            if not self._cs_config.disable_version_check:
                for component_details in mgmt_versions:
                    component_name = ComponentName.Name(component_details.name)
                    version = component_details.version
                    if "+" in version:
                        version, githash = version.split("+")
                    else:
                        # Possible future cluster version epoch.
                        # Definitely incompatible, so pass None for the githash
                        # to fail the check.
                        githash = None
                    version_check(component_name, version, githash)

            debug_args = DebugArgs()
            debug_args.CopyFrom(self._debug_args)

            # Apply log settings for servers
            apply_wsc_log_settings("compile", debug_args)

            try:
                response = mgmt_client.init_compile_job(
                    str(self._compile_dir),
                    job_mode,
                    debug_args,
                )
            except ClusterJobInitError as e:
                self.try_log_failed_job(mgmt_client, e.job_id)
                raise
            service_authority = response["service_authority"]
            self.set_default_authority(service_authority)

            self._update_coordinator_addr(response["service_url"])
            self._set_credentials(response["certificate_bytes"])
            # Refactor so client doesn't need to be returned
            yield mgmt_client, response

    def _update_coordinator_addr(self, addr: str):
        """Updates the coordinator addresses. Clients may attempt to connect to any of the
        addresses in the list."""

        # TODO workaround for mocking cluster management responses
        if addr.count(':') == 1:
            self._coord_address = addr
        else:
            second_colon_idx = addr.rfind(':')
            self._coord_address = addr[:second_colon_idx]

    def compile(self, compile_request: CompileRequest) -> CompileResponse:
        """Compiles the model for CS-X hardware.

        Args:
            compile_request: Compile information for appliance.

        Returns:
            compile_resp: Appliance response to compile request.
        """
        self.tracker_execute.start("compile_coord_start")

        with self.compile_cluster() as (mgmt_client, mgmt_response):
            self.remove_grpc_client()
            job_id = mgmt_response["job_id"]
            self.tracker_execute.stop("compile_coord_start")
            with self.tracker_execute.entry("cirh_end"), self.subscribe(
                ValidTopics.COMPILE
            ):
                exc = None
                try:
                    compile_dir_absolute_path = mgmt_response[
                        "compile_dir_absolute_path"
                    ]
                    compile_request.compile_dir = compile_dir_absolute_path
                    compile_resp = self.grpc_client.compile(compile_request)
                    cache_compile_dir = compile_resp.cache_compile_dir
                    mgmt_client.log_cache_compile(job_id, cache_compile_dir)
                    self.logger.info(
                        f"Compile artifacts successfully written to remote "
                        f"compile directory. Compile hash is: "
                        f"{os.path.basename(cache_compile_dir)}"
                    )
                except grpc.RpcError:
                    exc = sys.exc_info()[1]
                    if exc.code() == grpc.StatusCode.INTERNAL:
                        # Interpret as compilation error. Remove link to current exception
                        # so that it doesn't get printed when the raised exception is printed.
                        raise ApplianceCompilationError(exc.details()) from None
                    raise
                except Exception:  # pylint: disable=broad-except
                    exc = sys.exc_info()[1]
                    raise
                finally:
                    if exc:
                        self.try_log_failed_job(mgmt_client, job_id)
                    if self._grpc_client:
                        self.grpc_client.done()

        return compile_resp

    def wait_build_image(
        self,
        mgmt_client: ClusterManagementClient,
        init_response: ImageBuildResponse,
        start_time: float,
        timeout: Real,
    ):
        """Waits for image build to complete"""
        wait_time = 0
        poll_interval = 5
        image_ready = init_response.image_ready
        job_id = init_response.job_id
        image_reference = init_response.image_reference
        while not image_ready and wait_time < timeout:
            response = mgmt_client.get_image_build_job(
                job_id=job_id, image_reference=image_reference
            )
            if response.status == JobStatus.JOB_STATUS_FAILED:
                break

            wait_time = time.time() - start_time
            time.sleep(poll_interval)
            image_ready = response.image_ready

        if response.status == JobStatus.JOB_STATUS_FAILED:
            error_log_path = mgmt_client.get_image_build_log_path()
            self.logger.warning(
                f"Image build job {job_id} failed. "
                f"Please check the error log in {error_log_path}. "
                f"User venv should be mounted to the worker environment "
                f"automatically to gain dependency parity unless the "
                f"venv mounting feature was explicitly disabled."
            )
            self._mount_user_venv = True
        elif not response.image_ready:
            self.logger.error(f"Image build job {job_id} timeout exceeded.")
            self._mount_user_venv = True
        else:
            if job_id:
                self.logger.info(f"Image build job {job_id} succeeded.")
            else:
                self.logger.info(
                    f"Image reference {response.image_reference} already exists."
                )
            self._debug_args.debug_mgr.custom_streamer_image = (
                response.image_reference
            )

    @contextmanager
    def build_worker_image(self, should_skip=False, timeout: Real = 60 * 60):
        """Trigger cluster management job to build worker image"""
        # Skip launching the custom worker build job, if any of the following is true:
        # - The run was meant for compile only or validate only
        # - The debug args to skip image build is raised
        # - There had already been a job created with the same base image and package dependencies
        if should_skip or self._debug_args.debug_usr.skip_image_build:
            self._mount_user_venv = True
            yield
            return

        with ClusterManagementClient(**self._mgmt_client_args) as mgmt_client:
            start_time = time.time()

            response = mgmt_client.init_image_build_job(
                pip_options=pip_config_list(),
                frozen_dependencies=pip_freeze(),
                workdir_hostpath_override=self._debug_args.debug_mgr.workdir_hostpath_override,
            )

            # "image_ready" and "image_reference" attributes will always be non-empty.
            # In the event where image build job is short circuited in the cluster server, the
            # "job_id" attribute will be empty. The Framework code should always rely on the
            # "image_ready" attribute to check whether the workflow should proceed further.
            if response.image_ready:
                self.logger.info(
                    f"Custom worker image {response.image_reference} is ready."
                )
                yield
            elif response.mount_user_venv:
                self.logger.info(
                    f"Custom worker image build is disabled from server."
                )
                self._mount_user_venv = response.mount_user_venv
                yield
            else:
                yield
                self.wait_build_image(
                    mgmt_client, response, start_time, timeout
                )

    @contextmanager
    def subscribe(self, topic: ValidTopics, timeout: int = 15):
        """Poll Message Queue topic until exit"""

        self.logger.debug(
            f"Subscribing to server topic {ValidTopics.Name(topic)}"
        )

        unsubscribe = threading.Event()
        client_kwargs = dict(
            crd_address=self._coord_address,
            credentials=self._credentials,
            default_authority=self._default_authority,
        )
        threading.Thread(
            target=poll_topic,
            args=(
                client_kwargs,
                (unsubscribe, self.grpc_client.shutdown),
                self.logger,
                topic,
                timeout,
            ),
            name=f"SubscribeThread:{topic}",
            daemon=True,
        ).start()

        try:
            yield
        finally:
            unsubscribe.set()
            self.logger.debug(
                f"Unsubscribed from server topic {ValidTopics.Name(topic)}"
            )

    def send_weights(
        self,
        initial_weights,
        appliance_weights: Optional[List[Tuple[str, int]]] = None,
        skipped_weights: Optional[Set[str]] = None,
        grouper: Optional[TensorGrouper] = None,
    ):
        """Send weights to appliance.

        Args:
            initial_weights: The weight tensors to send.
            appliance_weights: List of weights that need to be carried over from PTR.
            skipped_weights: Set of weights that are not needed by runtime.
            grouper: Callable to process TensorSendPayloads into TensorGroups.

        """
        # Get a list of weight rt_names to send at this iteration
        tensor_rt_groups = self.grpc_client.send_check(
            0, info_type=SendCheckRequest.InfoType.GROUP
        )
        # Flatten groups into simple list.
        tensor_rt_names = [
            tensor_name
            for group in tensor_rt_groups
            for tensor_name in group.tensor_names
        ]

        if (
            len(tensor_rt_names) == 1
            and tensor_rt_names[0] == self.SEND_ALL_WGTS
        ):
            send_all = True
            tensor_rt_names = set()  # Track tensors to use in validate() below
        else:
            send_all = False
            tensor_rt_names = set(tensor_rt_names)

        skipped_weights = skipped_weights or set()
        skipped_rt_tensors = set(
            map(self._map_wgt_name_fw_to_rt, skipped_weights)
        )

        # Create the iterable for generating tensors
        def get_tensors() -> Generator[TensorSendPayload, None, None]:
            for fw_name, tensor_or_ckpt_file in initial_weights:
                rt_name = self._map_wgt_name_fw_to_rt(fw_name)
                if isinstance(tensor_or_ckpt_file, str):
                    lazy_tensor = TensorSendPayload(
                        rt_name=rt_name,
                        fw_name=fw_name,
                        tensor=None,
                        ckpt_file=tensor_or_ckpt_file,
                    )
                else:
                    lazy_tensor = TensorSendPayload(
                        rt_name=rt_name,
                        fw_name=fw_name,
                        tensor=tensor_or_ckpt_file,
                        ckpt_file=None,
                    )

                if rt_name in tensor_rt_names:
                    yield lazy_tensor
                elif send_all:
                    tensor_rt_names.add(rt_name)
                    yield lazy_tensor
                else:
                    # Mark fw tensor name as skipped.
                    # This is slightly unusual since the TensorTransferTracker
                    # otherwise deals solely with rt_name, but we have special
                    # handling for skipped tensors requiring them to be fw_name
                    skipped_weights.add(fw_name)

        if any(len(g.tensor_names) > 1 for g in tensor_rt_groups):
            # We have some actual groups, not just all single tenor groups
            if grouper:
                # In practice, this means sideband sparsity _AND_
                # sparsity_optimizer were used together, which is not
                # supported, but shouldn't be possible with modelzoo code.
                raise ValueError(
                    "Cannot support both client and server specified grouping."
                )

            # Build a grouper for the server directed groups.
            def server_grouper(
                tensors: Iterable[TensorSendPayload],
            ) -> Iterable[TensorGroup]:
                rt_tensors = {tensor.rt_name: tensor for tensor in tensors}
                for group in tensor_rt_groups:
                    # Set up weight egress grouping too
                    tensor_names = []
                    tensor_group = []
                    for n in group.tensor_names:
                        if n in rt_tensors:
                            tensor_names.append(n)
                            tensor_group.append(rt_tensors[n])

                    self.recv_groups.append(tensor_names)

                    yield TensorGroup(
                        tensors=tensor_group,
                    )

            grouper = server_grouper

        # Start transfer
        transfer_tracker = TensorTransferTracker()
        if self._transfer_threads > 1:
            pool_cls = functools.partial(
                multiprocessing.pool.Pool,
                context=multiprocessing.get_context('spawn'),
            )
        else:
            # fake multiprocessing, just use python threads
            pool_cls = multiprocessing.dummy.Pool

        with short_temp_dir(), limit_mp_threads(), pool_cls(
            processes=self._transfer_threads,
            initializer=WeightSender.initializer,
            initargs=(
                self._coord_address,
                self._certificate_bytes,
                self._default_authority,
                self._checkpoint_reader_cls,
                self._debug_args.debug_usr.retry_small_payload,
                self._debug_args.debug_usr.max_transfer_bytes,
            ),
        ) as pool:
            if grouper:
                # Each group returns iterable results, one for each tensor.
                iter_sent_tensor = itertools.chain.from_iterable(
                    pool.imap_unordered(
                        WeightSender.group_runner,
                        grouper(get_tensors()),
                    )
                )
            else:
                # Transfer each tensor individually.
                iter_sent_tensor = pool.imap_unordered(
                    WeightSender.runner, get_tensors()
                )
            try:
                for pkl_val in tqdm(
                    iter_sent_tensor,
                    total=len(tensor_rt_names),
                    desc="Transferring weights to server",
                    dynamic_ncols=True,  # Match console width
                    unit=" tensors",
                    file=sys.stdout,
                    disable=True
                    if send_all
                    else None,  # Disable on non-TTY/all
                ):
                    rt_name, outcome = WeightSender.deserialize(pkl_val)
                    transfer_tracker.add(rt_name, outcome)
            except ApplianceClientException as ex:
                raise ex

        # Carry over weights from PTR.
        if appliance_weights:
            for fw_name, ptid in appliance_weights:
                self.carry_over_from_ptr(
                    iteration=0,
                    tensor_name=fw_name,
                    tensor_id=ptid,
                    keep_in_repo=False,
                )
                transfer_tracker.add(self._map_wgt_name_fw_to_rt(fw_name), True)

        # Add all fw tensors that were skipped
        for fw_name in skipped_weights:
            transfer_tracker.add(fw_name, False)

        # Validate that everything went fine
        transfer_tracker.validate(tensor_rt_names - skipped_rt_tensors)

        # Save skipped weights for use later when saving checkpoints in FW
        self._skipped_weights = set(transfer_tracker.skipped)

    # pylint: disable=R0201
    def _map_wgt_name_fw_to_rt(self, tensor_name: str) -> str:
        """
        Map the weight name from what is it in the framework
        to what it is expected in the runtime
        """
        return tensor_name

    def _weight_iterator(
        self, initial_checkpoint_files
    ) -> Generator[Tuple[str, Any], None, None]:
        """Returns a generator that yields weights tensors to be sent.

        Yields:
            Tuple of tensor name and tensor content. The content can be either
            a tensor to checkpoint filename to read the tensor from.
        """
        if initial_checkpoint_files is None:
            raise RuntimeError(
                "Expected at least one initial checkpoint file. Got none"
            )

        if isinstance(initial_checkpoint_files, str):
            initial_checkpoint_files = [initial_checkpoint_files]

        for ckpt_file in initial_checkpoint_files:
            ckpt = self._checkpoint_reader_cls(ckpt_file)
            for weight_name in ckpt.tensor_names:
                yield weight_name, ckpt_file

    @property
    @abstractmethod
    def _checkpoint_reader_cls(self):
        """Return the checkpoint reader class"""

    @contextmanager
    def clean_shutdown(self, mgmt_client: ClusterManagementClient, job_id: str):
        """A context manager for cleanly shutting down the appliance."""
        run_state = None
        status = None

        try:
            yield
            status = JobStatus.JOB_STATUS_SUCCEEDED
            run_state = FinalizeRequest.FS_SUCCESS
        except (
            ApplianceDropModeComplete,
            ApplianceResourceExhausted,
            KeyboardInterrupt,
        ):
            status = JobStatus.JOB_STATUS_CANCELLED
            self.logger.warning(f"Job {job_id} was cancelled")
            raise
        except (grpc.RpcError, ApplianceUnknownError) as e:
            if isinstance(e, ApplianceUnknownError):
                self.logger.error(
                    f"Initiating shutdown sequence due to Appliance error: {e}"
                )
            else:
                self.logger.error(
                    f"Initiating shutdown sequence due to gRPC error: {e}"
                )

            status = JobStatus.JOB_STATUS_FAILED
            self.try_log_failed_job(mgmt_client, job_id)
            raise
        except Exception as e:  # pylint: disable=broad-except
            status = JobStatus.JOB_STATUS_FAILED

            if isinstance(e, ApplianceStallError):
                self.logger.error(
                    f"Initiating shutdown sequence due to possible stall: {e}"
                )
                run_state = FinalizeRequest.FS_STALL
            elif isinstance(e, ApplianceNanError):
                self.logger.error(
                    f"Initiating shutdown sequence due to NaN error: {e}"
                )
                run_state = FinalizeRequest.FS_NAN
            else:
                self.logger.error(
                    f"Initiating shutdown sequence due to error: {e}"
                )
                self.try_log_failed_job(mgmt_client, job_id)

            raise
        finally:
            with self.tracker_execute.entry("execute_shutdown"):
                if (
                    run_state is not None
                    and run_state != FinalizeRequest.FS_SUCCESS
                ):
                    try:
                        self.finalize(FinalizeRequest(state=run_state))
                    except Exception as e:  # pylint: disable=broad-except
                        self.logger.error(
                            f"Finalizing job ran into error: {e}.\n"
                            f"Continuing with shutdown sequence ..."
                        )

                # Clean shutdown when no errors
                if status != JobStatus.JOB_STATUS_FAILED:
                    try:
                        self.done()
                    except Exception as e:  # pylint: disable=broad-except
                        # If done() call throws an exception, ignore it and
                        # proceed with cancelling the job.
                        self.logger.error(
                            f"Clean shutdown ran into error: {e}.\n"
                            f"Proceeding to force cancel the job."
                        )
                # TODO: Temporary until graceful shutdown option for BR nodes
                self.grpc_client.shutdown.set()
                self.grpc_client.stop_heartbeat()
                mgmt_client.cancel_job(job_id, status)

    def finalize(self, request: Optional[FinalizeRequest] = None):
        """Finalize the session on the appliance."""
        self.grpc_client.stop_monitor_error()
        return self.grpc_client.finalize(
            request or FinalizeRequest(state=FinalizeRequest.FS_SUCCESS)
        )

    def done(self, wait: bool = False):
        """Cleanup appliance interaction"""
        if wait:
            # Call to done should never be creating a grpc client
            # If a call to done happens before a grpc client is created,
            # we should wait for the client to be created and before calling done
            self.wait_for_grpc_client()
        self.grpc_client.done()


@named_class_logger("WeightSender")
class WeightSender(ClassLogger):
    """A class to use in a multiprocessing context for sending weights."""

    impl: Union["WeightSender", None] = None

    def __init__(
        self,
        coord_address,
        certificate_bytes: Optional[bytes],
        default_authority,
        checkpoint_reader_cls,
        retry_small_payload,
        max_transfer_bytes: Optional[int] = None,
    ):
        """Constructs a `WeightSender` instance.

        Args:
            coord_address: Address of the coordinator to send to.
            credentials_data: Optional PEM encoded certificate string for grpc
                secure channel setup.
            default_authority: Authority to authorize communication.
            max_transfer_bytes: Maximum tensor chunk size to send.
        """
        super().__init__()

        credentials = None
        if certificate_bytes:
            credentials = grpc.ssl_channel_credentials(certificate_bytes)

        self._grpc_client = ApplianceClient(
            coord_address,
            credentials=credentials,
            default_authority=default_authority,
            disable_version_check=True,
            retry_small_payload=retry_small_payload,
            max_transfer_bytes=max_transfer_bytes,
        )

        self.checkpoint_reader_cls = checkpoint_reader_cls
        self._reader = None
        self._current_ckpt_file = None

        # Add pickling support to exceptions so that they include their
        # traceback
        from tblib import pickling_support

        pickling_support.install()

        # gRPC exceptions are not picklable by default. Register custom picklers
        # so they can be properly pickled to be sent across processes.
        register_grpc_error_pickler()

    def send_tensor(self, tensor: TensorSendPayload):
        """Sends the given tensor through gRPC to appliance service."""
        name = "Unknown"  # In case tensor is malformed
        try:
            name = tensor.rt_name
            np_tensor, broadcast = self._get_numpy_tensor(tensor)
            self._grpc_client.send_weight(
                0, tensor.rt_name, np_tensor, broadcast
            )
            return WeightSender.serialize((name, True))  # success
        except Exception as e:  # pylint: disable=broad-except
            return WeightSender.serialize((name, e))  # failure

    def send_group(self, group: TensorGroup):
        """Sends the given group of tensors through gRPC to appliance service."""
        try:
            for tensor in group.tensors:
                # Assign the numpy tensor back into the TensorSendPayload.
                tensor.tensor, broadcast = self._get_numpy_tensor(tensor)
                self._grpc_client.send_weight(
                    0, tensor.rt_name, tensor.tensor, broadcast
                )
            return [
                WeightSender.serialize((tensor.rt_name, True))
                for tensor in group.tensors
            ]
        except Exception as e:  # pylint: disable=broad-except
            return [
                WeightSender.serialize((tensor.rt_name, e))
                for tensor in group.tensors
            ]

    def _get_numpy_tensor(
        self, tensor: TensorSendPayload, allow_scalar_broadcast: bool = True
    ):
        """Loads or returns the numpy tensor from the given TensorSendPayload."""
        if tensor.tensor is None:
            # checkpoint file
            if tensor.ckpt_file != self._current_ckpt_file:
                self._reader = self.checkpoint_reader_cls(tensor.ckpt_file)
                self._current_ckpt_file = tensor.ckpt_file
            np_tensor = self._reader[tensor.fw_name]
        else:
            np_tensor = tensor.tensor

        if isinstance(np_tensor, np.ndarray):
            return np_tensor, False
        elif isinstance(np_tensor, np.number):
            return np.array(np_tensor), False
        else:
            try:
                import torch

                import cerebras.pytorch as cstorch
                from cerebras.pytorch.saver.storage import (
                    check_deferred_backing_storage,
                )

                if isinstance(np_tensor, torch.Tensor):
                    if (
                        allow_scalar_broadcast
                        and isinstance(
                            np_tensor, cstorch.saver.storage.DeferredFullTensor
                        )
                        and not np_tensor.is_modified
                        and np_tensor.fill_value is not None
                    ):
                        return (
                            np.array(
                                np_tensor.fill_value,
                                dtype=cstorch.saver.storage.torch_to_np_dtype(
                                    np_tensor.dtype
                                ),
                            ),
                            True,
                        )

                    # Disable file modification check since we are in full control of the
                    # initial state file after creation and know that we're not modifying it.
                    with check_deferred_backing_storage(False):
                        return cstorch.to_numpy(np_tensor), False
            except ImportError:
                pass

            raise ValueError(
                f"Expected weight tensors to be np.ndarray or np.number, but "
                f"weight tensor `{tensor.fw_name}` has type "
                f"`{type(np_tensor)}`."
            )

    @staticmethod
    def serialize(val):
        """Generic serialization using dill."""
        return dill.dumps(val)

    @staticmethod
    def deserialize(pkl_val):
        """Generic de-serialization method using dill."""
        return dill.loads(pkl_val)

    @staticmethod
    def initializer(*args, **kwargs):
        """The initializer to use in multiprocessing."""
        WeightSender.impl = WeightSender(*args, **kwargs)

    @staticmethod
    def runner(tensor: TensorSendPayload):
        """The runner method to use in multiprocessing."""
        assert WeightSender is not None, "Initializer must be called."
        return WeightSender.impl.send_tensor(tensor)

    @staticmethod
    def group_runner(group: TensorGroup):
        """The runner method to use in multiprocessing."""
        assert WeightSender is not None, "Initializer must be called."
        return WeightSender.impl.send_group(group)


@named_class_logger("TensorTransferTracker")
@dataclasses.dataclass
class TensorTransferTracker(ClassLogger):
    """Class to track transfer of tensors.

    Args:
        success: List of tensor names that were successfuly transferred.
        errors: List of exceptions encountered when transferring tensors.
        dropped: List of tensor names that were transferred and dropped at the
            coordinator due to DROP flow being enabled.
        skipped: List of FW tensor names that are in the graph but not needed by
            the runtime (e.g., pruned from the graph during lowering).
    """

    success: List[str] = dataclasses.field(default_factory=list)
    errors: List[Union[Exception, str]] = dataclasses.field(
        default_factory=list
    )
    dropped: List[str] = dataclasses.field(default_factory=list)
    skipped: List[str] = dataclasses.field(default_factory=list)

    def add(self, tensor_name: str, outcome: Union[bool, Exception]) -> None:
        """Track a tensor's weight transfer outcome.

        Args:
            tensor_name: The RT/FW tensor name.
            outcome: Transfer outcome of the tensor. It must be one of:
                True: If transferring this RT weight was successful.
                False: If this FW weight was skipped.
                Exception: If transferring this RT tensor ran into an error.
        """
        if outcome is True:
            self.success.append(tensor_name)
        elif isinstance(outcome, ApplianceTensorDropped):
            self.dropped.append(tensor_name)
        elif isinstance(outcome, ApplianceResourceExhausted):
            self.logger.error(
                f"Resource exhausted when transferring '{tensor_name}'. {str(outcome)}"
            )
            # raise on the first error found, this causes an early abort
            raise outcome
        elif isinstance(outcome, Exception):
            self.logger.error(
                f"Ran into error when transferring '{tensor_name}'. {str(outcome)}"
            )
            # raise on the first error found, this causes an early abort
            raise outcome
        elif outcome is False:
            self.skipped.append(tensor_name)
        else:
            raise TypeError(
                f"Expected outcome to be one of True/False/Exception, but "
                f"got: {type(outcome)}"
            )

    def validate(self, expected: Set[str]) -> None:
        """Validates weight transfer and raises exception if unsuccesful.

        Args:
            expected: List of rt tensor names that we expect to have been transferred.
        """

        num_tensors = (
            len(self.success)
            + len(self.errors)
            + len(self.dropped)
            + len(self.skipped)
        )

        self.logger.verbose(f"Weight transfer summary:")
        self.logger.verbose(f"\tSuccess: {self.success}")
        self.logger.verbose(f"\tDropped: {self.dropped}")
        self.logger.verbose(f"\tSkipped: {self.skipped}")
        self.logger.verbose(f"\tErrors: {self.errors}")

        if self.errors:
            self.logger.error(
                f"Failed to transfer {len(self.errors)} out of "
                f"{num_tensors} weight tensors. Raising the first "
                f"error encountered."
            )
            raise self.errors[0]
        elif self.success and self.dropped:
            raise ApplianceClientException(
                f"Some weights were successfully transferred, while some were "
                f"dropped at the coordinator. This indicates an "
                f"internal error.\n"
                f"Transferred Tensors: {self.success}\n"
                f"Dropped Tenors: {self.dropped}"
            )
        elif self.success:
            missing = set(expected) - set(self.success)
            if missing:
                raise ApplianceClientException(
                    f"Appliance service expects the following tensors "
                    f"which were not transferred by the client: {missing}"
                )
        elif self.dropped:
            missing = set(expected) - set(self.dropped)
            if missing:
                raise ApplianceClientException(
                    f"Appliance service expects the following tensors "
                    f"which were not transfer by the client: {missing}"
                )
            raise ApplianceDropModeComplete(
                f"All {len(self.dropped)} weight tensors were dropped."
            )
        elif expected:
            # No errors, success, or dropped. We transferred nothing!
            raise ApplianceClientException(
                f"Expected client to transfer {len(expected)} weight tensors, but "
                f"none were transferred and {len(self.skipped)} were skipped."
            )


def apply_wsc_log_settings(
    job_mode: Literal["compile", "execute"], debug_args: DebugArgs
) -> None:
    """Injects the WSC log settings to the given debug args.

    Args:
        job_mode: The job mode to apply the log settings for.
        debug_args: The debug args to inject log settings into.
    """

    log_settings = log.collect_wsc_log_settings()
    if not log_settings:
        return

    modes = log.WscLogSetting.allowed_modes()
    if job_mode not in modes:
        raise ValueError(
            f"Invalid job mode {job_mode}. Must be one of: {', '.join(modes)}"
        )

    for role in log.WscLogSetting.allowed_roles():
        role_args = getattr(debug_args, f"debug_{role}")
        role_log_settings = role_args.log_settings
        for log_setting in log_settings:
            if log_setting.mode is not None and log_setting.mode != job_mode:
                continue
            if log_setting.role is not None and log_setting.role != role:
                continue

            wsc_level = python_to_wsc_level(log_setting.level)
            if log_setting.tag is None:
                role_log_settings.global_level = wsc_level
            else:
                message_tag = role_log_settings.message_tags.add()
                message_tag.tag = log_setting.tag
                message_tag.level = wsc_level


def python_to_wsc_level(level: int) -> int:
    """Translate Client levels to Server Levels"""
    if level == log.NOTSET:
        return LogSettings.LogLevel.NOTSET
    if level <= log.TRACE:
        return LogSettings.LogLevel.TRACE
    if level <= log.DEBUG:
        return LogSettings.LogLevel.DEBUG
    if level <= log.VERBOSE:
        return LogSettings.LogLevel.VERBOSE
    if level <= log.INFO:
        return LogSettings.LogLevel.INFO
    if level <= log.WARNING:
        return LogSettings.LogLevel.WARNING
    if level <= log.ERROR:
        return LogSettings.LogLevel.ERROR
    if level <= log.FATAL:
        return LogSettings.LogLevel.FATAL
    return LogSettings.LogLevel.FATAL


def wsc_to_python_level(level: int) -> int:
    """Translate Server levels to Client Levels"""
    # Our proto levels are fixed and not ordered
    # so only do exact equality
    if level == LogSettings.LogLevel.NOTSET:
        return log.NOTSET
    if level == LogSettings.LogLevel.TRACE:
        return log.TRACE
    if level == LogSettings.LogLevel.DEBUG:
        return log.DEBUG
    if level == LogSettings.LogLevel.VERBOSE:
        return log.VERBOSE
    if level == LogSettings.LogLevel.INFO:
        return log.INFO
    if level == LogSettings.LogLevel.WARNING:
        return log.WARNING
    if level == LogSettings.LogLevel.ERROR:
        return log.ERROR
    if level == LogSettings.LogLevel.FATAL:
        return log.FATAL
    return log.FATAL


def poll_topic(
    client_kwargs: dict,
    stop_events: Iterable[threading.Event],
    logger: log._CerebrasLogger,
    topic: ValidTopics,
    timeout: int = 15,
):
    """Poll Server for messages in a topic queue and log results"""

    def is_done():
        return any(event.is_set() for event in stop_events)

    client = ApplianceClient(**client_kwargs, disable_version_check=True)
    pbar = None
    while not is_done():
        try:
            response = client.get_msg(topic, timeout)
        except grpc.RpcError as e:
            if is_done():
                break
            logger.debug(
                f"Polling topic {ValidTopics.Name(topic)} ran into error: {e} "
                f"Retrying ..."
            )
            time.sleep(1)
            continue

        # Do something with response (Assumes SINGLE PROGRESS BAR at a time)
        # 0. if empty continue
        if len(response.status.msg) == 0 and response.progress.total_steps == 0:
            # TODO probably want a non_empty bit for ease of use
            if pbar:
                # tqdm progress bar only updates when iteration changes
                # (there are settings that are intended to allow more frequent
                # updates, but they don't work as intended). So refresh even if
                # there are no updates.
                # Refresh interval = timeout
                pbar.refresh()
            continue
        # 1. if not in progress bar
        elif pbar is None:
            # a. response is progress: enter progress bar
            if response.progress.total_steps > 0:
                if sys.stdout.isatty():
                    pbar = tqdm(
                        total=response.progress.total_steps,
                        dynamic_ncols=True,  # Match console width
                        file=sys.stdout,
                        # Custom format:
                        # - Remove "n_fmt/total_fmt" as the step counts/units are
                        #   not for the user
                        # - Remove "remaining" time as it's quite misleading for
                        #   uneven iteration times
                        bar_format="{desc} {percentage:3.0f}%|{bar}| {elapsed} {postfix}",
                    )
                    pbar.set_description(response.progress.prefix)
                    if response.progress.postfix:
                        pbar.set_postfix(note=response.progress.postfix)
                    pbar.update(n=response.progress.step_increment)
                elif response.progress.current_step == 0:
                    # No progress bar if not tty. Only show message when the
                    # progress bar is initialized.
                    log_level = wsc_to_python_level(response.progress.tag.level)
                    logger.log(log_level, response.progress.prefix)
            # b. response is status: write to logger
            else:
                log_level, formatted_output = format_status(response.status)
                logger.log(log_level, formatted_output)
        # 2. in progress bar
        else:
            # a. response is progress: update bar
            if response.progress.total_steps > 0:
                pbar.set_description(response.progress.prefix)
                if response.progress.postfix:
                    pbar.set_postfix(note=response.progress.postfix)
                else:
                    pbar.set_postfix()
                pbar.update(n=response.progress.step_increment)
                # i. If total reached clear progress bar
                if pbar.n >= pbar.total:
                    pbar.close()
                    pbar = None

            # b. response is status: tqdm write (how does that interact with logger?)
            else:
                _, formatted_output = format_status(response.status)
                pbar.write(formatted_output)


def format_status(status: MsgStatus) -> Tuple[int, str]:
    """Display format for Message Queue"""
    log_level = wsc_to_python_level(status.tag.level)
    status_string = f"{status.msg}"
    if len(status.action) > 0:
        status_string = (
            status_string + "\n" + textwrap.indent(status.action, 3 * " ")
        )
    # TODO handle message tags and internal message content
    return log_level, status_string


def log_failed_job_events(logger, job_events: List[JobEvent]):
    """Friendly logging explaining JobEvents and their relevant config"""
    replica_type_mem_runconfig = {
        "activation": "act_memory_gi",
        "command": "cmd_memory_gi",
        "coordinator": "compile_crd_memory_gi, execute_crd_memory_gi",
        "weight": "wgt_memory_gi",
        "worker": "wrk_memory_gi",
    }
    pod_replica_type_re = re.compile(r"^wsjob-[^-\s]+-([^-\s]+)-\d+$")

    for event in job_events:
        msg = str(
            f"Event {event.lastTimestamp} reason={event.reason.strip()} "
            f"object={event.name.strip()} message='{event.message.strip()}'"
        )
        details = ""
        if event.reason == "OOMKilled":
            m = pod_replica_type_re.match(event.name)
            if m:
                rt = m.groups()[0]
                if rt in replica_type_mem_runconfig:
                    params = replica_type_mem_runconfig[rt]
                    details = str(
                        f"You can attempt to override the default "
                        f"memory limit using runconfig params ({params}) and "
                        "check node capacity with `csctl get nodegroups`. "
                        "Note that increasing memory can lead to unschedulable "
                        "jobs."
                    )
        elif event.reason == "SchedulingFailed":
            params_str = ", ".join(sorted(replica_type_mem_runconfig.values()))
            details = str(
                f"If memory was the limiting resource, you can attempt to "
                f"override the default using a runconfig param ({params_str}) "
                "and check node capacity with `csctl get nodegroups`"
            )

        if details:
            msg += f" details={details}"
        logger.warning(msg)
