"""ToothFlankFractureStressStepAtAnalysisPointN1457"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_STRESS_STEP_AT_ANALYSIS_POINT_N1457 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureStressStepAtAnalysisPointN1457",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureStressStepAtAnalysisPointN1457",)


Self = TypeVar("Self", bound="ToothFlankFractureStressStepAtAnalysisPointN1457")


class ToothFlankFractureStressStepAtAnalysisPointN1457(_0.APIBase):
    """ToothFlankFractureStressStepAtAnalysisPointN1457

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_STRESS_STEP_AT_ANALYSIS_POINT_N1457
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ToothFlankFractureStressStepAtAnalysisPointN1457"
    )

    class _Cast_ToothFlankFractureStressStepAtAnalysisPointN1457:
        """Special nested class for casting ToothFlankFractureStressStepAtAnalysisPointN1457 to subclasses."""

        def __init__(
            self: "ToothFlankFractureStressStepAtAnalysisPointN1457._Cast_ToothFlankFractureStressStepAtAnalysisPointN1457",
            parent: "ToothFlankFractureStressStepAtAnalysisPointN1457",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_stress_step_at_analysis_point_n1457(
            self: "ToothFlankFractureStressStepAtAnalysisPointN1457._Cast_ToothFlankFractureStressStepAtAnalysisPointN1457",
        ) -> "ToothFlankFractureStressStepAtAnalysisPointN1457":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureStressStepAtAnalysisPointN1457._Cast_ToothFlankFractureStressStepAtAnalysisPointN1457",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "ToothFlankFractureStressStepAtAnalysisPointN1457.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_sensitivity_to_hydro_static_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueSensitivityToHydroStaticPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def first_hertzian_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstHertzianParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def global_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GlobalNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def global_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GlobalShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def global_transverse_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GlobalTransverseStress

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrostatic_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrostaticPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stress_due_to_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStressDueToFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stress_due_to_normal_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStressDueToNormalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def second_hertzian_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SecondHertzianParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def second_stress_invariant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SecondStressInvariant

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_stress_due_to_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearStressDueToFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_stress_due_to_normal_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearStressDueToNormalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def third_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThirdNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stress_due_to_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseStressDueToFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stress_due_to_normal_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseStressDueToNormalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_position_on_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPositionOnProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def relative_coordinates(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeCoordinates

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def stress(self: Self) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureStressStepAtAnalysisPointN1457._Cast_ToothFlankFractureStressStepAtAnalysisPointN1457":
        return self._Cast_ToothFlankFractureStressStepAtAnalysisPointN1457(self)
