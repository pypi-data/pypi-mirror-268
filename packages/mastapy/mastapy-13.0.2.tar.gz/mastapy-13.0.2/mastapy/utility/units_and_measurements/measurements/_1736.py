"""TorquePerSquareRootOfPower"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_SQUARE_ROOT_OF_POWER = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "TorquePerSquareRootOfPower",
)


__docformat__ = "restructuredtext en"
__all__ = ("TorquePerSquareRootOfPower",)


Self = TypeVar("Self", bound="TorquePerSquareRootOfPower")


class TorquePerSquareRootOfPower(_1612.MeasurementBase):
    """TorquePerSquareRootOfPower

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_SQUARE_ROOT_OF_POWER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorquePerSquareRootOfPower")

    class _Cast_TorquePerSquareRootOfPower:
        """Special nested class for casting TorquePerSquareRootOfPower to subclasses."""

        def __init__(
            self: "TorquePerSquareRootOfPower._Cast_TorquePerSquareRootOfPower",
            parent: "TorquePerSquareRootOfPower",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TorquePerSquareRootOfPower._Cast_TorquePerSquareRootOfPower",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def torque_per_square_root_of_power(
            self: "TorquePerSquareRootOfPower._Cast_TorquePerSquareRootOfPower",
        ) -> "TorquePerSquareRootOfPower":
            return self._parent

        def __getattr__(
            self: "TorquePerSquareRootOfPower._Cast_TorquePerSquareRootOfPower",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorquePerSquareRootOfPower.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorquePerSquareRootOfPower._Cast_TorquePerSquareRootOfPower":
        return self._Cast_TorquePerSquareRootOfPower(self)
