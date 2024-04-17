"""Volume"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VOLUME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Volume"
)


__docformat__ = "restructuredtext en"
__all__ = ("Volume",)


Self = TypeVar("Self", bound="Volume")


class Volume(_1612.MeasurementBase):
    """Volume

    This is a mastapy class.
    """

    TYPE = _VOLUME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Volume")

    class _Cast_Volume:
        """Special nested class for casting Volume to subclasses."""

        def __init__(self: "Volume._Cast_Volume", parent: "Volume"):
            self._parent = parent

        @property
        def measurement_base(self: "Volume._Cast_Volume") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def volume(self: "Volume._Cast_Volume") -> "Volume":
            return self._parent

        def __getattr__(self: "Volume._Cast_Volume", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Volume.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Volume._Cast_Volume":
        return self._Cast_Volume(self)
