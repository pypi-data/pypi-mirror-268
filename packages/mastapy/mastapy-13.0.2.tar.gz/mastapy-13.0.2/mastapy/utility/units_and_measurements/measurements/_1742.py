"""VoltagePerAngularVelocity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VOLTAGE_PER_ANGULAR_VELOCITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "VoltagePerAngularVelocity",
)


__docformat__ = "restructuredtext en"
__all__ = ("VoltagePerAngularVelocity",)


Self = TypeVar("Self", bound="VoltagePerAngularVelocity")


class VoltagePerAngularVelocity(_1612.MeasurementBase):
    """VoltagePerAngularVelocity

    This is a mastapy class.
    """

    TYPE = _VOLTAGE_PER_ANGULAR_VELOCITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VoltagePerAngularVelocity")

    class _Cast_VoltagePerAngularVelocity:
        """Special nested class for casting VoltagePerAngularVelocity to subclasses."""

        def __init__(
            self: "VoltagePerAngularVelocity._Cast_VoltagePerAngularVelocity",
            parent: "VoltagePerAngularVelocity",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "VoltagePerAngularVelocity._Cast_VoltagePerAngularVelocity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def voltage_per_angular_velocity(
            self: "VoltagePerAngularVelocity._Cast_VoltagePerAngularVelocity",
        ) -> "VoltagePerAngularVelocity":
            return self._parent

        def __getattr__(
            self: "VoltagePerAngularVelocity._Cast_VoltagePerAngularVelocity", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VoltagePerAngularVelocity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "VoltagePerAngularVelocity._Cast_VoltagePerAngularVelocity":
        return self._Cast_VoltagePerAngularVelocity(self)
