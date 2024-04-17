"""PlanetCarrierWindup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_WINDUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "PlanetCarrierWindup",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2855,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierWindup",)


Self = TypeVar("Self", bound="PlanetCarrierWindup")


class PlanetCarrierWindup(_0.APIBase):
    """PlanetCarrierWindup

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_WINDUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierWindup")

    class _Cast_PlanetCarrierWindup:
        """Special nested class for casting PlanetCarrierWindup to subclasses."""

        def __init__(
            self: "PlanetCarrierWindup._Cast_PlanetCarrierWindup",
            parent: "PlanetCarrierWindup",
        ):
            self._parent = parent

        @property
        def planet_carrier_windup(
            self: "PlanetCarrierWindup._Cast_PlanetCarrierWindup",
        ) -> "PlanetCarrierWindup":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierWindup._Cast_PlanetCarrierWindup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierWindup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_axial_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageAxialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def average_radial_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageRadialTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def average_tangential_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageTangentialTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def average_torsional_wind_up(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageTorsionalWindUp

        if temp is None:
            return 0.0

        return temp

    @property
    def other_planet_carrier(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OtherPlanetCarrier

        if temp is None:
            return ""

        return temp

    @property
    def other_socket(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OtherSocket

        if temp is None:
            return ""

        return temp

    @property
    def reference_socket(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceSocket

        if temp is None:
            return ""

        return temp

    @property
    def pin_wind_ups(self: Self) -> "List[_2855.PlanetPinWindup]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.PlanetPinWindup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinWindUps

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PlanetCarrierWindup._Cast_PlanetCarrierWindup":
        return self._Cast_PlanetCarrierWindup(self)
