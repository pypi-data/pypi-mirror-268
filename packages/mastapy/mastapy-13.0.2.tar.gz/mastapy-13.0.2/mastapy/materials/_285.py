"""SNCurvePoint"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SN_CURVE_POINT = python_net_import("SMT.MastaAPI.Materials", "SNCurvePoint")


__docformat__ = "restructuredtext en"
__all__ = ("SNCurvePoint",)


Self = TypeVar("Self", bound="SNCurvePoint")


class SNCurvePoint(_0.APIBase):
    """SNCurvePoint

    This is a mastapy class.
    """

    TYPE = _SN_CURVE_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SNCurvePoint")

    class _Cast_SNCurvePoint:
        """Special nested class for casting SNCurvePoint to subclasses."""

        def __init__(self: "SNCurvePoint._Cast_SNCurvePoint", parent: "SNCurvePoint"):
            self._parent = parent

        @property
        def sn_curve_point(self: "SNCurvePoint._Cast_SNCurvePoint") -> "SNCurvePoint":
            return self._parent

        def __getattr__(self: "SNCurvePoint._Cast_SNCurvePoint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SNCurvePoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SNCurvePoint._Cast_SNCurvePoint":
        return self._Cast_SNCurvePoint(self)
