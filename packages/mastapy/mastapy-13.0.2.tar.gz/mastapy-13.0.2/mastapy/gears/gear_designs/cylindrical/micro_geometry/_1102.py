"""CylindricalGearLeadModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LEAD_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearLeadModification",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1103
    from mastapy.gears.micro_geometry import _582


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLeadModification",)


Self = TypeVar("Self", bound="CylindricalGearLeadModification")


class CylindricalGearLeadModification(_575.LeadModification):
    """CylindricalGearLeadModification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LEAD_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearLeadModification")

    class _Cast_CylindricalGearLeadModification:
        """Special nested class for casting CylindricalGearLeadModification to subclasses."""

        def __init__(
            self: "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
            parent: "CylindricalGearLeadModification",
        ):
            self._parent = parent

        @property
        def lead_modification(
            self: "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
        ) -> "_575.LeadModification":
            return self._parent._cast(_575.LeadModification)

        @property
        def modification(
            self: "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(
            self: "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
        ) -> "_1103.CylindricalGearLeadModificationAtProfilePosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1103

            return self._parent._cast(
                _1103.CylindricalGearLeadModificationAtProfilePosition
            )

        @property
        def cylindrical_gear_lead_modification(
            self: "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
        ) -> "CylindricalGearLeadModification":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearLeadModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def evaluation_left_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLeftLimit

        if temp is None:
            return 0.0

        return temp

    @evaluation_left_limit.setter
    @enforce_parameter_types
    def evaluation_left_limit(self: Self, value: "float"):
        self.wrapped.EvaluationLeftLimit = float(value) if value is not None else 0.0

    @property
    def evaluation_of_linear_left_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearLeftRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_left_relief.setter
    @enforce_parameter_types
    def evaluation_of_linear_left_relief(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_right_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRightRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_right_relief.setter
    @enforce_parameter_types
    def evaluation_of_linear_right_relief(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_left_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicLeftRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_left_relief.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_left_relief(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_right_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRightRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_right_relief.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_right_relief(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_right_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationRightLimit

        if temp is None:
            return 0.0

        return temp

    @evaluation_right_limit.setter
    @enforce_parameter_types
    def evaluation_right_limit(self: Self, value: "float"):
        self.wrapped.EvaluationRightLimit = float(value) if value is not None else 0.0

    @property
    def evaluation_side_limit(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationSideLimit

        if temp is None:
            return None

        return temp

    @evaluation_side_limit.setter
    @enforce_parameter_types
    def evaluation_side_limit(self: Self, value: "Optional[float]"):
        self.wrapped.EvaluationSideLimit = value

    @property
    def evaluation_of_linear_side_relief(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationOfLinearSideRelief

        if temp is None:
            return None

        return temp

    @evaluation_of_linear_side_relief.setter
    @enforce_parameter_types
    def evaluation_of_linear_side_relief(self: Self, value: "Optional[float]"):
        self.wrapped.EvaluationOfLinearSideRelief = value

    @property
    def evaluation_of_parabolic_side_relief(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationOfParabolicSideRelief

        if temp is None:
            return None

        return temp

    @evaluation_of_parabolic_side_relief.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_side_relief(self: Self, value: "Optional[float]"):
        self.wrapped.EvaluationOfParabolicSideRelief = value

    @property
    def helix_angle_modification_at_original_reference_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleModificationAtOriginalReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @helix_angle_modification_at_original_reference_diameter.setter
    @enforce_parameter_types
    def helix_angle_modification_at_original_reference_diameter(
        self: Self, value: "float"
    ):
        self.wrapped.HelixAngleModificationAtOriginalReferenceDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def lead_modification_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_relief_isodinagmavdi(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefISODINAGMAVDI

        if temp is None:
            return 0.0

        return temp

    @linear_relief_isodinagmavdi.setter
    @enforce_parameter_types
    def linear_relief_isodinagmavdi(self: Self, value: "float"):
        self.wrapped.LinearReliefISODINAGMAVDI = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_isodinagmavdi_across_full_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefISODINAGMAVDIAcrossFullFaceWidth

        if temp is None:
            return 0.0

        return temp

    @linear_relief_isodinagmavdi_across_full_face_width.setter
    @enforce_parameter_types
    def linear_relief_isodinagmavdi_across_full_face_width(self: Self, value: "float"):
        self.wrapped.LinearReliefISODINAGMAVDIAcrossFullFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_ldp(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefLDP

        if temp is None:
            return 0.0

        return temp

    @linear_relief_ldp.setter
    @enforce_parameter_types
    def linear_relief_ldp(self: Self, value: "float"):
        self.wrapped.LinearReliefLDP = float(value) if value is not None else 0.0

    @property
    def linear_relief_ldp_across_full_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefLDPAcrossFullFaceWidth

        if temp is None:
            return 0.0

        return temp

    @linear_relief_ldp_across_full_face_width.setter
    @enforce_parameter_types
    def linear_relief_ldp_across_full_face_width(self: Self, value: "float"):
        self.wrapped.LinearReliefLDPAcrossFullFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_across_full_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefAcrossFullFaceWidth

        if temp is None:
            return 0.0

        return temp

    @linear_relief_across_full_face_width.setter
    @enforce_parameter_types
    def linear_relief_across_full_face_width(self: Self, value: "float"):
        self.wrapped.LinearReliefAcrossFullFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_base_helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModifiedBaseHelixAngle

        if temp is None:
            return 0.0

        return temp

    @modified_base_helix_angle.setter
    @enforce_parameter_types
    def modified_base_helix_angle(self: Self, value: "float"):
        self.wrapped.ModifiedBaseHelixAngle = float(value) if value is not None else 0.0

    @property
    def modified_helix_angle_assuming_unmodified_normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModifiedHelixAngleAssumingUnmodifiedNormalModule

        if temp is None:
            return 0.0

        return temp

    @modified_helix_angle_assuming_unmodified_normal_module.setter
    @enforce_parameter_types
    def modified_helix_angle_assuming_unmodified_normal_module(
        self: Self, value: "float"
    ):
        self.wrapped.ModifiedHelixAngleAssumingUnmodifiedNormalModule = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_helix_angle_at_original_reference_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModifiedHelixAngleAtOriginalReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @modified_helix_angle_at_original_reference_diameter.setter
    @enforce_parameter_types
    def modified_helix_angle_at_original_reference_diameter(self: Self, value: "float"):
        self.wrapped.ModifiedHelixAngleAtOriginalReferenceDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_assuming_unmodified_normal_module(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModule
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_at_original_reference_diameter(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAtOriginalReferenceDiameter
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def start_of_linear_left_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearLeftRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_left_relief.setter
    @enforce_parameter_types
    def start_of_linear_left_relief(self: Self, value: "float"):
        self.wrapped.StartOfLinearLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_right_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRightRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_right_relief.setter
    @enforce_parameter_types
    def start_of_linear_right_relief(self: Self, value: "float"):
        self.wrapped.StartOfLinearRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_side_relief(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.StartOfLinearSideRelief

        if temp is None:
            return None

        return temp

    @start_of_linear_side_relief.setter
    @enforce_parameter_types
    def start_of_linear_side_relief(self: Self, value: "Optional[float]"):
        self.wrapped.StartOfLinearSideRelief = value

    @property
    def start_of_parabolic_left_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicLeftRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_left_relief.setter
    @enforce_parameter_types
    def start_of_parabolic_left_relief(self: Self, value: "float"):
        self.wrapped.StartOfParabolicLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_right_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRightRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_right_relief.setter
    @enforce_parameter_types
    def start_of_parabolic_right_relief(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_side_relief(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.StartOfParabolicSideRelief

        if temp is None:
            return None

        return temp

    @start_of_parabolic_side_relief.setter
    @enforce_parameter_types
    def start_of_parabolic_side_relief(self: Self, value: "Optional[float]"):
        self.wrapped.StartOfParabolicSideRelief = value

    @property
    def use_measured_data(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMeasuredData

        if temp is None:
            return False

        return temp

    @use_measured_data.setter
    @enforce_parameter_types
    def use_measured_data(self: Self, value: "bool"):
        self.wrapped.UseMeasuredData = bool(value) if value is not None else False

    @enforce_parameter_types
    def relief_of(self: Self, face_width: "float") -> "float":
        """float

        Args:
            face_width (float)
        """
        face_width = float(face_width)
        method_result = self.wrapped.ReliefOf(face_width if face_width else 0.0)
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearLeadModification._Cast_CylindricalGearLeadModification":
        return self._Cast_CylindricalGearLeadModification(self)
