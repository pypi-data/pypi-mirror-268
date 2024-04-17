"""BubbleChartDefinition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility_gui.charts import _1869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BUBBLE_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "BubbleChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874, _1866
    from mastapy.utility.report import _1755


__docformat__ = "restructuredtext en"
__all__ = ("BubbleChartDefinition",)


Self = TypeVar("Self", bound="BubbleChartDefinition")


class BubbleChartDefinition(_1869.ScatterChartDefinition):
    """BubbleChartDefinition

    This is a mastapy class.
    """

    TYPE = _BUBBLE_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BubbleChartDefinition")

    class _Cast_BubbleChartDefinition:
        """Special nested class for casting BubbleChartDefinition to subclasses."""

        def __init__(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
            parent: "BubbleChartDefinition",
        ):
            self._parent = parent

        @property
        def scatter_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1869.ScatterChartDefinition":
            return self._parent._cast(_1869.ScatterChartDefinition)

        @property
        def two_d_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1874.TwoDChartDefinition":
            from mastapy.utility_gui.charts import _1874

            return self._parent._cast(_1874.TwoDChartDefinition)

        @property
        def nd_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1866.NDChartDefinition":
            from mastapy.utility_gui.charts import _1866

            return self._parent._cast(_1866.NDChartDefinition)

        @property
        def chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1755.ChartDefinition":
            from mastapy.utility.report import _1755

            return self._parent._cast(_1755.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "BubbleChartDefinition":
            return self._parent

        def __getattr__(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BubbleChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BubbleChartDefinition._Cast_BubbleChartDefinition":
        return self._Cast_BubbleChartDefinition(self)
