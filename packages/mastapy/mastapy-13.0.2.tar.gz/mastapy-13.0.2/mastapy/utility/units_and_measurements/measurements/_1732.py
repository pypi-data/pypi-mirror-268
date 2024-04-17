"""Torque"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Torque"
)


__docformat__ = "restructuredtext en"
__all__ = ("Torque",)


Self = TypeVar("Self", bound="Torque")


class Torque(_1612.MeasurementBase):
    """Torque

    This is a mastapy class.
    """

    TYPE = _TORQUE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Torque")

    class _Cast_Torque:
        """Special nested class for casting Torque to subclasses."""

        def __init__(self: "Torque._Cast_Torque", parent: "Torque"):
            self._parent = parent

        @property
        def measurement_base(self: "Torque._Cast_Torque") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def torque(self: "Torque._Cast_Torque") -> "Torque":
            return self._parent

        def __getattr__(self: "Torque._Cast_Torque", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Torque.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Torque._Cast_Torque":
        return self._Cast_Torque(self)
