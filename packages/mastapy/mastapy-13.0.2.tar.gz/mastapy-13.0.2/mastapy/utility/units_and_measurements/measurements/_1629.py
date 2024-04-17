"""Area"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AREA = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Area"
)


__docformat__ = "restructuredtext en"
__all__ = ("Area",)


Self = TypeVar("Self", bound="Area")


class Area(_1612.MeasurementBase):
    """Area

    This is a mastapy class.
    """

    TYPE = _AREA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Area")

    class _Cast_Area:
        """Special nested class for casting Area to subclasses."""

        def __init__(self: "Area._Cast_Area", parent: "Area"):
            self._parent = parent

        @property
        def measurement_base(self: "Area._Cast_Area") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def area(self: "Area._Cast_Area") -> "Area":
            return self._parent

        def __getattr__(self: "Area._Cast_Area", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Area.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Area._Cast_Area":
        return self._Cast_Area(self)
