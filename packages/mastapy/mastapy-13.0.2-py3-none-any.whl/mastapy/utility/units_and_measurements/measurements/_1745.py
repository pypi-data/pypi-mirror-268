"""Yank"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_YANK = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Yank"
)


__docformat__ = "restructuredtext en"
__all__ = ("Yank",)


Self = TypeVar("Self", bound="Yank")


class Yank(_1612.MeasurementBase):
    """Yank

    This is a mastapy class.
    """

    TYPE = _YANK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Yank")

    class _Cast_Yank:
        """Special nested class for casting Yank to subclasses."""

        def __init__(self: "Yank._Cast_Yank", parent: "Yank"):
            self._parent = parent

        @property
        def measurement_base(self: "Yank._Cast_Yank") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def yank(self: "Yank._Cast_Yank") -> "Yank":
            return self._parent

        def __getattr__(self: "Yank._Cast_Yank", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Yank.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Yank._Cast_Yank":
        return self._Cast_Yank(self)
