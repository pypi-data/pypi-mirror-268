"""NamedPlanetSideBandAmplitudeFactor"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_PLANET_SIDE_BAND_AMPLITUDE_FACTOR = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "NamedPlanetSideBandAmplitudeFactor"
)


__docformat__ = "restructuredtext en"
__all__ = ("NamedPlanetSideBandAmplitudeFactor",)


Self = TypeVar("Self", bound="NamedPlanetSideBandAmplitudeFactor")


class NamedPlanetSideBandAmplitudeFactor(_0.APIBase):
    """NamedPlanetSideBandAmplitudeFactor

    This is a mastapy class.
    """

    TYPE = _NAMED_PLANET_SIDE_BAND_AMPLITUDE_FACTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedPlanetSideBandAmplitudeFactor")

    class _Cast_NamedPlanetSideBandAmplitudeFactor:
        """Special nested class for casting NamedPlanetSideBandAmplitudeFactor to subclasses."""

        def __init__(
            self: "NamedPlanetSideBandAmplitudeFactor._Cast_NamedPlanetSideBandAmplitudeFactor",
            parent: "NamedPlanetSideBandAmplitudeFactor",
        ):
            self._parent = parent

        @property
        def named_planet_side_band_amplitude_factor(
            self: "NamedPlanetSideBandAmplitudeFactor._Cast_NamedPlanetSideBandAmplitudeFactor",
        ) -> "NamedPlanetSideBandAmplitudeFactor":
            return self._parent

        def __getattr__(
            self: "NamedPlanetSideBandAmplitudeFactor._Cast_NamedPlanetSideBandAmplitudeFactor",
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
        self: Self, instance_to_wrap: "NamedPlanetSideBandAmplitudeFactor.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_sidebands_amplitude_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetarySidebandsAmplitudeFactor

        if temp is None:
            return 0.0

        return temp

    @planetary_sidebands_amplitude_factor.setter
    @enforce_parameter_types
    def planetary_sidebands_amplitude_factor(self: Self, value: "float"):
        self.wrapped.PlanetarySidebandsAmplitudeFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "NamedPlanetSideBandAmplitudeFactor._Cast_NamedPlanetSideBandAmplitudeFactor":
        return self._Cast_NamedPlanetSideBandAmplitudeFactor(self)
