"""Spec for legend of a Map Shape widget."""

from typing import Any

from engineai.sdk.dashboard.base import AbstractFactory
from engineai.sdk.dashboard.decorator import type_check
from engineai.sdk.dashboard.utils import generate_input


class MapStylingLabel(AbstractFactory):
    """Spec for Map Geo Styling Label of a Map widget."""

    @type_check
    def __init__(self, *, hidden: bool = False):
        """Construct a Styling Label for a Map Geo widget.

        Args:
            hidden: Hide labels.
        """
        super().__init__()
        self._hidden = hidden

    def build(self) -> Any:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return generate_input("MapGeoWidgetStylingLabel", hidden=self._hidden)
