"""Text"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEXT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Text"
)


__docformat__ = "restructuredtext en"
__all__ = ("Text",)


Self = TypeVar("Self", bound="Text")


class Text(_1612.MeasurementBase):
    """Text

    This is a mastapy class.
    """

    TYPE = _TEXT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Text")

    class _Cast_Text:
        """Special nested class for casting Text to subclasses."""

        def __init__(self: "Text._Cast_Text", parent: "Text"):
            self._parent = parent

        @property
        def measurement_base(self: "Text._Cast_Text") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def text(self: "Text._Cast_Text") -> "Text":
            return self._parent

        def __getattr__(self: "Text._Cast_Text", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Text.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Text._Cast_Text":
        return self._Cast_Text(self)
