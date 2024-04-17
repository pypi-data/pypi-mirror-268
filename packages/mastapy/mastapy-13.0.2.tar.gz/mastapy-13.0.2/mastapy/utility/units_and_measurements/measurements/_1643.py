"""Energy"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Energy"
)


__docformat__ = "restructuredtext en"
__all__ = ("Energy",)


Self = TypeVar("Self", bound="Energy")


class Energy(_1612.MeasurementBase):
    """Energy

    This is a mastapy class.
    """

    TYPE = _ENERGY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Energy")

    class _Cast_Energy:
        """Special nested class for casting Energy to subclasses."""

        def __init__(self: "Energy._Cast_Energy", parent: "Energy"):
            self._parent = parent

        @property
        def measurement_base(self: "Energy._Cast_Energy") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def energy(self: "Energy._Cast_Energy") -> "Energy":
            return self._parent

        def __getattr__(self: "Energy._Cast_Energy", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Energy.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Energy._Cast_Energy":
        return self._Cast_Energy(self)
