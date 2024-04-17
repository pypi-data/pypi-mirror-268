"""PlanetPinWindup"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_PIN_WINDUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "PlanetPinWindup",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetPinWindup",)


Self = TypeVar("Self", bound="PlanetPinWindup")


class PlanetPinWindup(_0.APIBase):
    """PlanetPinWindup

    This is a mastapy class.
    """

    TYPE = _PLANET_PIN_WINDUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetPinWindup")

    class _Cast_PlanetPinWindup:
        """Special nested class for casting PlanetPinWindup to subclasses."""

        def __init__(
            self: "PlanetPinWindup._Cast_PlanetPinWindup", parent: "PlanetPinWindup"
        ):
            self._parent = parent

        @property
        def planet_pin_windup(
            self: "PlanetPinWindup._Cast_PlanetPinWindup",
        ) -> "PlanetPinWindup":
            return self._parent

        def __getattr__(self: "PlanetPinWindup._Cast_PlanetPinWindup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetPinWindup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAxialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeRadialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_tangential_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeTangentialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_wind_up(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalWindUp

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "PlanetPinWindup._Cast_PlanetPinWindup":
        return self._Cast_PlanetPinWindup(self)
