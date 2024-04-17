"""ToothFlankFractureAnalysisPoint"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_POINT = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ToothFlankFractureAnalysisPoint"
)


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisPoint",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisPoint")


class ToothFlankFractureAnalysisPoint(_0.APIBase):
    """ToothFlankFractureAnalysisPoint

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothFlankFractureAnalysisPoint")

    class _Cast_ToothFlankFractureAnalysisPoint:
        """Special nested class for casting ToothFlankFractureAnalysisPoint to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisPoint._Cast_ToothFlankFractureAnalysisPoint",
            parent: "ToothFlankFractureAnalysisPoint",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_point(
            self: "ToothFlankFractureAnalysisPoint._Cast_ToothFlankFractureAnalysisPoint",
        ) -> "ToothFlankFractureAnalysisPoint":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisPoint._Cast_ToothFlankFractureAnalysisPoint",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToothFlankFractureAnalysisPoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def case_hardening_depth_influence_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CaseHardeningDepthInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def correction_factor_for_practice_oriented_calculation_approach_first(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CorrectionFactorForPracticeOrientedCalculationApproachFirst

        if temp is None:
            return 0.0

        return temp

    @property
    def correction_factor_for_practice_oriented_calculation_approach_second(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CorrectionFactorForPracticeOrientedCalculationApproachSecond

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_from_surface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthFromSurface

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_conversion_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessConversionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_pressure_and_residual_stress_influence_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianPressureAndResidualStressInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def influence_of_the_residual_stresses_on_the_local_equivalent_stress(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InfluenceOfTheResidualStressesOnTheLocalEquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def local_equivalent_stress_without_consideration_of_residual_stresses(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalEquivalentStressWithoutConsiderationOfResidualStresses

        if temp is None:
            return 0.0

        return temp

    @property
    def local_material_exposure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalMaterialExposure

        if temp is None:
            return 0.0

        return temp

    @property
    def local_material_hardness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalMaterialHardness

        if temp is None:
            return 0.0

        return temp

    @property
    def local_material_shear_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalMaterialShearStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def local_occurring_equivalent_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalOccurringEquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def local_tensile_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalTensileStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def material_exposure_calibration_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialExposureCalibrationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def material_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_depth_from_surface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedDepthFromSurface

        if temp is None:
            return 0.0

        return temp

    @property
    def quasi_stationary_residual_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QuasiStationaryResidualStress

        if temp is None:
            return 0.0

        return temp

    @property
    def residual_stress_sensitivity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResidualStressSensitivity

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_component_of_compressive_residual_stresses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialComponentOfCompressiveResidualStresses

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisPoint._Cast_ToothFlankFractureAnalysisPoint":
        return self._Cast_ToothFlankFractureAnalysisPoint(self)
