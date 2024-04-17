"""NamedPlanetAngle"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_PLANET_ANGLE = python_net_import("SMT.MastaAPI.Gears", "NamedPlanetAngle")


__docformat__ = "restructuredtext en"
__all__ = ("NamedPlanetAngle",)


Self = TypeVar("Self", bound="NamedPlanetAngle")


class NamedPlanetAngle(_0.APIBase):
    """NamedPlanetAngle

    This is a mastapy class.
    """

    TYPE = _NAMED_PLANET_ANGLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedPlanetAngle")

    class _Cast_NamedPlanetAngle:
        """Special nested class for casting NamedPlanetAngle to subclasses."""

        def __init__(
            self: "NamedPlanetAngle._Cast_NamedPlanetAngle", parent: "NamedPlanetAngle"
        ):
            self._parent = parent

        @property
        def named_planet_angle(
            self: "NamedPlanetAngle._Cast_NamedPlanetAngle",
        ) -> "NamedPlanetAngle":
            return self._parent

        def __getattr__(self: "NamedPlanetAngle._Cast_NamedPlanetAngle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedPlanetAngle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetAngle

        if temp is None:
            return 0.0

        return temp

    @planet_angle.setter
    @enforce_parameter_types
    def planet_angle(self: Self, value: "float"):
        self.wrapped.PlanetAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "NamedPlanetAngle._Cast_NamedPlanetAngle":
        return self._Cast_NamedPlanetAngle(self)
