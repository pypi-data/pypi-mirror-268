"""VirtualSimulationCalculator"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "VirtualSimulationCalculator",
)


__docformat__ = "restructuredtext en"
__all__ = ("VirtualSimulationCalculator",)


Self = TypeVar("Self", bound="VirtualSimulationCalculator")


class VirtualSimulationCalculator(_734.CutterSimulationCalc):
    """VirtualSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_SIMULATION_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualSimulationCalculator")

    class _Cast_VirtualSimulationCalculator:
        """Special nested class for casting VirtualSimulationCalculator to subclasses."""

        def __init__(
            self: "VirtualSimulationCalculator._Cast_VirtualSimulationCalculator",
            parent: "VirtualSimulationCalculator",
        ):
            self._parent = parent

        @property
        def cutter_simulation_calc(
            self: "VirtualSimulationCalculator._Cast_VirtualSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def virtual_simulation_calculator(
            self: "VirtualSimulationCalculator._Cast_VirtualSimulationCalculator",
        ) -> "VirtualSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "VirtualSimulationCalculator._Cast_VirtualSimulationCalculator",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualSimulationCalculator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_moment_arm_for_iso_rating_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingMomentArmForISORatingWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def form_factor_for_iso_rating_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormFactorForISORatingWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def notch_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NotchDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_of_critical_point_for_iso_rating_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusOfCriticalPointForISORatingWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_iso(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusISO

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def root_fillet_radius_for_agma_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForAGMARating

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_for_iso_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForISORating

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_for_iso_rating_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForISORatingWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_form_factor_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFormFactorWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor_for_iso_rating_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactorForISORatingWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chord_for_iso_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordForISORating

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chord_for_iso_rating_worst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordForISORatingWorst

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualSimulationCalculator._Cast_VirtualSimulationCalculator":
        return self._Cast_VirtualSimulationCalculator(self)
