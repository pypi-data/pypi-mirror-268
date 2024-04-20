# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import Type, Optional, Sequence

from google.protobuf.any_pb2 import Any

from .. import logger
from ..exceptions import CegalHubError
from ..protos import investigator_api_pb2
from ..utils import _pack_payloads

from .investigation import Investigation

def _create_borehole_intersections(investigation: Type[Investigation], grid_names: Sequence[str]):
    dataset_tuples = list(investigation._get_datasets(investigation._datasets))

    msg = investigator_api_pb2.CreateIntersections()
    msg.investigation_id.id = investigation._info.id
    msg.create_borehole_intersections = True
    msg.create_maps = False

    for name in grid_names:
        found = False
        for t in dataset_tuples:
            if t[0].name == name:
                msg.selected_grids.append(t[0].id)
                found = True
        if not found:
            raise ValueError(f"{name} is not valid")

    payload = Any()
    payload.Pack(msg)

    result = investigation._hub_context.do_unary_request("investigator.CreateIntersections", payload)
    if result[0]:
        investigation.refresh()
        return
    else:
        raise CegalHubError(result[1])

def _create_map_intersections(investigation: Type[Investigation], grid_names: Sequence[str]):
    dataset_tuples = list(investigation._get_datasets(investigation._datasets))

    msg = investigator_api_pb2.CreateIntersections()
    msg.investigation_id.id = investigation._info.id
    msg.create_borehole_intersections = False
    msg.create_maps = True

    for name in grid_names:
        found = False
        for t in dataset_tuples:
            if t[0].name == name:
                msg.selected_grids.append(t[0].id)
                found = True
        if not found:
            raise ValueError(f"{name} is not valid")

    payload = Any()
    payload.Pack(msg)

    result = investigation._hub_context.do_unary_request("investigator.CreateIntersections", payload)
    if result[0]:
        investigation.refresh()
        return
    else:
        raise CegalHubError(result[1])