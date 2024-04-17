"""PressureVelocityProduct"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_VELOCITY_PRODUCT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PressureVelocityProduct"
)


__docformat__ = "restructuredtext en"
__all__ = ("PressureVelocityProduct",)


Self = TypeVar("Self", bound="PressureVelocityProduct")


class PressureVelocityProduct(_1612.MeasurementBase):
    """PressureVelocityProduct

    This is a mastapy class.
    """

    TYPE = _PRESSURE_VELOCITY_PRODUCT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PressureVelocityProduct")

    class _Cast_PressureVelocityProduct:
        """Special nested class for casting PressureVelocityProduct to subclasses."""

        def __init__(
            self: "PressureVelocityProduct._Cast_PressureVelocityProduct",
            parent: "PressureVelocityProduct",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PressureVelocityProduct._Cast_PressureVelocityProduct",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def pressure_velocity_product(
            self: "PressureVelocityProduct._Cast_PressureVelocityProduct",
        ) -> "PressureVelocityProduct":
            return self._parent

        def __getattr__(
            self: "PressureVelocityProduct._Cast_PressureVelocityProduct", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PressureVelocityProduct.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PressureVelocityProduct._Cast_PressureVelocityProduct":
        return self._Cast_PressureVelocityProduct(self)
