# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""This file contains the definition of the colorscale options class

This class is internal and is only exposed via inheritance
"""

# pylint: disable=relative-beyond-top-level
# pylint: disable=protected-access

from ..protos import predefined_view_pb2
from .base_legend import BaseLegend

_CORNER_OPTIONS = ["top-left", "top-right", "bottom-left", "bottom-right"]

class OptionsColorscale(BaseLegend):
    """A class representing a colorscale
    """

    def show_colorscale(self, show: bool):
        """Set whether the points colorscale is shown

        Args:
            show (bool): Should the colorscale be shown
        """
        self._data.general_settings.show_points_colorscale = show

    def set_colorscale_location(self, inside_viewport: bool, location: str):
        """Set where in the plot the points colorscale is to be shown.

        Valid locations outside viewport are 'left' or 'right'
        Valid locations inside viewport are 'top-left' or 'top-right' or 'bottom-left' or 'bottom-right'

        Args:
            inside_viewport (bool): If True, the colorscale will be shown inside the viewport
            location (str): A string indicating the desired location of the colorscale

        Raises:
            ValueError: if the location is not a valid string
        """
        self._set_legend_location(self._data.general_settings.points_colorscale, inside_viewport, location)

    def show_colorscale_frame(self, show_frame: bool):
        """Set whether the frame should be shown around the points colorscale

        Args:
            show (bool): Should the colorscale be shown
        """
        self._show_legend_frame(self._data.general_settings.points_colorscale, show_frame)
