"""WearCoefficient"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WEAR_COEFFICIENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "WearCoefficient"
)


__docformat__ = "restructuredtext en"
__all__ = ("WearCoefficient",)


Self = TypeVar("Self", bound="WearCoefficient")


class WearCoefficient(_1612.MeasurementBase):
    """WearCoefficient

    This is a mastapy class.
    """

    TYPE = _WEAR_COEFFICIENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WearCoefficient")

    class _Cast_WearCoefficient:
        """Special nested class for casting WearCoefficient to subclasses."""

        def __init__(
            self: "WearCoefficient._Cast_WearCoefficient", parent: "WearCoefficient"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "WearCoefficient._Cast_WearCoefficient",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def wear_coefficient(
            self: "WearCoefficient._Cast_WearCoefficient",
        ) -> "WearCoefficient":
            return self._parent

        def __getattr__(self: "WearCoefficient._Cast_WearCoefficient", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WearCoefficient.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "WearCoefficient._Cast_WearCoefficient":
        return self._Cast_WearCoefficient(self)
