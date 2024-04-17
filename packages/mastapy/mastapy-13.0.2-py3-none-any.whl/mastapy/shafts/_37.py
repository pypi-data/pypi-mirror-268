"""ShaftSectionEndDamageResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SECTION_END_DAMAGE_RESULTS = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftSectionEndDamageResults"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _87
    from mastapy.shafts import _44, _16, _17, _29
    from mastapy.materials import _284


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSectionEndDamageResults",)


Self = TypeVar("Self", bound="ShaftSectionEndDamageResults")


class ShaftSectionEndDamageResults(_0.APIBase):
    """ShaftSectionEndDamageResults

    This is a mastapy class.
    """

    TYPE = _SHAFT_SECTION_END_DAMAGE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSectionEndDamageResults")

    class _Cast_ShaftSectionEndDamageResults:
        """Special nested class for casting ShaftSectionEndDamageResults to subclasses."""

        def __init__(
            self: "ShaftSectionEndDamageResults._Cast_ShaftSectionEndDamageResults",
            parent: "ShaftSectionEndDamageResults",
        ):
            self._parent = parent

        @property
        def shaft_section_end_damage_results(
            self: "ShaftSectionEndDamageResults._Cast_ShaftSectionEndDamageResults",
        ) -> "ShaftSectionEndDamageResults":
            return self._parent

        def __getattr__(
            self: "ShaftSectionEndDamageResults._Cast_ShaftSectionEndDamageResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSectionEndDamageResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def displacement_angular(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def displacement_axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementAxial

        if temp is None:
            return 0.0

        return temp

    @property
    def displacement_linear(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def displacement_radial_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementRadialMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def displacement_radial_tilt_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementRadialTiltMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def displacement_twist(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementTwist

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_alternating_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentAlternatingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_safety_factor_for_infinite_life(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueSafetyFactorForInfiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def force_angular(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def force_axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAxial

        if temp is None:
            return 0.0

        return temp

    @property
    def force_linear(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def force_radial_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceRadialMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def force_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_diameter_to_achieve_fatigue_safety_factor_requirement(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameterToAchieveFatigueSafetyFactorRequirement

        if temp is None:
            return 0.0

        return temp

    @outer_diameter_to_achieve_fatigue_safety_factor_requirement.setter
    @enforce_parameter_types
    def outer_diameter_to_achieve_fatigue_safety_factor_requirement(
        self: Self, value: "float"
    ):
        self.wrapped.OuterDiameterToAchieveFatigueSafetyFactorRequirement = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_radius_to_achieve_shaft_fatigue_safety_factor_requirement(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadiusToAchieveShaftFatigueSafetyFactorRequirement

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_for_infinite_life(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityForInfiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def section_end(self: Self) -> "_87.SectionEnd":
        """mastapy.nodal_analysis.SectionEnd

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectionEnd

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.NodalAnalysis.SectionEnd")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.nodal_analysis._87", "SectionEnd")(
            value
        )

    @property
    def shaft_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def total_number_of_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalNumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def din743201212_component_fatigue_limit_under_reversed_stress_sigma_zd_wk_sigma_bwk_tau_twk(
        self: Self,
    ) -> "_44.StressMeasurementShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.StressMeasurementShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DIN743201212ComponentFatigueLimitUnderReversedStressSigmaZdWKSigmaBWKTauTWK
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_component_yield_point_sigma_zd_fk_sigma_bfk_tau_tfk(
        self: Self,
    ) -> "_44.StressMeasurementShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.StressMeasurementShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212ComponentYieldPointSigmaZdFKSigmaBFKTauTFK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_influence_factor_for_mean_stress_sensitivity_psi_sigma_k_psi_tau_k(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DIN743201212InfluenceFactorForMeanStressSensitivityPsiSigmaKPsiTauK
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fkm_guideline_6th_edition_2012_cyclic_degree_of_utilization_for_finite_life(
        self: Self,
    ) -> "_17.ShaftAxialBendingXBendingYTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingXBendingYTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.FKMGuideline6thEdition2012CyclicDegreeOfUtilizationForFiniteLife
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fkm_guideline_6th_edition_2012_cyclic_degree_of_utilization_for_infinite_life(
        self: Self,
    ) -> "_17.ShaftAxialBendingXBendingYTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingXBendingYTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.FKMGuideline6thEdition2012CyclicDegreeOfUtilizationForInfiniteLife
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sn_curve(self: Self) -> "_284.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sn_curve_axial(self: Self) -> "_284.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurveAxial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sn_curve_bending_x(self: Self) -> "_284.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurveBendingX

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sn_curve_bending_y(self: Self) -> "_284.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurveBendingY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sn_curve_torsional(self: Self) -> "_284.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurveTorsional

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stress_concentration_factors(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_stress_amplitude_of_component_fatigue_strength_sigma_zd_adk_sigma_badk_tau_tadk(
        self: Self,
    ) -> "List[_44.StressMeasurementShaftAxialBendingTorsionalComponentValues]":
        """List[mastapy.shafts.StressMeasurementShaftAxialBendingTorsionalComponentValues]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DIN743201212StressAmplitudeOfComponentFatigueStrengthSigmaZdADKSigmaBADKTauTADK
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def stress_cycles(self: Self) -> "List[_29.ShaftPointStressCycleReporting]":
        """List[mastapy.shafts.ShaftPointStressCycleReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCycles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSectionEndDamageResults._Cast_ShaftSectionEndDamageResults":
        return self._Cast_ShaftSectionEndDamageResults(self)
