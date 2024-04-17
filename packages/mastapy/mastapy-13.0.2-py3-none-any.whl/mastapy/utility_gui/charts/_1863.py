"""LegacyChartMathChartDefinition"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEGACY_CHART_MATH_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "LegacyChartMathChartDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("LegacyChartMathChartDefinition",)


Self = TypeVar("Self", bound="LegacyChartMathChartDefinition")


class LegacyChartMathChartDefinition(_1755.ChartDefinition):
    """LegacyChartMathChartDefinition

    This is a mastapy class.
    """

    TYPE = _LEGACY_CHART_MATH_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LegacyChartMathChartDefinition")

    class _Cast_LegacyChartMathChartDefinition:
        """Special nested class for casting LegacyChartMathChartDefinition to subclasses."""

        def __init__(
            self: "LegacyChartMathChartDefinition._Cast_LegacyChartMathChartDefinition",
            parent: "LegacyChartMathChartDefinition",
        ):
            self._parent = parent

        @property
        def chart_definition(
            self: "LegacyChartMathChartDefinition._Cast_LegacyChartMathChartDefinition",
        ) -> "_1755.ChartDefinition":
            return self._parent._cast(_1755.ChartDefinition)

        @property
        def legacy_chart_math_chart_definition(
            self: "LegacyChartMathChartDefinition._Cast_LegacyChartMathChartDefinition",
        ) -> "LegacyChartMathChartDefinition":
            return self._parent

        def __getattr__(
            self: "LegacyChartMathChartDefinition._Cast_LegacyChartMathChartDefinition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LegacyChartMathChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LegacyChartMathChartDefinition._Cast_LegacyChartMathChartDefinition":
        return self._Cast_LegacyChartMathChartDefinition(self)
