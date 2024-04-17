# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Utilities to simplify run.py usage"""
from collections import defaultdict
from typing import List, Optional

from google.protobuf import json_format, text_format

from cerebras.appliance.pb.workflow.appliance.common.common_config_pb2 import (
    DebugArgs,
)


def get_supported_type_maps(debug_args):
    """Get the ini maps in the DebugArgs for supported types"""
    ini_maps = {
        bool: debug_args.ini.bools,
        int: debug_args.ini.ints,
        float: debug_args.ini.floats,
        str: debug_args.ini.strings,
    }
    return ini_maps


def write_debug_args(debug_args: DebugArgs, path: str):
    """Appliance mode write debug args file"""
    with open(path, 'w') as f:
        text_format.PrintMessage(debug_args, f)


def get_debug_args(path: Optional[str]) -> DebugArgs:
    """Appliance mode load debug args and apply defaults"""
    debug_args = DebugArgs()
    if path:
        with open(path, 'r') as f:
            text_format.Parse(f.read(), debug_args)
    return debug_args


def update_debug_args_from_keys(debug_args: DebugArgs, flat_dargs: dict):
    """
    Update DebugArgs from a dict using dotted-field notation to refer to
    nested objects.
    """

    def nested_defaultdict():
        return defaultdict(nested_defaultdict)

    dict_dargs = nested_defaultdict()

    # First, handle both the dotted flat dict keys and nested dict values into
    # a full dict matching the proto message schema.
    def recursive_merge(d, nd):
        for key, value in nd.items():
            subkeys = key.split(".")
            obj = d
            for subkey in subkeys[:-1]:
                obj = obj[subkey]
            key = subkeys[-1]

            if isinstance(value, dict):
                recursive_merge(obj[key], value)
            else:
                obj[key] = value

    recursive_merge(dict_dargs, flat_dargs)

    # Now, convert this nested dict to the proto message
    json_format.ParseDict(dict_dargs, debug_args)


def set_ini(debug_args: DebugArgs, **kwargs):
    """Set an Debug INI in the DebugArgs"""
    ini_maps = get_supported_type_maps(debug_args)
    for k, v in kwargs.items():
        maps = ini_maps.get(type(v))
        if maps is None:
            raise TypeError(
                f"\"{k}\"={v} is of unsupported type {type(v)}. Only "
                f"{list(ini_maps.keys())} types are supported INI values."
            )
        maps[k] = v


def set_default_ini(debug_args: DebugArgs, **kwargs):
    """Set default INI in the DebugArgs, if INI is not set"""
    ini_maps = get_supported_type_maps(debug_args)

    for k, v in kwargs.items():
        maps = ini_maps.get(type(v))
        if maps is None:
            raise TypeError(
                f"\"{k}\"={v} is of unsupported type {type(v)}. Only "
                f"{list(ini_maps.keys())} types are supported INI values."
            )
        if k not in maps:
            maps[k] = v


def clear_ini(debug_args: DebugArgs, *args):
    """Unsets INIs in DebugArgs."""
    ini_maps = get_supported_type_maps(debug_args)

    for k in args:
        for ini_map in ini_maps.values():
            ini_map.pop(k, None)


def update_debug_args_with_job_labels(
    debug_args: DebugArgs, job_labels: Optional[List[str]] = None
):
    """Update debug args with job labels"""
    if not job_labels:
        return

    for label in job_labels:
        tokens = label.split("=")
        label_key = tokens[0]
        label_val = tokens[1]
        debug_args.debug_mgr.labels[label_key] = label_val
