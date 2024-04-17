"""PlanetCarrierSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_SETTINGS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrierSettings"
)

if TYPE_CHECKING:
    from mastapy.system_model import _2222
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierSettings",)


Self = TypeVar("Self", bound="PlanetCarrierSettings")


class PlanetCarrierSettings(_1601.PerMachineSettings):
    """PlanetCarrierSettings

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierSettings")

    class _Cast_PlanetCarrierSettings:
        """Special nested class for casting PlanetCarrierSettings to subclasses."""

        def __init__(
            self: "PlanetCarrierSettings._Cast_PlanetCarrierSettings",
            parent: "PlanetCarrierSettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "PlanetCarrierSettings._Cast_PlanetCarrierSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "PlanetCarrierSettings._Cast_PlanetCarrierSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def planet_carrier_settings(
            self: "PlanetCarrierSettings._Cast_PlanetCarrierSettings",
        ) -> "PlanetCarrierSettings":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierSettings._Cast_PlanetCarrierSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_pin_manufacturing_errors_coordinate_system(
        self: Self,
    ) -> "_2222.PlanetPinManufacturingErrorsCoordinateSystem":
        """mastapy.system_model.PlanetPinManufacturingErrorsCoordinateSystem"""
        temp = self.wrapped.PlanetPinManufacturingErrorsCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PlanetPinManufacturingErrorsCoordinateSystem",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2222", "PlanetPinManufacturingErrorsCoordinateSystem"
        )(value)

    @planet_pin_manufacturing_errors_coordinate_system.setter
    @enforce_parameter_types
    def planet_pin_manufacturing_errors_coordinate_system(
        self: Self, value: "_2222.PlanetPinManufacturingErrorsCoordinateSystem"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PlanetPinManufacturingErrorsCoordinateSystem",
        )
        self.wrapped.PlanetPinManufacturingErrorsCoordinateSystem = value

    @property
    def cast_to(self: Self) -> "PlanetCarrierSettings._Cast_PlanetCarrierSettings":
        return self._Cast_PlanetCarrierSettings(self)
