"""TorqueConverterInverseK"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_INVERSE_K = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TorqueConverterInverseK"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterInverseK",)


Self = TypeVar("Self", bound="TorqueConverterInverseK")


class TorqueConverterInverseK(_1612.MeasurementBase):
    """TorqueConverterInverseK

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_INVERSE_K
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterInverseK")

    class _Cast_TorqueConverterInverseK:
        """Special nested class for casting TorqueConverterInverseK to subclasses."""

        def __init__(
            self: "TorqueConverterInverseK._Cast_TorqueConverterInverseK",
            parent: "TorqueConverterInverseK",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TorqueConverterInverseK._Cast_TorqueConverterInverseK",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def torque_converter_inverse_k(
            self: "TorqueConverterInverseK._Cast_TorqueConverterInverseK",
        ) -> "TorqueConverterInverseK":
            return self._parent

        def __getattr__(
            self: "TorqueConverterInverseK._Cast_TorqueConverterInverseK", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterInverseK.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TorqueConverterInverseK._Cast_TorqueConverterInverseK":
        return self._Cast_TorqueConverterInverseK(self)
