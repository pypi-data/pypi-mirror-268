"""SpecificHeat"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFIC_HEAT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "SpecificHeat"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpecificHeat",)


Self = TypeVar("Self", bound="SpecificHeat")


class SpecificHeat(_1612.MeasurementBase):
    """SpecificHeat

    This is a mastapy class.
    """

    TYPE = _SPECIFIC_HEAT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecificHeat")

    class _Cast_SpecificHeat:
        """Special nested class for casting SpecificHeat to subclasses."""

        def __init__(self: "SpecificHeat._Cast_SpecificHeat", parent: "SpecificHeat"):
            self._parent = parent

        @property
        def measurement_base(
            self: "SpecificHeat._Cast_SpecificHeat",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def specific_heat(self: "SpecificHeat._Cast_SpecificHeat") -> "SpecificHeat":
            return self._parent

        def __getattr__(self: "SpecificHeat._Cast_SpecificHeat", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecificHeat.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SpecificHeat._Cast_SpecificHeat":
        return self._Cast_SpecificHeat(self)
