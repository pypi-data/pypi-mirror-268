"""RescaledMeasurement"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESCALED_MEASUREMENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "RescaledMeasurement"
)


__docformat__ = "restructuredtext en"
__all__ = ("RescaledMeasurement",)


Self = TypeVar("Self", bound="RescaledMeasurement")


class RescaledMeasurement(_1612.MeasurementBase):
    """RescaledMeasurement

    This is a mastapy class.
    """

    TYPE = _RESCALED_MEASUREMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RescaledMeasurement")

    class _Cast_RescaledMeasurement:
        """Special nested class for casting RescaledMeasurement to subclasses."""

        def __init__(
            self: "RescaledMeasurement._Cast_RescaledMeasurement",
            parent: "RescaledMeasurement",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "RescaledMeasurement._Cast_RescaledMeasurement",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def rescaled_measurement(
            self: "RescaledMeasurement._Cast_RescaledMeasurement",
        ) -> "RescaledMeasurement":
            return self._parent

        def __getattr__(
            self: "RescaledMeasurement._Cast_RescaledMeasurement", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RescaledMeasurement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RescaledMeasurement._Cast_RescaledMeasurement":
        return self._Cast_RescaledMeasurement(self)
