"""OuterRingFittingThermalResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.fitting import _2120
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_RING_FITTING_THERMAL_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.Fitting",
    "OuterRingFittingThermalResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("OuterRingFittingThermalResults",)


Self = TypeVar("Self", bound="OuterRingFittingThermalResults")


class OuterRingFittingThermalResults(_2120.RingFittingThermalResults):
    """OuterRingFittingThermalResults

    This is a mastapy class.
    """

    TYPE = _OUTER_RING_FITTING_THERMAL_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterRingFittingThermalResults")

    class _Cast_OuterRingFittingThermalResults:
        """Special nested class for casting OuterRingFittingThermalResults to subclasses."""

        def __init__(
            self: "OuterRingFittingThermalResults._Cast_OuterRingFittingThermalResults",
            parent: "OuterRingFittingThermalResults",
        ):
            self._parent = parent

        @property
        def ring_fitting_thermal_results(
            self: "OuterRingFittingThermalResults._Cast_OuterRingFittingThermalResults",
        ) -> "_2120.RingFittingThermalResults":
            return self._parent._cast(_2120.RingFittingThermalResults)

        @property
        def outer_ring_fitting_thermal_results(
            self: "OuterRingFittingThermalResults._Cast_OuterRingFittingThermalResults",
        ) -> "OuterRingFittingThermalResults":
            return self._parent

        def __getattr__(
            self: "OuterRingFittingThermalResults._Cast_OuterRingFittingThermalResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterRingFittingThermalResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "OuterRingFittingThermalResults._Cast_OuterRingFittingThermalResults":
        return self._Cast_OuterRingFittingThermalResults(self)
