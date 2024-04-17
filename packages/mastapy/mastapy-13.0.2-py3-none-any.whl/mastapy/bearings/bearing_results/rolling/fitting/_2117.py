"""InnerRingFittingThermalResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.fitting import _2120
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_RING_FITTING_THERMAL_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.Fitting",
    "InnerRingFittingThermalResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("InnerRingFittingThermalResults",)


Self = TypeVar("Self", bound="InnerRingFittingThermalResults")


class InnerRingFittingThermalResults(_2120.RingFittingThermalResults):
    """InnerRingFittingThermalResults

    This is a mastapy class.
    """

    TYPE = _INNER_RING_FITTING_THERMAL_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerRingFittingThermalResults")

    class _Cast_InnerRingFittingThermalResults:
        """Special nested class for casting InnerRingFittingThermalResults to subclasses."""

        def __init__(
            self: "InnerRingFittingThermalResults._Cast_InnerRingFittingThermalResults",
            parent: "InnerRingFittingThermalResults",
        ):
            self._parent = parent

        @property
        def ring_fitting_thermal_results(
            self: "InnerRingFittingThermalResults._Cast_InnerRingFittingThermalResults",
        ) -> "_2120.RingFittingThermalResults":
            return self._parent._cast(_2120.RingFittingThermalResults)

        @property
        def inner_ring_fitting_thermal_results(
            self: "InnerRingFittingThermalResults._Cast_InnerRingFittingThermalResults",
        ) -> "InnerRingFittingThermalResults":
            return self._parent

        def __getattr__(
            self: "InnerRingFittingThermalResults._Cast_InnerRingFittingThermalResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerRingFittingThermalResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "InnerRingFittingThermalResults._Cast_InnerRingFittingThermalResults":
        return self._Cast_InnerRingFittingThermalResults(self)
