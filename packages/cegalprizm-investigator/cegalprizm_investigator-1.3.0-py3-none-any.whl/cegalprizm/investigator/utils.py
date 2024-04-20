# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""This file contains private methods which should only be used internally
"""

import os
from google.protobuf.any_pb2 import Any
import webcolors

# pylint: disable=relative-beyond-top-level

from .protos import common_pb2
from .protos import investigation_pb2

_CHUNK_SIZE = 2 * 1024 * 1024  # 2MB

def _get_envvar(key: str):
    env = os.environ
    try:
        return (True, env[key])
    except:
        return (False, "")


def _get_file_chunks(path: str):
    with open(path, 'rb') as file:
        while True:
            chunk = file.read(_CHUNK_SIZE)
            if len(chunk) == 0:
                return
            yield common_pb2.Chunk(buffer=chunk)


def _pack_payloads(messages):
    for message in messages:
        payload = Any()
        payload.Pack(message)
        yield payload


def _clamp(value: int, min_value: int, max_value: int) -> int:
    return max(min_value, min(value, max_value))


def _get_shape(shape: str) -> int:
    shape_key = next((x for x in common_pb2.ShapeEnum.keys() if x.lower() == shape), None)
    if shape_key is None:
        options = [x.lower() for x in common_pb2.ShapeEnum.keys()]
        raise ValueError(f"shape ('{shape}') must be one of {str(options)}")
    return common_pb2.ShapeEnum.Value(shape_key)


def _clamp_size(size: int) -> int:
    return _clamp(size, 1, 14)


def _get_numeric_precision(precision: str) -> int:
    precision_key = next((x for x in investigation_pb2.PrecisionEnum.keys() if x.lower() == precision), None)
    if precision_key is None:
        options = [x.lower() for x in investigation_pb2.PrecisionEnum.keys()]
        raise ValueError(f"precision ('{precision}') must be one of {str(options)}")
    return investigation_pb2.PrecisionEnum.Value(precision_key)


def _clamp_precision_value(precision: investigation_pb2.PrecisionEnum, value: int) -> int:
    if precision == investigation_pb2.PrecisionEnum.DecimalPlaces:
        options = range(0, 10)
    elif precision == investigation_pb2.PrecisionEnum.SignificantFigures:
        options = range(1, 10)
    elif precision == investigation_pb2.PrecisionEnum.Engineering:
        options = range(3, 10, 3)
    else:
        options = range(1, 10)

    clamped_value = _clamp(value, min(options), max(options))
    if clamped_value not in options:
        raise ValueError(f"value must be one of {str(options)}")
    return clamped_value


def _color_name_to_int(color_name: str) -> int:
    if color_name not in webcolors.CSS3_NAMES_TO_HEX.keys():
        raise ValueError(f"color_name ('{color_name}') not defined in webcolors")
    return int(webcolors.name_to_hex(color_name).replace("#", "0xFF"), 16)


def _get_dataset_geometry(dataset_geometry_type: investigation_pb2.DatasetGeometryEnum) -> str:
    return investigation_pb2.DatasetGeometryEnum.keys()[dataset_geometry_type].lower()
