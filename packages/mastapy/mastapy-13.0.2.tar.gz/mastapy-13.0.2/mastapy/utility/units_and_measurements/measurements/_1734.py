"""TorqueConverterK"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_K = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TorqueConverterK"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterK",)


Self = TypeVar("Self", bound="TorqueConverterK")


class TorqueConverterK(_1612.MeasurementBase):
    """TorqueConverterK

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_K
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterK")

    class _Cast_TorqueConverterK:
        """Special nested class for casting TorqueConverterK to subclasses."""

        def __init__(
            self: "TorqueConverterK._Cast_TorqueConverterK", parent: "TorqueConverterK"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TorqueConverterK._Cast_TorqueConverterK",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def torque_converter_k(
            self: "TorqueConverterK._Cast_TorqueConverterK",
        ) -> "TorqueConverterK":
            return self._parent

        def __getattr__(self: "TorqueConverterK._Cast_TorqueConverterK", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterK.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TorqueConverterK._Cast_TorqueConverterK":
        return self._Cast_TorqueConverterK(self)
