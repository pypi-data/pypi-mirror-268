"""TimeOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "TimeOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("TimeOptions",)


Self = TypeVar("Self", bound="TimeOptions")


class TimeOptions(_0.APIBase):
    """TimeOptions

    This is a mastapy class.
    """

    TYPE = _TIME_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeOptions")

    class _Cast_TimeOptions:
        """Special nested class for casting TimeOptions to subclasses."""

        def __init__(self: "TimeOptions._Cast_TimeOptions", parent: "TimeOptions"):
            self._parent = parent

        @property
        def time_options(self: "TimeOptions._Cast_TimeOptions") -> "TimeOptions":
            return self._parent

        def __getattr__(self: "TimeOptions._Cast_TimeOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def end_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndTime

        if temp is None:
            return 0.0

        return temp

    @end_time.setter
    @enforce_parameter_types
    def end_time(self: Self, value: "float"):
        self.wrapped.EndTime = float(value) if value is not None else 0.0

    @property
    def start_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartTime

        if temp is None:
            return 0.0

        return temp

    @start_time.setter
    @enforce_parameter_types
    def start_time(self: Self, value: "float"):
        self.wrapped.StartTime = float(value) if value is not None else 0.0

    @property
    def total_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TotalTime

        if temp is None:
            return 0.0

        return temp

    @total_time.setter
    @enforce_parameter_types
    def total_time(self: Self, value: "float"):
        self.wrapped.TotalTime = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "TimeOptions._Cast_TimeOptions":
        return self._Cast_TimeOptions(self)
