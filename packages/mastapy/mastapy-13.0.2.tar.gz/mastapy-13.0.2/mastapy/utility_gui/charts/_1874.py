"""TwoDChartDefinition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.utility_gui.charts import _1866
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_D_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "TwoDChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1860, _1870, _1859, _1864, _1867, _1869
    from mastapy.utility.report import _1755


__docformat__ = "restructuredtext en"
__all__ = ("TwoDChartDefinition",)


Self = TypeVar("Self", bound="TwoDChartDefinition")


class TwoDChartDefinition(_1866.NDChartDefinition):
    """TwoDChartDefinition

    This is a mastapy class.
    """

    TYPE = _TWO_D_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TwoDChartDefinition")

    class _Cast_TwoDChartDefinition:
        """Special nested class for casting TwoDChartDefinition to subclasses."""

        def __init__(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
            parent: "TwoDChartDefinition",
        ):
            self._parent = parent

        @property
        def nd_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1866.NDChartDefinition":
            return self._parent._cast(_1866.NDChartDefinition)

        @property
        def chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1755.ChartDefinition":
            from mastapy.utility.report import _1755

            return self._parent._cast(_1755.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1859.BubbleChartDefinition":
            from mastapy.utility_gui.charts import _1859

            return self._parent._cast(_1859.BubbleChartDefinition)

        @property
        def matrix_visualisation_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1864.MatrixVisualisationDefinition":
            from mastapy.utility_gui.charts import _1864

            return self._parent._cast(_1864.MatrixVisualisationDefinition)

        @property
        def parallel_coordinates_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1867.ParallelCoordinatesChartDefinition":
            from mastapy.utility_gui.charts import _1867

            return self._parent._cast(_1867.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1869.ScatterChartDefinition":
            from mastapy.utility_gui.charts import _1869

            return self._parent._cast(_1869.ScatterChartDefinition)

        @property
        def two_d_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "TwoDChartDefinition":
            return self._parent

        def __getattr__(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TwoDChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def const_lines(self: Self) -> "List[_1860.ConstantLine]":
        """List[mastapy.utility_gui.charts.ConstantLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConstLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def series_list(self: Self) -> "List[_1870.Series2D]":
        """List[mastapy.utility_gui.charts.Series2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeriesList

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "TwoDChartDefinition._Cast_TwoDChartDefinition":
        return self._Cast_TwoDChartDefinition(self)
