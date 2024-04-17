"""Index"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEX = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Index"
)


__docformat__ = "restructuredtext en"
__all__ = ("Index",)


Self = TypeVar("Self", bound="Index")


class Index(_1612.MeasurementBase):
    """Index

    This is a mastapy class.
    """

    TYPE = _INDEX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Index")

    class _Cast_Index:
        """Special nested class for casting Index to subclasses."""

        def __init__(self: "Index._Cast_Index", parent: "Index"):
            self._parent = parent

        @property
        def measurement_base(self: "Index._Cast_Index") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def index(self: "Index._Cast_Index") -> "Index":
            return self._parent

        def __getattr__(self: "Index._Cast_Index", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Index.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Index._Cast_Index":
        return self._Cast_Index(self)
