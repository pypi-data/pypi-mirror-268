"""PlanetaryDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_DETAIL = python_net_import("SMT.MastaAPI.Gears", "PlanetaryDetail")

if TYPE_CHECKING:
    from mastapy.gears import _342


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryDetail",)


Self = TypeVar("Self", bound="PlanetaryDetail")


class PlanetaryDetail(_0.APIBase):
    """PlanetaryDetail

    This is a mastapy class.
    """

    TYPE = _PLANETARY_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryDetail")

    class _Cast_PlanetaryDetail:
        """Special nested class for casting PlanetaryDetail to subclasses."""

        def __init__(
            self: "PlanetaryDetail._Cast_PlanetaryDetail", parent: "PlanetaryDetail"
        ):
            self._parent = parent

        @property
        def planetary_detail(
            self: "PlanetaryDetail._Cast_PlanetaryDetail",
        ) -> "PlanetaryDetail":
            return self._parent

        def __getattr__(self: "PlanetaryDetail._Cast_PlanetaryDetail", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_planet_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstPlanetAngle

        if temp is None:
            return 0.0

        return temp

    @first_planet_angle.setter
    @enforce_parameter_types
    def first_planet_angle(self: Self, value: "float"):
        self.wrapped.FirstPlanetAngle = float(value) if value is not None else 0.0

    @property
    def number_of_planets(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPlanets

        if temp is None:
            return 0

        return temp

    @number_of_planets.setter
    @enforce_parameter_types
    def number_of_planets(self: Self, value: "int"):
        self.wrapped.NumberOfPlanets = int(value) if value is not None else 0

    @property
    def planet_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetDiameter

        if temp is None:
            return 0.0

        return temp

    @planet_diameter.setter
    @enforce_parameter_types
    def planet_diameter(self: Self, value: "float"):
        self.wrapped.PlanetDiameter = float(value) if value is not None else 0.0

    @property
    def regularly_spaced_planets(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RegularlySpacedPlanets

        if temp is None:
            return False

        return temp

    @regularly_spaced_planets.setter
    @enforce_parameter_types
    def regularly_spaced_planets(self: Self, value: "bool"):
        self.wrapped.RegularlySpacedPlanets = (
            bool(value) if value is not None else False
        )

    @property
    def planet_delta_angles(self: Self) -> "List[_342.NamedPlanetAngle]":
        """List[mastapy.gears.NamedPlanetAngle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetDeltaAngles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PlanetaryDetail._Cast_PlanetaryDetail":
        return self._Cast_PlanetaryDetail(self)
