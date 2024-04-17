"""CylindricalGearProfileModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PROFILE_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearProfileModification",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112
    from mastapy.gears.micro_geometry import _582


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearProfileModification",)


Self = TypeVar("Self", bound="CylindricalGearProfileModification")


class CylindricalGearProfileModification(_585.ProfileModification):
    """CylindricalGearProfileModification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PROFILE_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearProfileModification")

    class _Cast_CylindricalGearProfileModification:
        """Special nested class for casting CylindricalGearProfileModification to subclasses."""

        def __init__(
            self: "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification",
            parent: "CylindricalGearProfileModification",
        ):
            self._parent = parent

        @property
        def profile_modification(
            self: "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification",
        ) -> "_585.ProfileModification":
            return self._parent._cast(_585.ProfileModification)

        @property
        def modification(
            self: "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(
            self: "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification",
        ) -> "_1112.CylindricalGearProfileModificationAtFaceWidthPosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112

            return self._parent._cast(
                _1112.CylindricalGearProfileModificationAtFaceWidthPosition
            )

        @property
        def cylindrical_gear_profile_modification(
            self: "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification",
        ) -> "CylindricalGearProfileModification":
            return self._parent

        def __getattr__(
            self: "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification",
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
        self: Self, instance_to_wrap: "CylindricalGearProfileModification.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def barrelling_peak_point_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarrellingPeakPointDiameter

        if temp is None:
            return 0.0

        return temp

    @barrelling_peak_point_diameter.setter
    @enforce_parameter_types
    def barrelling_peak_point_diameter(self: Self, value: "float"):
        self.wrapped.BarrellingPeakPointDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def barrelling_peak_point_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarrellingPeakPointRadius

        if temp is None:
            return 0.0

        return temp

    @barrelling_peak_point_radius.setter
    @enforce_parameter_types
    def barrelling_peak_point_radius(self: Self, value: "float"):
        self.wrapped.BarrellingPeakPointRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def barrelling_peak_point_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarrellingPeakPointRollAngle

        if temp is None:
            return 0.0

        return temp

    @barrelling_peak_point_roll_angle.setter
    @enforce_parameter_types
    def barrelling_peak_point_roll_angle(self: Self, value: "float"):
        self.wrapped.BarrellingPeakPointRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def barrelling_peak_point_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarrellingPeakPointRollDistance

        if temp is None:
            return 0.0

        return temp

    @barrelling_peak_point_roll_distance.setter
    @enforce_parameter_types
    def barrelling_peak_point_roll_distance(self: Self, value: "float"):
        self.wrapped.BarrellingPeakPointRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitDiameter

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_diameter.setter
    @enforce_parameter_types
    def evaluation_lower_limit_diameter(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_diameter_for_zero_root_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitDiameterForZeroRootRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_diameter_for_zero_root_relief.setter
    @enforce_parameter_types
    def evaluation_lower_limit_diameter_for_zero_root_relief(
        self: Self, value: "float"
    ):
        self.wrapped.EvaluationLowerLimitDiameterForZeroRootRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitRadius

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_radius.setter
    @enforce_parameter_types
    def evaluation_lower_limit_radius(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_radius_for_zero_root_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitRadiusForZeroRootRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_radius_for_zero_root_relief.setter
    @enforce_parameter_types
    def evaluation_lower_limit_radius_for_zero_root_relief(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitRadiusForZeroRootRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitRollAngle

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_roll_angle.setter
    @enforce_parameter_types
    def evaluation_lower_limit_roll_angle(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_roll_angle_for_zero_root_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitRollAngleForZeroRootRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_roll_angle_for_zero_root_relief.setter
    @enforce_parameter_types
    def evaluation_lower_limit_roll_angle_for_zero_root_relief(
        self: Self, value: "float"
    ):
        self.wrapped.EvaluationLowerLimitRollAngleForZeroRootRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitRollDistance

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_roll_distance.setter
    @enforce_parameter_types
    def evaluation_lower_limit_roll_distance(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_roll_distance_for_zero_root_relief(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitRollDistanceForZeroRootRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_roll_distance_for_zero_root_relief.setter
    @enforce_parameter_types
    def evaluation_lower_limit_roll_distance_for_zero_root_relief(
        self: Self, value: "float"
    ):
        self.wrapped.EvaluationLowerLimitRollDistanceForZeroRootRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_root_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRootReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_root_relief_diameter.setter
    @enforce_parameter_types
    def evaluation_of_linear_root_relief_diameter(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRootReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_root_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRootReliefRadius

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_root_relief_radius.setter
    @enforce_parameter_types
    def evaluation_of_linear_root_relief_radius(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRootReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_root_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRootReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_root_relief_roll_angle.setter
    @enforce_parameter_types
    def evaluation_of_linear_root_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRootReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_root_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRootReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_root_relief_roll_distance.setter
    @enforce_parameter_types
    def evaluation_of_linear_root_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRootReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_tip_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearTipReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_tip_relief_diameter.setter
    @enforce_parameter_types
    def evaluation_of_linear_tip_relief_diameter(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearTipReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_tip_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearTipReliefRadius

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_tip_relief_radius.setter
    @enforce_parameter_types
    def evaluation_of_linear_tip_relief_radius(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearTipReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_tip_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearTipReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_tip_relief_roll_angle.setter
    @enforce_parameter_types
    def evaluation_of_linear_tip_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearTipReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_tip_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearTipReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_tip_relief_roll_distance.setter
    @enforce_parameter_types
    def evaluation_of_linear_tip_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearTipReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_root_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRootReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_root_relief_diameter.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_root_relief_diameter(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRootReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_root_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRootReliefRadius

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_root_relief_radius.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_root_relief_radius(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRootReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_root_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRootReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_root_relief_roll_angle.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_root_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRootReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_root_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRootReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_root_relief_roll_distance.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_root_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRootReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_tip_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicTipReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_tip_relief_diameter.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_tip_relief_diameter(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicTipReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_tip_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicTipReliefRadius

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_tip_relief_radius.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_tip_relief_radius(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicTipReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_tip_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicTipReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_tip_relief_roll_angle.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_tip_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicTipReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_tip_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicTipReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_tip_relief_roll_distance.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_tip_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicTipReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitDiameter

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_diameter.setter
    @enforce_parameter_types
    def evaluation_upper_limit_diameter(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_diameter_for_zero_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitDiameterForZeroTipRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_diameter_for_zero_tip_relief.setter
    @enforce_parameter_types
    def evaluation_upper_limit_diameter_for_zero_tip_relief(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitDiameterForZeroTipRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitRadius

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_radius.setter
    @enforce_parameter_types
    def evaluation_upper_limit_radius(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_radius_for_zero_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitRadiusForZeroTipRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_radius_for_zero_tip_relief.setter
    @enforce_parameter_types
    def evaluation_upper_limit_radius_for_zero_tip_relief(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitRadiusForZeroTipRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitRollAngle

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_roll_angle.setter
    @enforce_parameter_types
    def evaluation_upper_limit_roll_angle(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_roll_angle_for_zero_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitRollAngleForZeroTipRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_roll_angle_for_zero_tip_relief.setter
    @enforce_parameter_types
    def evaluation_upper_limit_roll_angle_for_zero_tip_relief(
        self: Self, value: "float"
    ):
        self.wrapped.EvaluationUpperLimitRollAngleForZeroTipRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitRollDistance

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_roll_distance.setter
    @enforce_parameter_types
    def evaluation_upper_limit_roll_distance(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_roll_distance_for_zero_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitRollDistanceForZeroTipRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_roll_distance_for_zero_tip_relief.setter
    @enforce_parameter_types
    def evaluation_upper_limit_roll_distance_for_zero_tip_relief(
        self: Self, value: "float"
    ):
        self.wrapped.EvaluationUpperLimitRollDistanceForZeroTipRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_isoagmadin(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefISOAGMADIN

        if temp is None:
            return 0.0

        return temp

    @linear_relief_isoagmadin.setter
    @enforce_parameter_types
    def linear_relief_isoagmadin(self: Self, value: "float"):
        self.wrapped.LinearReliefISOAGMADIN = float(value) if value is not None else 0.0

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
    def linear_relief_vdi(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearReliefVDI

        if temp is None:
            return 0.0

        return temp

    @linear_relief_vdi.setter
    @enforce_parameter_types
    def linear_relief_vdi(self: Self, value: "float"):
        self.wrapped.LinearReliefVDI = float(value) if value is not None else 0.0

    @property
    def pressure_angle_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngleModification

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_modification.setter
    @enforce_parameter_types
    def pressure_angle_modification(self: Self, value: "float"):
        self.wrapped.PressureAngleModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_modification_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def start_of_linear_root_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRootReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_root_relief_diameter.setter
    @enforce_parameter_types
    def start_of_linear_root_relief_diameter(self: Self, value: "float"):
        self.wrapped.StartOfLinearRootReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_root_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRootReliefRadius

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_root_relief_radius.setter
    @enforce_parameter_types
    def start_of_linear_root_relief_radius(self: Self, value: "float"):
        self.wrapped.StartOfLinearRootReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_root_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRootReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_root_relief_roll_angle.setter
    @enforce_parameter_types
    def start_of_linear_root_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.StartOfLinearRootReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_root_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRootReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_root_relief_roll_distance.setter
    @enforce_parameter_types
    def start_of_linear_root_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.StartOfLinearRootReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_tip_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearTipReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_tip_relief_diameter.setter
    @enforce_parameter_types
    def start_of_linear_tip_relief_diameter(self: Self, value: "float"):
        self.wrapped.StartOfLinearTipReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_tip_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearTipReliefRadius

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_tip_relief_radius.setter
    @enforce_parameter_types
    def start_of_linear_tip_relief_radius(self: Self, value: "float"):
        self.wrapped.StartOfLinearTipReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_tip_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearTipReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_tip_relief_roll_angle.setter
    @enforce_parameter_types
    def start_of_linear_tip_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.StartOfLinearTipReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_tip_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearTipReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_tip_relief_roll_distance.setter
    @enforce_parameter_types
    def start_of_linear_tip_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.StartOfLinearTipReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_root_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRootReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_root_relief_diameter.setter
    @enforce_parameter_types
    def start_of_parabolic_root_relief_diameter(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRootReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_root_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRootReliefRadius

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_root_relief_radius.setter
    @enforce_parameter_types
    def start_of_parabolic_root_relief_radius(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRootReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_root_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRootReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_root_relief_roll_angle.setter
    @enforce_parameter_types
    def start_of_parabolic_root_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRootReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_root_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRootReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_root_relief_roll_distance.setter
    @enforce_parameter_types
    def start_of_parabolic_root_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRootReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_tip_relief_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicTipReliefDiameter

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_tip_relief_diameter.setter
    @enforce_parameter_types
    def start_of_parabolic_tip_relief_diameter(self: Self, value: "float"):
        self.wrapped.StartOfParabolicTipReliefDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_tip_relief_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicTipReliefRadius

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_tip_relief_radius.setter
    @enforce_parameter_types
    def start_of_parabolic_tip_relief_radius(self: Self, value: "float"):
        self.wrapped.StartOfParabolicTipReliefRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_tip_relief_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicTipReliefRollAngle

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_tip_relief_roll_angle.setter
    @enforce_parameter_types
    def start_of_parabolic_tip_relief_roll_angle(self: Self, value: "float"):
        self.wrapped.StartOfParabolicTipReliefRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_tip_relief_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicTipReliefRollDistance

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_tip_relief_roll_distance.setter
    @enforce_parameter_types
    def start_of_parabolic_tip_relief_roll_distance(self: Self, value: "float"):
        self.wrapped.StartOfParabolicTipReliefRollDistance = (
            float(value) if value is not None else 0.0
        )

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

    @property
    def barrelling_peak_point(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BarrellingPeakPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def evaluation_lower_limit(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EvaluationLowerLimit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def evaluation_lower_limit_for_zero_root_relief(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EvaluationLowerLimitForZeroRootRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def evaluation_upper_limit(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EvaluationUpperLimit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def evaluation_upper_limit_for_zero_tip_relief(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EvaluationUpperLimitForZeroTipRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_root_relief_evaluation(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearRootReliefEvaluation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_root_relief_start(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearRootReliefStart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_tip_relief_evaluation(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearTipReliefEvaluation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_tip_relief_start(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearTipReliefStart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parabolic_root_relief_evaluation(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParabolicRootReliefEvaluation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parabolic_root_relief_start(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParabolicRootReliefStart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parabolic_tip_relief_evaluation(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParabolicTipReliefEvaluation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parabolic_tip_relief_start(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParabolicTipReliefStart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def relief_of(self: Self, roll_distance: "float") -> "float":
        """float

        Args:
            roll_distance (float)
        """
        roll_distance = float(roll_distance)
        method_result = self.wrapped.ReliefOf(roll_distance if roll_distance else 0.0)
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearProfileModification._Cast_CylindricalGearProfileModification":
        return self._Cast_CylindricalGearProfileModification(self)
