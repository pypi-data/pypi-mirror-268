"""NDChartDefinition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility.report import _1755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ND_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "NDChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1750
    from mastapy.utility_gui.charts import (
        _1859,
        _1864,
        _1867,
        _1869,
        _1872,
        _1873,
        _1874,
    )


__docformat__ = "restructuredtext en"
__all__ = ("NDChartDefinition",)


Self = TypeVar("Self", bound="NDChartDefinition")


class NDChartDefinition(_1755.ChartDefinition):
    """NDChartDefinition

    This is a mastapy class.
    """

    TYPE = _ND_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NDChartDefinition")

    class _Cast_NDChartDefinition:
        """Special nested class for casting NDChartDefinition to subclasses."""

        def __init__(
            self: "NDChartDefinition._Cast_NDChartDefinition",
            parent: "NDChartDefinition",
        ):
            self._parent = parent

        @property
        def chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1755.ChartDefinition":
            return self._parent._cast(_1755.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1859.BubbleChartDefinition":
            from mastapy.utility_gui.charts import _1859

            return self._parent._cast(_1859.BubbleChartDefinition)

        @property
        def matrix_visualisation_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1864.MatrixVisualisationDefinition":
            from mastapy.utility_gui.charts import _1864

            return self._parent._cast(_1864.MatrixVisualisationDefinition)

        @property
        def parallel_coordinates_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1867.ParallelCoordinatesChartDefinition":
            from mastapy.utility_gui.charts import _1867

            return self._parent._cast(_1867.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1869.ScatterChartDefinition":
            from mastapy.utility_gui.charts import _1869

            return self._parent._cast(_1869.ScatterChartDefinition)

        @property
        def three_d_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1872.ThreeDChartDefinition":
            from mastapy.utility_gui.charts import _1872

            return self._parent._cast(_1872.ThreeDChartDefinition)

        @property
        def three_d_vector_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1873.ThreeDVectorChartDefinition":
            from mastapy.utility_gui.charts import _1873

            return self._parent._cast(_1873.ThreeDVectorChartDefinition)

        @property
        def two_d_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "_1874.TwoDChartDefinition":
            from mastapy.utility_gui.charts import _1874

            return self._parent._cast(_1874.TwoDChartDefinition)

        @property
        def nd_chart_definition(
            self: "NDChartDefinition._Cast_NDChartDefinition",
        ) -> "NDChartDefinition":
            return self._parent

        def __getattr__(self: "NDChartDefinition._Cast_NDChartDefinition", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NDChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def specify_shared_chart_settings(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifySharedChartSettings

        if temp is None:
            return False

        return temp

    @specify_shared_chart_settings.setter
    @enforce_parameter_types
    def specify_shared_chart_settings(self: Self, value: "bool"):
        self.wrapped.SpecifySharedChartSettings = (
            bool(value) if value is not None else False
        )

    @property
    def x_axis(self: Self) -> "_1750.AxisSettings":
        """mastapy.utility.report.AxisSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def y_axis(self: Self) -> "_1750.AxisSettings":
        """mastapy.utility.report.AxisSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "NDChartDefinition._Cast_NDChartDefinition":
        return self._Cast_NDChartDefinition(self)
