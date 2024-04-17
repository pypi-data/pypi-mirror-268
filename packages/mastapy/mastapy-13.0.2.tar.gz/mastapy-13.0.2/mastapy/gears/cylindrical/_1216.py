"""CylindricalGearWorstLTCAContactChartDataAsTextFile"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_WORST_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE = python_net_import(
    "SMT.MastaAPI.Gears.Cylindrical",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearWorstLTCAContactChartDataAsTextFile",)


Self = TypeVar("Self", bound="CylindricalGearWorstLTCAContactChartDataAsTextFile")


class CylindricalGearWorstLTCAContactChartDataAsTextFile(_0.APIBase):
    """CylindricalGearWorstLTCAContactChartDataAsTextFile

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_WORST_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile"
    )

    class _Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile:
        """Special nested class for casting CylindricalGearWorstLTCAContactChartDataAsTextFile to subclasses."""

        def __init__(
            self: "CylindricalGearWorstLTCAContactChartDataAsTextFile._Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile",
            parent: "CylindricalGearWorstLTCAContactChartDataAsTextFile",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_worst_ltca_contact_chart_data_as_text_file(
            self: "CylindricalGearWorstLTCAContactChartDataAsTextFile._Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile",
        ) -> "CylindricalGearWorstLTCAContactChartDataAsTextFile":
            return self._parent

        def __getattr__(
            self: "CylindricalGearWorstLTCAContactChartDataAsTextFile._Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile",
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
        instance_to_wrap: "CylindricalGearWorstLTCAContactChartDataAsTextFile.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_benedict_and_kelley(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionBenedictAndKelley

        if temp is None:
            return ""

        return temp

    @property
    def depth_of_max_shear_stress(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaxShearStress

        if temp is None:
            return ""

        return temp

    @property
    def force_per_unit_length(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForcePerUnitLength

        if temp is None:
            return ""

        return temp

    @property
    def gap_between_loaded_flanks_transverse(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GapBetweenLoadedFlanksTransverse

        if temp is None:
            return ""

        return temp

    @property
    def gap_between_unloaded_flanks_transverse(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GapBetweenUnloadedFlanksTransverse

        if temp is None:
            return ""

        return temp

    @property
    def gear_a_depth_of_maximum_material_exposure_iso633642019(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearADepthOfMaximumMaterialExposureISO633642019

        if temp is None:
            return ""

        return temp

    @property
    def gear_a_maximum_material_exposure_iso633642019(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAMaximumMaterialExposureISO633642019

        if temp is None:
            return ""

        return temp

    @property
    def gear_b_depth_of_maximum_material_exposure_iso633642019(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBDepthOfMaximumMaterialExposureISO633642019

        if temp is None:
            return ""

        return temp

    @property
    def gear_b_maximum_material_exposure_iso633642019(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBMaximumMaterialExposureISO633642019

        if temp is None:
            return ""

        return temp

    @property
    def hertzian_contact_half_width(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactHalfWidth

        if temp is None:
            return ""

        return temp

    @property
    def max_pressure(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxPressure

        if temp is None:
            return ""

        return temp

    @property
    def max_shear_stress(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxShearStress

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_contact_temperature_isotr1514412010(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperatureISOTR1514412010

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_contact_temperature_isotr1514412014(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperatureISOTR1514412014

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_contact_temperature_isots6336222018(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingContactTemperatureISOTS6336222018

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_flash_temperature_isotr1514412010(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperatureISOTR1514412010

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_flash_temperature_isotr1514412014(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperatureISOTR1514412014

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_flash_temperature_isots6336222018(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingFlashTemperatureISOTS6336222018

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_safety_factor_isotr1514412010(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorISOTR1514412010

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_safety_factor_isotr1514412014(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorISOTR1514412014

        if temp is None:
            return ""

        return temp

    @property
    def micropitting_safety_factor_isots6336222018(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactorISOTS6336222018

        if temp is None:
            return ""

        return temp

    @property
    def minimum_lubricant_film_thickness_isotr1514412010(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThicknessISOTR1514412010

        if temp is None:
            return ""

        return temp

    @property
    def minimum_lubricant_film_thickness_isotr1514412014(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThicknessISOTR1514412014

        if temp is None:
            return ""

        return temp

    @property
    def minimum_lubricant_film_thickness_isots6336222018(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThicknessISOTS6336222018

        if temp is None:
            return ""

        return temp

    @property
    def pressure_velocity_pv(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureVelocityPV

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_contact_temperature_agma925a03(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureAGMA925A03

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_contact_temperature_agma925b22(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureAGMA925B22

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_contact_temperature_din399041987(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureDIN399041987

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_contact_temperature_isotr1398912000(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureISOTR1398912000

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_contact_temperature_isots6336202017(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureISOTS6336202017

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_contact_temperature_isots6336202022(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingContactTemperatureISOTS6336202022

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_flash_temperature_agma925a03(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureAGMA925A03

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_flash_temperature_agma925b22(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureAGMA925B22

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_flash_temperature_din399041987(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureDIN399041987

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_flash_temperature_isotr1398912000(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureISOTR1398912000

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_flash_temperature_isots6336202017(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureISOTS6336202017

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_flash_temperature_isots6336202022(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingFlashTemperatureISOTS6336202022

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_safety_factor_agma925a03(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorAGMA925A03

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_safety_factor_agma925b22(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorAGMA925B22

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_safety_factor_din399041987(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorDIN399041987

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_safety_factor_isotr1398912000(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorISOTR1398912000

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_safety_factor_isots6336202017(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorISOTS6336202017

        if temp is None:
            return ""

        return temp

    @property
    def scuffing_safety_factor_isots6336202022(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorISOTS6336202022

        if temp is None:
            return ""

        return temp

    @property
    def sliding_power_loss(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingPowerLoss

        if temp is None:
            return ""

        return temp

    @property
    def sliding_velocity(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return ""

        return temp

    @property
    def specific_lubricant_film_thickness_isotr1514412010(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLubricantFilmThicknessISOTR1514412010

        if temp is None:
            return ""

        return temp

    @property
    def specific_lubricant_film_thickness_isotr1514412014(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLubricantFilmThicknessISOTR1514412014

        if temp is None:
            return ""

        return temp

    @property
    def specific_lubricant_film_thickness_isots6336222018(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLubricantFilmThicknessISOTS6336222018

        if temp is None:
            return ""

        return temp

    @property
    def total_deflection_for_mesh(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDeflectionForMesh

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearWorstLTCAContactChartDataAsTextFile._Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile":
        return self._Cast_CylindricalGearWorstLTCAContactChartDataAsTextFile(self)
