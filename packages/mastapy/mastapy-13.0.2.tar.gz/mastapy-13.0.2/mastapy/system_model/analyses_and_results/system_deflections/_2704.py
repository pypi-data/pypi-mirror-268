"""BearingDynamicResultsPropertyWrapper"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_RESULTS_PROPERTY_WRAPPER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BearingDynamicResultsPropertyWrapper",
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingDynamicResultsPropertyWrapper",)


Self = TypeVar("Self", bound="BearingDynamicResultsPropertyWrapper")


class BearingDynamicResultsPropertyWrapper(_0.APIBase):
    """BearingDynamicResultsPropertyWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_RESULTS_PROPERTY_WRAPPER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDynamicResultsPropertyWrapper")

    class _Cast_BearingDynamicResultsPropertyWrapper:
        """Special nested class for casting BearingDynamicResultsPropertyWrapper to subclasses."""

        def __init__(
            self: "BearingDynamicResultsPropertyWrapper._Cast_BearingDynamicResultsPropertyWrapper",
            parent: "BearingDynamicResultsPropertyWrapper",
        ):
            self._parent = parent

        @property
        def bearing_dynamic_results_property_wrapper(
            self: "BearingDynamicResultsPropertyWrapper._Cast_BearingDynamicResultsPropertyWrapper",
        ) -> "BearingDynamicResultsPropertyWrapper":
            return self._parent

        def __getattr__(
            self: "BearingDynamicResultsPropertyWrapper._Cast_BearingDynamicResultsPropertyWrapper",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BearingDynamicResultsPropertyWrapper.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def plot_time_series(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PlotTimeSeries

        if temp is None:
            return False

        return temp

    @plot_time_series.setter
    @enforce_parameter_types
    def plot_time_series(self: Self, value: "bool"):
        self.wrapped.PlotTimeSeries = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "BearingDynamicResultsPropertyWrapper._Cast_BearingDynamicResultsPropertyWrapper":
        return self._Cast_BearingDynamicResultsPropertyWrapper(self)
