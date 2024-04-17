"""NamedSpeed"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "NamedSpeed"
)


__docformat__ = "restructuredtext en"
__all__ = ("NamedSpeed",)


Self = TypeVar("Self", bound="NamedSpeed")


class NamedSpeed(_0.APIBase):
    """NamedSpeed

    This is a mastapy class.
    """

    TYPE = _NAMED_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedSpeed")

    class _Cast_NamedSpeed:
        """Special nested class for casting NamedSpeed to subclasses."""

        def __init__(self: "NamedSpeed._Cast_NamedSpeed", parent: "NamedSpeed"):
            self._parent = parent

        @property
        def named_speed(self: "NamedSpeed._Cast_NamedSpeed") -> "NamedSpeed":
            return self._parent

        def __getattr__(self: "NamedSpeed._Cast_NamedSpeed", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedSpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    @enforce_parameter_types
    def speed(self: Self, value: "float"):
        self.wrapped.Speed = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "NamedSpeed._Cast_NamedSpeed":
        return self._Cast_NamedSpeed(self)
