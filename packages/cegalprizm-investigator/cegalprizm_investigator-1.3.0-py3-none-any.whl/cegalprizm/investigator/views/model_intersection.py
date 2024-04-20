# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""This file contains the definition of the ModelIntersectionView class
"""

from typing import List, Sequence, Tuple, Union

# pylint: disable=relative-beyond-top-level
# pylint: disable=protected-access

from ..inv.investigation import Investigation
from .options_colorscale import OptionsColorscale
from .predefined_view import PredefinedView
from .predefined_view_tuple import PredefinedViewTuple


class ModelIntersectionView(OptionsColorscale, PredefinedView):
    """A class representing a ModelIntersectionView

    The view defines how a model intersection should be displayed.
    It allows control of both what data should be displayed and how the the data should be rendered.
    """

    def __init__(self, investigation: Investigation):
        super().__init__(investigation, "ModelIntersection")

    def copy(self):
        """Create a copy of this view

        Returns:
            ModelIntersectionView: the copied view
        """
        copy = ModelIntersectionView(None)
        copy._investigation = self._investigation
        copy._plot_type = self._plot_type
        copy._options = self._options
        copy._data.CopyFrom(self._data)
        copy._dataset_priority_order = list(self._dataset_priority_order)
        return copy

    ######################################################################
    # Multi-Views
    ######################################################################

    def create_property_views(self, property_names: Union[str, Sequence[str]] = "all") -> List[PredefinedViewTuple]:
        """Creates a copy of this view for each property specified

        Args:
            property_names (Union[str, Sequence[str]], optional): Defaults to 'all'.
                                - 'all' will duplicate the view for all the valid properties from the investigation
                                - a list of property names to be used

        Returns:
            List[PredefinedViewTuple]: a list of views; one per specified property
        """
        if property_names is None:
            raise ValueError("property_names must be defined")
        elif property_names == "all":
            property_names = [x.name for x in self._options.intersection_settings.available_properties]
        elif isinstance(property_names, list):
            if len(property_names) == 0:
                raise ValueError("property_names must contain at least 1 entry")
        else:
            raise ValueError("property_names is not valid")

        views = []
        for name in property_names:
            view = self.copy()
            view.set_property(name)
            views.append(PredefinedViewTuple(name=name, view=view))
        return views

    def create_borehole_views(self, borehole_names: Union[str, Sequence[str]] = "all") -> List[PredefinedViewTuple]:
        """Creates a copy of this view for each borehole specified

        Args:
            borehole_names (Union[str, Sequence[str]], optional): Defaults to 'all'.
                                - 'all' will duplicate the view for all the valid boreholes in the investigation
                                - a list of boreholes to be used

        Returns:
            List[PredefinedViewTuple]: a list of views; one per specified borehole
        """
        if borehole_names is None:
            raise ValueError("property_names must be defined")
        elif borehole_names == "all":
            borehole_names = [x.name for x in self._options.intersection_settings.available_boreholes]
        elif isinstance(borehole_names, list):
            if len(borehole_names) == 0:
                raise ValueError("borehole_names must contain at least 1 entry")
        else:
            raise ValueError("borehole_names is not valid")

        views = []
        for name in borehole_names:
            view = self.copy()
            view.set_borehole(name)
            views.append(PredefinedViewTuple(name=name, view=view))
        return views

    ######################################################################
    # Intersection settings
    ######################################################################

    def set_property(self, property_name: str):
        """Sets the property to be shown in the view

        Args:
            property_name (str): The name of the property to be used

        Raises:
            ValueError: if the property_name is not a valid property
        """
        property_id = self.__get_property_id(property_name)
        self._data.intersection_settings.selected_property = property_id

    def set_grid(self, grid: str):
        """Sets the grid to be shown in the view

        Args:
            grid (str): The name of the grid to be used

        Raises:
            ValueError: if the property_name is not a valid property
        """
        option = next((x.id for x in self._options.intersection_settings.available_grids if x.name == grid), None)
        if option is None:
            options = [x.name for x in self._options.intersection_settings.available_grids]
            raise ValueError(f"grid ('{grid}') must be one of {str(options)}")
        self._data.intersection_settings.selected_grid = option

    def use_grid_range(self, use_grid_range: bool):
        """Set whether the intersection shown in the view should be zoomed to fill the view or 
        whether the view should so the entire grid range

        Args:
            use_grid_range (bool): Should the intersecti0n view use the grid range
        """
        self._data.intersection_settings.use_grid_range = use_grid_range

    def get_north_south_range(self) -> Tuple[float, float]:
        """Gets the north-south range of the model

        Returns:
            Tuple[float, float]: A tuple containing the value range for the north-south intersections
        """
        return (self._options.intersection_settings.range_north_south.min, self._options.intersection_settings.range_north_south.max)

    def set_north_south(self, value: Union[float, int]):
        """Set the location of the north-south intersection

        Args:
            value (Union[float, int]): The location of the intersection to be used

        Raises:
            ValueError: if the value is not valid
        """
        if value < self._options.intersection_settings.range_north_south.min or value > self._options.intersection_settings.range_north_south.max:
            raise ValueError(f"value must be between {self._options.intersection_settings.range_north_south.min} and {self._options.intersection_settings.range_north_south.max}")
        self._data.intersection_settings.selected_intersection_type = "ns"
        self._data.intersection_settings.selected_north_south = value

    def get_east_west_range(self) -> Tuple[float, float]:
        """Gets the east-west range of the model

        Returns:
            Tuple[float, float]: A tuple containing the value range for the east-west intersections
        """
        return (self._options.intersection_settings.range_east_west.min, self._options.intersection_settings.range_east_west.max)

    def set_east_west(self, value: Union[float, int]):
        """Set the location of the east-west intersection

        Args:
            value (Union[float, int]): The location of the intersection to be used

        Raises:
            ValueError: if the value is not valid
        """
        if value < self._options.intersection_settings.range_east_west.min or value > self._options.intersection_settings.range_east_west.max:
            raise ValueError(f"value must be between {self._options.intersection_settings.range_east_west.min} and {self._options.intersection_settings.range_east_west.max}")
        self._data.intersection_settings.selected_intersection_type = "ew"
        self._data.intersection_settings.selected_east_west = value

    def get_i_range(self) -> Tuple[int, int]:
        """Gets the i range of the model

        Returns:
            Tuple[int, int]: A tuple containing the value range for the i index
        """
        return (self._options.intersection_settings.range_i.min, self._options.intersection_settings.range_i.max)
    
    def set_i(self, value: int):
        """Set the i slice to show

        Args:
            value (int): The i slice index to be used

        Raises:
            ValueError: if the value is not valid
        """
        if value < self._options.intersection_settings.range_i.min or value > self._options.intersection_settings.range_i.max:
            raise ValueError(f"value must be between {self._options.intersection_settings.range_i.min} and {self._options.intersection_settings.range_i.max}")
        self._data.intersection_settings.selected_intersection_type = "i"
        self._data.intersection_settings.selected_i = value

    def get_j_range(self) -> Tuple[int, int]:
        """Gets the j range of the model

        Returns:
            Tuple[int, int]: A tuple containing the value range for the j index
        """
        return (self._options.intersection_settings.range_j.min, self._options.intersection_settings.range_j.max)
    
    def set_j(self, value: int):
        """Set the j slice to show

        Args:
            value (int): The j slice index to be used

        Raises:
            ValueError: if the value is not valid
        """
        if value < self._options.intersection_settings.range_j.min or value > self._options.intersection_settings.range_j.max:
            raise ValueError(f"value must be between {self._options.intersection_settings.range_j.min} and {self._options.intersection_settings.range_j.max}")
        self._data.intersection_settings.selected_intersection_type = "j"
        self._data.intersection_settings.selected_j = value

    def set_borehole(self, borehole_name: str):
        """Sets the borhole for which the intersection should be shown

        Args:
            borehole (str): The borehole name

        Raises:
            ValueError: if the breohole is not valid
        """
        borehole_id = self.__get_borehole_id(borehole_name)
        self._data.intersection_settings.selected_intersection_type = "borehole"
        self._data.intersection_settings.selected_borehole = borehole_id

    ######################################################################
    # Private methods
    ######################################################################

    def __get_property_id(self, property_name: str) -> str:
        property_id = next((x.id for x in self._options.intersection_settings.available_properties if x.name == property_name), None)
        if property_id is None:
            options = [x.name for x in self._options.intersection_settings.available_properties]
            raise ValueError(f"property_name ('{property_name}') must be one of {str(options)}")
        return property_id

    def __get_borehole_id(self, name: str):
        borehole_id = next((x.id for x in self._options.intersection_settings.available_boreholes if x.name == name), None)
        if borehole_id is None:
            options = [x.name for x in self._options.intersection_settings.available_boreholes]
            raise ValueError(f"name ('{name}') must be one of {str(options)}")
        return borehole_id
