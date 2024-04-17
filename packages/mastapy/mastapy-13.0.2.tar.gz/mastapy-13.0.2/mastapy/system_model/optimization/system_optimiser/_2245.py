"""PlanetGearOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_GEAR_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization.SystemOptimiser", "PlanetGearOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetGearOptions",)


Self = TypeVar("Self", bound="PlanetGearOptions")


class PlanetGearOptions(_0.APIBase):
    """PlanetGearOptions

    This is a mastapy class.
    """

    TYPE = _PLANET_GEAR_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetGearOptions")

    class _Cast_PlanetGearOptions:
        """Special nested class for casting PlanetGearOptions to subclasses."""

        def __init__(
            self: "PlanetGearOptions._Cast_PlanetGearOptions",
            parent: "PlanetGearOptions",
        ):
            self._parent = parent

        @property
        def planet_gear_options(
            self: "PlanetGearOptions._Cast_PlanetGearOptions",
        ) -> "PlanetGearOptions":
            return self._parent

        def __getattr__(self: "PlanetGearOptions._Cast_PlanetGearOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetGearOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def modify_planet_carrier_diameter(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ModifyPlanetCarrierDiameter

        if temp is None:
            return False

        return temp

    @modify_planet_carrier_diameter.setter
    @enforce_parameter_types
    def modify_planet_carrier_diameter(self: Self, value: "bool"):
        self.wrapped.ModifyPlanetCarrierDiameter = (
            bool(value) if value is not None else False
        )

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
    def cast_to(self: Self) -> "PlanetGearOptions._Cast_PlanetGearOptions":
        return self._Cast_PlanetGearOptions(self)
