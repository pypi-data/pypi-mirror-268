"""Spec for MapSryling of a Map Geo widget."""

from typing import Any
from typing import Optional

from engineai.sdk.dashboard.base import AbstractFactory
from engineai.sdk.dashboard.decorator import type_check
from engineai.sdk.dashboard.utils import generate_input

from .label import MapStylingLabel


class MapStyling(AbstractFactory):
    """Spec for MapStyling of a Map Geo widget."""

    @type_check
    def __init__(self, *, label: Optional[MapStylingLabel] = None):
        """Construct a Styling for a Map Geo widget.

        Args:
            label: label style for map
        """
        super().__init__()
        self._label = label if label is not None else MapStylingLabel()

    def build(self) -> Any:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return generate_input(
            "MapGeoWidgetStylingInput",
            label=self._label.build(),
        )
