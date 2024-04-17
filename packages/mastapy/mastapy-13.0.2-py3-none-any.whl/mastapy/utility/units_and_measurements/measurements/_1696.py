"""Percentage"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.units_and_measurements.measurements import _1653
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERCENTAGE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Percentage"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612


__docformat__ = "restructuredtext en"
__all__ = ("Percentage",)


Self = TypeVar("Self", bound="Percentage")


class Percentage(_1653.FractionMeasurementBase):
    """Percentage

    This is a mastapy class.
    """

    TYPE = _PERCENTAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Percentage")

    class _Cast_Percentage:
        """Special nested class for casting Percentage to subclasses."""

        def __init__(self: "Percentage._Cast_Percentage", parent: "Percentage"):
            self._parent = parent

        @property
        def fraction_measurement_base(
            self: "Percentage._Cast_Percentage",
        ) -> "_1653.FractionMeasurementBase":
            return self._parent._cast(_1653.FractionMeasurementBase)

        @property
        def measurement_base(
            self: "Percentage._Cast_Percentage",
        ) -> "_1612.MeasurementBase":
            from mastapy.utility.units_and_measurements import _1612

            return self._parent._cast(_1612.MeasurementBase)

        @property
        def percentage(self: "Percentage._Cast_Percentage") -> "Percentage":
            return self._parent

        def __getattr__(self: "Percentage._Cast_Percentage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Percentage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Percentage._Cast_Percentage":
        return self._Cast_Percentage(self)
