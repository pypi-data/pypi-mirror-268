"""CurrentDensity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CURRENT_DENSITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "CurrentDensity"
)


__docformat__ = "restructuredtext en"
__all__ = ("CurrentDensity",)


Self = TypeVar("Self", bound="CurrentDensity")


class CurrentDensity(_1612.MeasurementBase):
    """CurrentDensity

    This is a mastapy class.
    """

    TYPE = _CURRENT_DENSITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CurrentDensity")

    class _Cast_CurrentDensity:
        """Special nested class for casting CurrentDensity to subclasses."""

        def __init__(
            self: "CurrentDensity._Cast_CurrentDensity", parent: "CurrentDensity"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "CurrentDensity._Cast_CurrentDensity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def current_density(
            self: "CurrentDensity._Cast_CurrentDensity",
        ) -> "CurrentDensity":
            return self._parent

        def __getattr__(self: "CurrentDensity._Cast_CurrentDensity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CurrentDensity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CurrentDensity._Cast_CurrentDensity":
        return self._Cast_CurrentDensity(self)
