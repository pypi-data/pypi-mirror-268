"""TorquePerCurrent"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_CURRENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TorquePerCurrent"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorquePerCurrent",)


Self = TypeVar("Self", bound="TorquePerCurrent")


class TorquePerCurrent(_1612.MeasurementBase):
    """TorquePerCurrent

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_CURRENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorquePerCurrent")

    class _Cast_TorquePerCurrent:
        """Special nested class for casting TorquePerCurrent to subclasses."""

        def __init__(
            self: "TorquePerCurrent._Cast_TorquePerCurrent", parent: "TorquePerCurrent"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TorquePerCurrent._Cast_TorquePerCurrent",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def torque_per_current(
            self: "TorquePerCurrent._Cast_TorquePerCurrent",
        ) -> "TorquePerCurrent":
            return self._parent

        def __getattr__(self: "TorquePerCurrent._Cast_TorquePerCurrent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorquePerCurrent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TorquePerCurrent._Cast_TorquePerCurrent":
        return self._Cast_TorquePerCurrent(self)
