"""DamageRate"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DAMAGE_RATE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "DamageRate"
)


__docformat__ = "restructuredtext en"
__all__ = ("DamageRate",)


Self = TypeVar("Self", bound="DamageRate")


class DamageRate(_1612.MeasurementBase):
    """DamageRate

    This is a mastapy class.
    """

    TYPE = _DAMAGE_RATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DamageRate")

    class _Cast_DamageRate:
        """Special nested class for casting DamageRate to subclasses."""

        def __init__(self: "DamageRate._Cast_DamageRate", parent: "DamageRate"):
            self._parent = parent

        @property
        def measurement_base(
            self: "DamageRate._Cast_DamageRate",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def damage_rate(self: "DamageRate._Cast_DamageRate") -> "DamageRate":
            return self._parent

        def __getattr__(self: "DamageRate._Cast_DamageRate", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DamageRate.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DamageRate._Cast_DamageRate":
        return self._Cast_DamageRate(self)
