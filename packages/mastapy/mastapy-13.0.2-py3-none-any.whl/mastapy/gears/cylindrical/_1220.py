"""PointsWithWorstResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINTS_WITH_WORST_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.Cylindrical", "PointsWithWorstResults"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _862


__docformat__ = "restructuredtext en"
__all__ = ("PointsWithWorstResults",)


Self = TypeVar("Self", bound="PointsWithWorstResults")


class PointsWithWorstResults(_0.APIBase):
    """PointsWithWorstResults

    This is a mastapy class.
    """

    TYPE = _POINTS_WITH_WORST_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointsWithWorstResults")

    class _Cast_PointsWithWorstResults:
        """Special nested class for casting PointsWithWorstResults to subclasses."""

        def __init__(
            self: "PointsWithWorstResults._Cast_PointsWithWorstResults",
            parent: "PointsWithWorstResults",
        ):
            self._parent = parent

        @property
        def points_with_worst_results(
            self: "PointsWithWorstResults._Cast_PointsWithWorstResults",
        ) -> "PointsWithWorstResults":
            return self._parent

        def __getattr__(
            self: "PointsWithWorstResults._Cast_PointsWithWorstResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointsWithWorstResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_benedict_and_kelley(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionBenedictAndKelley

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def depth_of_max_shear_stress(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaxShearStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_per_unit_length(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForcePerUnitLength

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gap_between_loaded_flanks_transverse(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GapBetweenLoadedFlanksTransverse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gap_between_unloaded_flanks_transverse(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GapBetweenUnloadedFlanksTransverse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a_depth_of_maximum_material_exposure_iso633642019(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearADepthOfMaximumMaterialExposureISO633642019

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a_maximum_material_exposure_iso633642019(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAMaximumMaterialExposureISO633642019

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_depth_of_maximum_material_exposure_iso633642019(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBDepthOfMaximumMaterialExposureISO633642019

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_maximum_material_exposure_iso633642019(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBMaximumMaterialExposureISO633642019

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hertzian_contact_half_width(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactHalfWidth

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def max_pressure(self: Self) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxPressure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def max_shear_stress(self: Self) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxShearStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_contact_temperature_isotr1514412010(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperatureISOTR1514412010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_contact_temperature_isotr1514412014(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperatureISOTR1514412014

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_contact_temperature_isots6336222018(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperatureISOTS6336222018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_flash_temperature_isotr1514412010(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperatureISOTR1514412010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_flash_temperature_isotr1514412014(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperatureISOTR1514412014

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_flash_temperature_isots6336222018(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperatureISOTS6336222018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_safety_factor_isotr1514412010(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorISOTR1514412010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_safety_factor_isotr1514412014(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorISOTR1514412014

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting_safety_factor_isots6336222018(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorISOTS6336222018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_lubricant_film_thickness_isotr1514412010(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThicknessISOTR1514412010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_lubricant_film_thickness_isotr1514412014(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThicknessISOTR1514412014

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_lubricant_film_thickness_isots6336222018(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThicknessISOTS6336222018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pressure_velocity_pv(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureVelocityPV

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_contact_temperature_agma925a03(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureAGMA925A03

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_contact_temperature_agma925b22(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureAGMA925B22

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_contact_temperature_din399041987(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureDIN399041987

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_contact_temperature_isotr1398912000(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureISOTR1398912000

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_contact_temperature_isots6336202017(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureISOTS6336202017

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_contact_temperature_isots6336202022(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureISOTS6336202022

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_flash_temperature_agma925a03(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureAGMA925A03

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_flash_temperature_agma925b22(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureAGMA925B22

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_flash_temperature_din399041987(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureDIN399041987

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_flash_temperature_isotr1398912000(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureISOTR1398912000

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_flash_temperature_isots6336202017(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureISOTS6336202017

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_flash_temperature_isots6336202022(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureISOTS6336202022

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_safety_factor_agma925a03(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorAGMA925A03

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_safety_factor_agma925b22(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorAGMA925B22

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_safety_factor_din399041987(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorDIN399041987

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_safety_factor_isotr1398912000(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorISOTR1398912000

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_safety_factor_isots6336202017(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorISOTS6336202017

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing_safety_factor_isots6336202022(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorISOTS6336202022

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sliding_power_loss(self: Self) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingPowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sliding_velocity(self: Self) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specific_lubricant_film_thickness_isotr1514412010(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLubricantFilmThicknessISOTR1514412010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specific_lubricant_film_thickness_isotr1514412014(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLubricantFilmThicknessISOTR1514412014

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specific_lubricant_film_thickness_isots6336222018(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLubricantFilmThicknessISOTS6336222018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_deflection_for_mesh(
        self: Self,
    ) -> "_862.CylindricalGearMeshLoadedContactPoint":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDeflectionForMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PointsWithWorstResults._Cast_PointsWithWorstResults":
        return self._Cast_PointsWithWorstResults(self)
