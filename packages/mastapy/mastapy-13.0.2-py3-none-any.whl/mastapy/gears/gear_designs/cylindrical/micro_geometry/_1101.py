"""CylindricalGearFlankMicroGeometry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.micro_geometry import _573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearFlankMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_data import _1572
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1099,
        _1102,
        _1109,
        _1111,
        _1116,
        _1120,
        _1122,
        _1131,
        _1133,
        _1136,
        _1137,
    )
    from mastapy.gears.gear_designs.cylindrical import _1029, _1016


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFlankMicroGeometry",)


Self = TypeVar("Self", bound="CylindricalGearFlankMicroGeometry")


class CylindricalGearFlankMicroGeometry(_573.FlankMicroGeometry):
    """CylindricalGearFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFlankMicroGeometry")

    class _Cast_CylindricalGearFlankMicroGeometry:
        """Special nested class for casting CylindricalGearFlankMicroGeometry to subclasses."""

        def __init__(
            self: "CylindricalGearFlankMicroGeometry._Cast_CylindricalGearFlankMicroGeometry",
            parent: "CylindricalGearFlankMicroGeometry",
        ):
            self._parent = parent

        @property
        def flank_micro_geometry(
            self: "CylindricalGearFlankMicroGeometry._Cast_CylindricalGearFlankMicroGeometry",
        ) -> "_573.FlankMicroGeometry":
            return self._parent._cast(_573.FlankMicroGeometry)

        @property
        def cylindrical_gear_flank_micro_geometry(
            self: "CylindricalGearFlankMicroGeometry._Cast_CylindricalGearFlankMicroGeometry",
        ) -> "CylindricalGearFlankMicroGeometry":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFlankMicroGeometry._Cast_CylindricalGearFlankMicroGeometry",
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
        self: Self, instance_to_wrap: "CylindricalGearFlankMicroGeometry.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_matrix(self: Self) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.MicroGeometryMatrix

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @micro_geometry_matrix.setter
    @enforce_parameter_types
    def micro_geometry_matrix(self: Self, value: "_1572.GriddedSurfaceAccessor"):
        self.wrapped.MicroGeometryMatrix = value.wrapped

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_assuming_unmodified_normal_module_and_pressure_angle_modification(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModuleAndPressureAngleModification
        )

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
    def use_measured_map_data(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMeasuredMapData

        if temp is None:
            return False

        return temp

    @use_measured_map_data.setter
    @enforce_parameter_types
    def use_measured_map_data(self: Self, value: "bool"):
        self.wrapped.UseMeasuredMapData = bool(value) if value is not None else False

    @property
    def bias(self: Self) -> "_1099.CylindricalGearBiasModification":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearBiasModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bias

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_relief(self: Self) -> "_1102.CylindricalGearLeadModification":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearLeadModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry_map(self: Self) -> "_1109.CylindricalGearMicroGeometryMap":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryMap

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometryMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_control_point(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileControlPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_relief(self: Self) -> "_1111.CylindricalGearProfileModification":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearProfileModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def triangular_end_relief(
        self: Self,
    ) -> "_1116.CylindricalGearTriangularEndModification":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearTriangularEndModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TriangularEndRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_form_deviation_points(
        self: Self,
    ) -> "List[_1120.LeadFormReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.LeadFormReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadFormDeviationPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def lead_slope_deviation_points(
        self: Self,
    ) -> "List[_1122.LeadSlopeReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.LeadSlopeReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadSlopeDeviationPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def profile_form_deviation_points(
        self: Self,
    ) -> "List[_1131.ProfileFormReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.ProfileFormReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviationPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def profile_slope_deviation_at_10_percent_face_width(
        self: Self,
    ) -> "List[_1133.ProfileSlopeReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.ProfileSlopeReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviationAt10PercentFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def profile_slope_deviation_at_50_percent_face_width(
        self: Self,
    ) -> "List[_1133.ProfileSlopeReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.ProfileSlopeReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviationAt50PercentFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def profile_slope_deviation_at_90_percent_face_width(
        self: Self,
    ) -> "List[_1133.ProfileSlopeReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.ProfileSlopeReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviationAt90PercentFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def total_lead_relief_points(
        self: Self,
    ) -> "List[_1136.TotalLeadReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.TotalLeadReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalLeadReliefPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def total_profile_relief_points(
        self: Self,
    ) -> "List[_1137.TotalProfileReliefWithDeviation]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.TotalProfileReliefWithDeviation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalProfileReliefPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_design(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def total_relief(
        self: Self, face_width: "float", roll_distance: "float"
    ) -> "float":
        """float

        Args:
            face_width (float)
            roll_distance (float)
        """
        face_width = float(face_width)
        roll_distance = float(roll_distance)
        method_result = self.wrapped.TotalRelief(
            face_width if face_width else 0.0, roll_distance if roll_distance else 0.0
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFlankMicroGeometry._Cast_CylindricalGearFlankMicroGeometry":
        return self._Cast_CylindricalGearFlankMicroGeometry(self)
