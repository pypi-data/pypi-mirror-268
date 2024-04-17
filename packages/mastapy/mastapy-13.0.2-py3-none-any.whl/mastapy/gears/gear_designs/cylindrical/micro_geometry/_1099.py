"""CylindricalGearBiasModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BIAS_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearBiasModification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.micro_geometry import _582


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearBiasModification",)


Self = TypeVar("Self", bound="CylindricalGearBiasModification")


class CylindricalGearBiasModification(_572.BiasModification):
    """CylindricalGearBiasModification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BIAS_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearBiasModification")

    class _Cast_CylindricalGearBiasModification:
        """Special nested class for casting CylindricalGearBiasModification to subclasses."""

        def __init__(
            self: "CylindricalGearBiasModification._Cast_CylindricalGearBiasModification",
            parent: "CylindricalGearBiasModification",
        ):
            self._parent = parent

        @property
        def bias_modification(
            self: "CylindricalGearBiasModification._Cast_CylindricalGearBiasModification",
        ) -> "_572.BiasModification":
            return self._parent._cast(_572.BiasModification)

        @property
        def modification(
            self: "CylindricalGearBiasModification._Cast_CylindricalGearBiasModification",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_bias_modification(
            self: "CylindricalGearBiasModification._Cast_CylindricalGearBiasModification",
        ) -> "CylindricalGearBiasModification":
            return self._parent

        def __getattr__(
            self: "CylindricalGearBiasModification._Cast_CylindricalGearBiasModification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearBiasModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_evaluation_left_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadEvaluationLeftLimit

        if temp is None:
            return 0.0

        return temp

    @lead_evaluation_left_limit.setter
    @enforce_parameter_types
    def lead_evaluation_left_limit(self: Self, value: "float"):
        self.wrapped.LeadEvaluationLeftLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def lead_evaluation_right_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadEvaluationRightLimit

        if temp is None:
            return 0.0

        return temp

    @lead_evaluation_right_limit.setter
    @enforce_parameter_types
    def lead_evaluation_right_limit(self: Self, value: "float"):
        self.wrapped.LeadEvaluationRightLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_angle_mod_at_left_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngleModAtLeftLimit

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_mod_at_left_limit.setter
    @enforce_parameter_types
    def pressure_angle_mod_at_left_limit(self: Self, value: "float"):
        self.wrapped.PressureAngleModAtLeftLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_angle_mod_at_right_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngleModAtRightLimit

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_mod_at_right_limit.setter
    @enforce_parameter_types
    def pressure_angle_mod_at_right_limit(self: Self, value: "float"):
        self.wrapped.PressureAngleModAtRightLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimitDiameter

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit_diameter.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit_diameter(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationLowerLimitDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimitRadius

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit_radius.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit_radius(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationLowerLimitRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimitRollAngle

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit_roll_angle.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit_roll_angle(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationLowerLimitRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimitRollDistance

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit_roll_distance.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit_roll_distance(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationLowerLimitRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimitDiameter

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit_diameter.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit_diameter(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationUpperLimitDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimitRadius

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit_radius.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit_radius(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationUpperLimitRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimitRollAngle

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit_roll_angle.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit_roll_angle(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationUpperLimitRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimitRollDistance

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit_roll_distance.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit_roll_distance(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationUpperLimitRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def relief_at_left_limit_isoagmadin(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtLeftLimitISOAGMADIN

        if temp is None:
            return 0.0

        return temp

    @relief_at_left_limit_isoagmadin.setter
    @enforce_parameter_types
    def relief_at_left_limit_isoagmadin(self: Self, value: "float"):
        self.wrapped.ReliefAtLeftLimitISOAGMADIN = (
            float(value) if value is not None else 0.0
        )

    @property
    def relief_at_left_limit_ldp(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtLeftLimitLDP

        if temp is None:
            return 0.0

        return temp

    @relief_at_left_limit_ldp.setter
    @enforce_parameter_types
    def relief_at_left_limit_ldp(self: Self, value: "float"):
        self.wrapped.ReliefAtLeftLimitLDP = float(value) if value is not None else 0.0

    @property
    def relief_at_left_limit_vdi(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtLeftLimitVDI

        if temp is None:
            return 0.0

        return temp

    @relief_at_left_limit_vdi.setter
    @enforce_parameter_types
    def relief_at_left_limit_vdi(self: Self, value: "float"):
        self.wrapped.ReliefAtLeftLimitVDI = float(value) if value is not None else 0.0

    @property
    def relief_at_right_limit_isoagmadin(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtRightLimitISOAGMADIN

        if temp is None:
            return 0.0

        return temp

    @relief_at_right_limit_isoagmadin.setter
    @enforce_parameter_types
    def relief_at_right_limit_isoagmadin(self: Self, value: "float"):
        self.wrapped.ReliefAtRightLimitISOAGMADIN = (
            float(value) if value is not None else 0.0
        )

    @property
    def relief_at_right_limit_ldp(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtRightLimitLDP

        if temp is None:
            return 0.0

        return temp

    @relief_at_right_limit_ldp.setter
    @enforce_parameter_types
    def relief_at_right_limit_ldp(self: Self, value: "float"):
        self.wrapped.ReliefAtRightLimitLDP = float(value) if value is not None else 0.0

    @property
    def relief_at_right_limit_vdi(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtRightLimitVDI

        if temp is None:
            return 0.0

        return temp

    @relief_at_right_limit_vdi.setter
    @enforce_parameter_types
    def relief_at_right_limit_vdi(self: Self, value: "float"):
        self.wrapped.ReliefAtRightLimitVDI = float(value) if value is not None else 0.0

    @property
    def zero_bias_relief(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZeroBiasRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_evaluation_lower_limit(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileEvaluationLowerLimit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_evaluation_upper_limit(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileEvaluationUpperLimit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def relief_of(self: Self, face_width: "float", roll_distance: "float") -> "float":
        """float

        Args:
            face_width (float)
            roll_distance (float)
        """
        face_width = float(face_width)
        roll_distance = float(roll_distance)
        method_result = self.wrapped.ReliefOf(
            face_width if face_width else 0.0, roll_distance if roll_distance else 0.0
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearBiasModification._Cast_CylindricalGearBiasModification":
        return self._Cast_CylindricalGearBiasModification(self)
