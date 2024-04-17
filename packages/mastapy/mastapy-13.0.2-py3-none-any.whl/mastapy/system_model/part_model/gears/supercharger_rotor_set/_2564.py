"""PressureRatioInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_RATIO_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "PressureRatioInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("PressureRatioInputOptions",)


Self = TypeVar("Self", bound="PressureRatioInputOptions")


class PressureRatioInputOptions(_1854.ColumnInputOptions):
    """PressureRatioInputOptions

    This is a mastapy class.
    """

    TYPE = _PRESSURE_RATIO_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PressureRatioInputOptions")

    class _Cast_PressureRatioInputOptions:
        """Special nested class for casting PressureRatioInputOptions to subclasses."""

        def __init__(
            self: "PressureRatioInputOptions._Cast_PressureRatioInputOptions",
            parent: "PressureRatioInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "PressureRatioInputOptions._Cast_PressureRatioInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def pressure_ratio_input_options(
            self: "PressureRatioInputOptions._Cast_PressureRatioInputOptions",
        ) -> "PressureRatioInputOptions":
            return self._parent

        def __getattr__(
            self: "PressureRatioInputOptions._Cast_PressureRatioInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PressureRatioInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reference_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferencePressure

        if temp is None:
            return 0.0

        return temp

    @reference_pressure.setter
    @enforce_parameter_types
    def reference_pressure(self: Self, value: "float"):
        self.wrapped.ReferencePressure = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "PressureRatioInputOptions._Cast_PressureRatioInputOptions":
        return self._Cast_PressureRatioInputOptions(self)
