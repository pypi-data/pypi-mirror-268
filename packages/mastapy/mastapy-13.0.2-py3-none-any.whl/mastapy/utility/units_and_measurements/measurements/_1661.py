"""HeatTransferCoefficientForPlasticGearTooth"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_TRANSFER_COEFFICIENT_FOR_PLASTIC_GEAR_TOOTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "HeatTransferCoefficientForPlasticGearTooth",
)


__docformat__ = "restructuredtext en"
__all__ = ("HeatTransferCoefficientForPlasticGearTooth",)


Self = TypeVar("Self", bound="HeatTransferCoefficientForPlasticGearTooth")


class HeatTransferCoefficientForPlasticGearTooth(_1612.MeasurementBase):
    """HeatTransferCoefficientForPlasticGearTooth

    This is a mastapy class.
    """

    TYPE = _HEAT_TRANSFER_COEFFICIENT_FOR_PLASTIC_GEAR_TOOTH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HeatTransferCoefficientForPlasticGearTooth"
    )

    class _Cast_HeatTransferCoefficientForPlasticGearTooth:
        """Special nested class for casting HeatTransferCoefficientForPlasticGearTooth to subclasses."""

        def __init__(
            self: "HeatTransferCoefficientForPlasticGearTooth._Cast_HeatTransferCoefficientForPlasticGearTooth",
            parent: "HeatTransferCoefficientForPlasticGearTooth",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "HeatTransferCoefficientForPlasticGearTooth._Cast_HeatTransferCoefficientForPlasticGearTooth",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def heat_transfer_coefficient_for_plastic_gear_tooth(
            self: "HeatTransferCoefficientForPlasticGearTooth._Cast_HeatTransferCoefficientForPlasticGearTooth",
        ) -> "HeatTransferCoefficientForPlasticGearTooth":
            return self._parent

        def __getattr__(
            self: "HeatTransferCoefficientForPlasticGearTooth._Cast_HeatTransferCoefficientForPlasticGearTooth",
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
        self: Self, instance_to_wrap: "HeatTransferCoefficientForPlasticGearTooth.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HeatTransferCoefficientForPlasticGearTooth._Cast_HeatTransferCoefficientForPlasticGearTooth":
        return self._Cast_HeatTransferCoefficientForPlasticGearTooth(self)
