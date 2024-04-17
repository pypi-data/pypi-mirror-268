"""Stress"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Stress"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements.measurements import _1706


__docformat__ = "restructuredtext en"
__all__ = ("Stress",)


Self = TypeVar("Self", bound="Stress")


class Stress(_1612.MeasurementBase):
    """Stress

    This is a mastapy class.
    """

    TYPE = _STRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Stress")

    class _Cast_Stress:
        """Special nested class for casting Stress to subclasses."""

        def __init__(self: "Stress._Cast_Stress", parent: "Stress"):
            self._parent = parent

        @property
        def measurement_base(self: "Stress._Cast_Stress") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def pressure(self: "Stress._Cast_Stress") -> "_1706.Pressure":
            from mastapy.utility.units_and_measurements.measurements import _1706

            return self._parent._cast(_1706.Pressure)

        @property
        def stress(self: "Stress._Cast_Stress") -> "Stress":
            return self._parent

        def __getattr__(self: "Stress._Cast_Stress", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Stress.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Stress._Cast_Stress":
        return self._Cast_Stress(self)
