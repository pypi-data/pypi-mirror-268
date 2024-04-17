"""SinCurve"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIN_CURVE = python_net_import("SMT.MastaAPI.MathUtility", "SinCurve")


__docformat__ = "restructuredtext en"
__all__ = ("SinCurve",)


Self = TypeVar("Self", bound="SinCurve")


class SinCurve(_0.APIBase):
    """SinCurve

    This is a mastapy class.
    """

    TYPE = _SIN_CURVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SinCurve")

    class _Cast_SinCurve:
        """Special nested class for casting SinCurve to subclasses."""

        def __init__(self: "SinCurve._Cast_SinCurve", parent: "SinCurve"):
            self._parent = parent

        @property
        def sin_curve(self: "SinCurve._Cast_SinCurve") -> "SinCurve":
            return self._parent

        def __getattr__(self: "SinCurve._Cast_SinCurve", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SinCurve.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @number_of_cycles.setter
    @enforce_parameter_types
    def number_of_cycles(self: Self, value: "float"):
        self.wrapped.NumberOfCycles = float(value) if value is not None else 0.0

    @property
    def starting_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartingAngle

        if temp is None:
            return 0.0

        return temp

    @starting_angle.setter
    @enforce_parameter_types
    def starting_angle(self: Self, value: "float"):
        self.wrapped.StartingAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "SinCurve._Cast_SinCurve":
        return self._Cast_SinCurve(self)
