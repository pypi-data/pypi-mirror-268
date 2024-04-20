# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""This file contains utility methods which help when using cegal.pythontoolpro
"""

from .from_dataframe import _WELL_KNOWN_SPATIAL_COLUMN_NAMES
from .named_tuples import ContinuousDimensionInfoTuple

def get_continuous_value_info(petrel_obj) -> ContinuousDimensionInfoTuple:
    """This method returns a ContinuousDimensionInfoTuple based on the information from the supplied petrel_obj.

    It assumes the petrel_obj is a cegal.pythontoolpro representation of a Petrel object and tries to access the properties
    and methods on this object that it needs to construct a ContinuousDimensionInfoTuple containing the information describing
    the values of the object

    Args:
        petrel_obj: A cegal.pythontoolpro representation on a Petrel object

    Returns:
        ContinuousDimensionInfoTuple: A named tuple describing the values reporesenting a continuous dimension
    """
    symbol = petrel_obj.unit_symbol
    is_logarithmic = False
    min_value = None
    max_value = None

    stats = petrel_obj.retrieve_stats()

    if symbol is None:
        symbol = " "
    if "permeability" in petrel_obj.template.lower() or "resistivity" in petrel_obj.template.lower():
        is_logarithmic = True
    if "Seismic (template) Min" in stats.keys():
        min_value = float(stats["Seismic (template) Min"])
    if "Seismic (template) Max" in stats.keys():
        max_value = float(stats["Seismic (template) Max"])

    return ContinuousDimensionInfoTuple(property_name=petrel_obj.template, unit_symbol=symbol, is_logarithmic=is_logarithmic, min=min_value, max=max_value)

def get_spatial_value_info(project_units, spatial_dimension_name: str) -> ContinuousDimensionInfoTuple:
    """This method returns a ContinuousDimensionInfoTuples that describes the requested spatial unit based on the information
    from the supplied project_units.

    It assumes the project_units is a cegal.pythontoolpro object describing the a Petrel project units and tries to access the object
    to construct a ContinuousDimensionInfoTuple

    Args:
        project_units: A cegal.pythontoolpro object describing a Petrel projects units
        spatial_dimension_name (str): The name of the spatial dimension (must be one of ['X', 'Y', 'Z', 'TVD', 'TWT'])

    Returns:
        ContinuousDimensionInfoTuple: A named tuple describing the units for spatial data for data from this project
    """
    if project_units is None:
        raise ValueError("project_units must be defined")

    if spatial_dimension_name == 'X':
        return ContinuousDimensionInfoTuple(property_name="X distance", unit_symbol=project_units["XY unit"])
    elif spatial_dimension_name == 'Y':
        return ContinuousDimensionInfoTuple(property_name="Y distance", unit_symbol=project_units["XY unit"])
    elif spatial_dimension_name == 'Z':
        return ContinuousDimensionInfoTuple(property_name="Elevation depth", unit_symbol=project_units["Z unit"])
    elif spatial_dimension_name == 'TVD':
        return ContinuousDimensionInfoTuple(property_name="Elevation depth", unit_symbol=project_units["Z unit"])
    if spatial_dimension_name == 'TWT':
        return ContinuousDimensionInfoTuple(property_name="Elevation time", unit_symbol=project_units["Seismic time"])
    else:
        raise ValueError(f"spatial_dimension_name ('{spatial_dimension_name}') must be one of {str(_WELL_KNOWN_SPATIAL_COLUMN_NAMES)}")
