"""DataSize"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SIZE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "DataSize"
)


__docformat__ = "restructuredtext en"
__all__ = ("DataSize",)


Self = TypeVar("Self", bound="DataSize")


class DataSize(_1612.MeasurementBase):
    """DataSize

    This is a mastapy class.
    """

    TYPE = _DATA_SIZE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataSize")

    class _Cast_DataSize:
        """Special nested class for casting DataSize to subclasses."""

        def __init__(self: "DataSize._Cast_DataSize", parent: "DataSize"):
            self._parent = parent

        @property
        def measurement_base(
            self: "DataSize._Cast_DataSize",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def data_size(self: "DataSize._Cast_DataSize") -> "DataSize":
            return self._parent

        def __getattr__(self: "DataSize._Cast_DataSize", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataSize.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DataSize._Cast_DataSize":
        return self._Cast_DataSize(self)
