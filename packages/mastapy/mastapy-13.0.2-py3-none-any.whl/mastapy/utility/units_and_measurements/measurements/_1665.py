"""Inductance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDUCTANCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Inductance"
)


__docformat__ = "restructuredtext en"
__all__ = ("Inductance",)


Self = TypeVar("Self", bound="Inductance")


class Inductance(_1612.MeasurementBase):
    """Inductance

    This is a mastapy class.
    """

    TYPE = _INDUCTANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Inductance")

    class _Cast_Inductance:
        """Special nested class for casting Inductance to subclasses."""

        def __init__(self: "Inductance._Cast_Inductance", parent: "Inductance"):
            self._parent = parent

        @property
        def measurement_base(
            self: "Inductance._Cast_Inductance",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def inductance(self: "Inductance._Cast_Inductance") -> "Inductance":
            return self._parent

        def __getattr__(self: "Inductance._Cast_Inductance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Inductance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Inductance._Cast_Inductance":
        return self._Cast_Inductance(self)
