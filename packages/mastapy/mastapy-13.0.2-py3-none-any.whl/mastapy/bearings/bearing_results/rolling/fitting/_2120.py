"""RingFittingThermalResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_FITTING_THERMAL_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.Fitting", "RingFittingThermalResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.fitting import _2118, _2117, _2119


__docformat__ = "restructuredtext en"
__all__ = ("RingFittingThermalResults",)


Self = TypeVar("Self", bound="RingFittingThermalResults")


class RingFittingThermalResults(_0.APIBase):
    """RingFittingThermalResults

    This is a mastapy class.
    """

    TYPE = _RING_FITTING_THERMAL_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingFittingThermalResults")

    class _Cast_RingFittingThermalResults:
        """Special nested class for casting RingFittingThermalResults to subclasses."""

        def __init__(
            self: "RingFittingThermalResults._Cast_RingFittingThermalResults",
            parent: "RingFittingThermalResults",
        ):
            self._parent = parent

        @property
        def inner_ring_fitting_thermal_results(
            self: "RingFittingThermalResults._Cast_RingFittingThermalResults",
        ) -> "_2117.InnerRingFittingThermalResults":
            from mastapy.bearings.bearing_results.rolling.fitting import _2117

            return self._parent._cast(_2117.InnerRingFittingThermalResults)

        @property
        def outer_ring_fitting_thermal_results(
            self: "RingFittingThermalResults._Cast_RingFittingThermalResults",
        ) -> "_2119.OuterRingFittingThermalResults":
            from mastapy.bearings.bearing_results.rolling.fitting import _2119

            return self._parent._cast(_2119.OuterRingFittingThermalResults)

        @property
        def ring_fitting_thermal_results(
            self: "RingFittingThermalResults._Cast_RingFittingThermalResults",
        ) -> "RingFittingThermalResults":
            return self._parent

        def __getattr__(
            self: "RingFittingThermalResults._Cast_RingFittingThermalResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingFittingThermalResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def change_in_diameter_due_to_interference_and_centrifugal_effects(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInDiameterDueToInterferenceAndCentrifugalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def interfacial_clearance_included_in_analysis(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterfacialClearanceIncludedInAnalysis

        if temp is None:
            return False

        return temp

    @property
    def interfacial_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterfacialNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_hoop_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumHoopStress

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def interference_values(self: Self) -> "List[_2118.InterferenceComponents]":
        """List[mastapy.bearings.bearing_results.rolling.fitting.InterferenceComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterferenceValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingFittingThermalResults._Cast_RingFittingThermalResults":
        return self._Cast_RingFittingThermalResults(self)
