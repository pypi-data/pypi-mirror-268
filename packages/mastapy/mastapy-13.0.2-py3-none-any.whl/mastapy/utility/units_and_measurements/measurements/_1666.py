"""Integer"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTEGER = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Integer"
)


__docformat__ = "restructuredtext en"
__all__ = ("Integer",)


Self = TypeVar("Self", bound="Integer")


class Integer(_1612.MeasurementBase):
    """Integer

    This is a mastapy class.
    """

    TYPE = _INTEGER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Integer")

    class _Cast_Integer:
        """Special nested class for casting Integer to subclasses."""

        def __init__(self: "Integer._Cast_Integer", parent: "Integer"):
            self._parent = parent

        @property
        def measurement_base(self: "Integer._Cast_Integer") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def integer(self: "Integer._Cast_Integer") -> "Integer":
            return self._parent

        def __getattr__(self: "Integer._Cast_Integer", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Integer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Integer._Cast_Integer":
        return self._Cast_Integer(self)
