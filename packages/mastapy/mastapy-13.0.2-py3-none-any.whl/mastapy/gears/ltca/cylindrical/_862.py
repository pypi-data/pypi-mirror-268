"""CylindricalGearMeshLoadedContactPoint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.ltca import _847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_POINT = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearMeshLoadedContactPoint"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.materials import _270
    from mastapy.gears.rating.cylindrical.iso6336 import _529


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshLoadedContactPoint",)


Self = TypeVar("Self", bound="CylindricalGearMeshLoadedContactPoint")


class CylindricalGearMeshLoadedContactPoint(_847.GearMeshLoadedContactPoint):
    """CylindricalGearMeshLoadedContactPoint

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_POINT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshLoadedContactPoint"
    )

    class _Cast_CylindricalGearMeshLoadedContactPoint:
        """Special nested class for casting CylindricalGearMeshLoadedContactPoint to subclasses."""

        def __init__(
            self: "CylindricalGearMeshLoadedContactPoint._Cast_CylindricalGearMeshLoadedContactPoint",
            parent: "CylindricalGearMeshLoadedContactPoint",
        ):
            self._parent = parent

        @property
        def gear_mesh_loaded_contact_point(
            self: "CylindricalGearMeshLoadedContactPoint._Cast_CylindricalGearMeshLoadedContactPoint",
        ) -> "_847.GearMeshLoadedContactPoint":
            return self._parent._cast(_847.GearMeshLoadedContactPoint)

        @property
        def cylindrical_gear_mesh_loaded_contact_point(
            self: "CylindricalGearMeshLoadedContactPoint._Cast_CylindricalGearMeshLoadedContactPoint",
        ) -> "CylindricalGearMeshLoadedContactPoint":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshLoadedContactPoint._Cast_CylindricalGearMeshLoadedContactPoint",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshLoadedContactPoint.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_benedict_and_kelley(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionBenedictAndKelley

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_of_maximum_material_exposure_gear_aiso633642019(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaximumMaterialExposureGearAISO633642019

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_of_maximum_material_exposure_gear_biso633642019(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaximumMaterialExposureGearBISO633642019

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_position_gear_a(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthPositionGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_position_gear_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthPositionGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def is_gear_a_tip_contact_point(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsGearATipContactPoint

        if temp is None:
            return False

        return temp

    @property
    def is_gear_b_tip_contact_point(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsGearBTipContactPoint

        if temp is None:
            return False

        return temp

    @property
    def is_tip_contact_point(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsTipContactPoint

        if temp is None:
            return False

        return temp

    @property
    def maximum_material_exposure_gear_aiso633642019(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMaterialExposureGearAISO633642019

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_material_exposure_gear_biso633642019(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMaterialExposureGearBISO633642019

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_contact_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_minimum_lubricant_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingMinimumLubricantFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_specific_lubricant_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSpecificLubricantFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_velocity_pv(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureVelocityPV

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_contact_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_contact_temperature_agma925a03(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureAGMA925A03

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_contact_temperature_agma925b22(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureAGMA925B22

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_contact_temperature_din399041987(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureDIN399041987

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_flash_temperature_agma925a03(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureAGMA925A03

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_flash_temperature_agma925b22(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureAGMA925B22

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_flash_temperature_din399041987(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureDIN399041987

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_agma925a03(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorAGMA925A03

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_agma925b22(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorAGMA925B22

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_din399041987(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorDIN399041987

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_profile_measurement(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAProfileMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_profile_measurement(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBProfileMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lubrication_detail(self: Self) -> "_270.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_flank_fracture_analysis_gear_a(
        self: Self,
    ) -> "_529.ToothFlankFractureAnalysisContactPointMethodA":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointMethodA

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFlankFractureAnalysisGearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_flank_fracture_analysis_gear_b(
        self: Self,
    ) -> "_529.ToothFlankFractureAnalysisContactPointMethodA":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointMethodA

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFlankFractureAnalysisGearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshLoadedContactPoint._Cast_CylindricalGearMeshLoadedContactPoint":
        return self._Cast_CylindricalGearMeshLoadedContactPoint(self)
