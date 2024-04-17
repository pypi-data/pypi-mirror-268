"""GearSetOptimiser"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_INT_32 = python_net_import("System", "Int32")
_BOOLEAN = python_net_import("System", "Boolean")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_GEAR_SET_OPTIMISER = python_net_import("SMT.MastaAPI.Gears", "GearSetOptimiser")

if TYPE_CHECKING:
    from mastapy import _7567
    from mastapy.gears import _334
    from mastapy.gears.gear_designs.cylindrical import _1034


__docformat__ = "restructuredtext en"
__all__ = ("GearSetOptimiser",)


Self = TypeVar("Self", bound="GearSetOptimiser")


class GearSetOptimiser(_0.APIBase):
    """GearSetOptimiser

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetOptimiser")

    class _Cast_GearSetOptimiser:
        """Special nested class for casting GearSetOptimiser to subclasses."""

        def __init__(
            self: "GearSetOptimiser._Cast_GearSetOptimiser", parent: "GearSetOptimiser"
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_macro_geometry_optimiser(
            self: "GearSetOptimiser._Cast_GearSetOptimiser",
        ) -> "_1034.CylindricalGearSetMacroGeometryOptimiser":
            from mastapy.gears.gear_designs.cylindrical import _1034

            return self._parent._cast(_1034.CylindricalGearSetMacroGeometryOptimiser)

        @property
        def gear_set_optimiser(
            self: "GearSetOptimiser._Cast_GearSetOptimiser",
        ) -> "GearSetOptimiser":
            return self._parent

        def __getattr__(self: "GearSetOptimiser._Cast_GearSetOptimiser", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetOptimiser.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_ratio_rating_for_nvh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def crack_initiation_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrackInitiationSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_fracture_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueFractureSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermanentDeformationSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_flash_temperature_method_for_worst_gear(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorFlashTemperatureMethodForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_integral_method_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorIntegralMethodForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def static_bending_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticBendingSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def static_contact_safety_factor_for_worst_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticContactSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_ratio_rating_for_nvh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    def dispose(self: Self):
        """Method does not return."""
        self.wrapped.Dispose()

    @enforce_parameter_types
    def perform_strength_optimisation_with_progress(
        self: Self,
        number_of_results: "int",
        progress: "_7567.TaskProgress",
        use_current_design_as_starting_point: "bool" = False,
    ) -> "_334.GearSetOptimisationResults":
        """mastapy.gears.GearSetOptimisationResults

        Args:
            number_of_results (int)
            progress (mastapy.TaskProgress)
            use_current_design_as_starting_point (bool, optional)
        """
        number_of_results = int(number_of_results)
        use_current_design_as_starting_point = bool(
            use_current_design_as_starting_point
        )
        method_result = self.wrapped.PerformStrengthOptimisation.Overloads[
            _INT_32, _TASK_PROGRESS, _BOOLEAN
        ](
            number_of_results if number_of_results else 0,
            progress.wrapped if progress else None,
            (
                use_current_design_as_starting_point
                if use_current_design_as_starting_point
                else False
            ),
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def perform_strength_optimisation(
        self: Self,
        number_of_results: "int",
        use_current_design_as_starting_point: "bool" = False,
    ) -> "_334.GearSetOptimisationResults":
        """mastapy.gears.GearSetOptimisationResults

        Args:
            number_of_results (int)
            use_current_design_as_starting_point (bool, optional)
        """
        number_of_results = int(number_of_results)
        use_current_design_as_starting_point = bool(
            use_current_design_as_starting_point
        )
        method_result = self.wrapped.PerformStrengthOptimisation.Overloads[
            _INT_32, _BOOLEAN
        ](
            number_of_results if number_of_results else 0,
            (
                use_current_design_as_starting_point
                if use_current_design_as_starting_point
                else False
            ),
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def __enter__(self: Self):
        return self

    def __exit__(self: Self, exception_type: Any, exception_value: Any, traceback: Any):
        self.dispose()

    @property
    def cast_to(self: Self) -> "GearSetOptimiser._Cast_GearSetOptimiser":
        return self._Cast_GearSetOptimiser(self)
