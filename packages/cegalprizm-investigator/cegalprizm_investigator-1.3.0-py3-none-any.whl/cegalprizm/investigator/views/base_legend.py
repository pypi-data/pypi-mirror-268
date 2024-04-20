# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""This file contains the definition of the colorscale options class

This class is internal and is only exposed via inheritance
"""

# pylint: disable=relative-beyond-top-level
# pylint: disable=protected-access

from ..protos import predefined_view_pb2
from .predefined_view import PredefinedView

_OUTSIDE_VIEWPORT_CORNER_OPTIONS = ["left", "right"]
_INSIDE_VIEWPORT_CORNER_OPTIONS = ["top-left", "top-right", "bottom-left", "bottom-right"]

class BaseLegend(PredefinedView):

    def _set_legend_location(self, legend_settings: predefined_view_pb2.SettingsLegend, inside_viewport: bool, location: str):
        if not inside_viewport and location not in _OUTSIDE_VIEWPORT_CORNER_OPTIONS:
            raise ValueError(f"location ('{location}') must be one of {str(_OUTSIDE_VIEWPORT_CORNER_OPTIONS)}")
        if inside_viewport and location not in _INSIDE_VIEWPORT_CORNER_OPTIONS:
            raise ValueError(f"location ('{location}') must be one of {str(_INSIDE_VIEWPORT_CORNER_OPTIONS)}")
        legend_settings.inside_viewport = inside_viewport
        legend_settings.show_at_top = "top" in location
        legend_settings.show_at_left = "left" in location

    def _show_legend_frame(self, legend_settings, show_frame: bool):
        legend_settings.show_frame = show_frame
