"""CylindricalGearLTCAContactChartDataAsTextFile"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.cylindrical import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE = python_net_import(
    "SMT.MastaAPI.Gears.Cylindrical", "CylindricalGearLTCAContactChartDataAsTextFile"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLTCAContactChartDataAsTextFile",)


Self = TypeVar("Self", bound="CylindricalGearLTCAContactChartDataAsTextFile")


class CylindricalGearLTCAContactChartDataAsTextFile(
    _1218.GearLTCAContactChartDataAsTextFile
):
    """CylindricalGearLTCAContactChartDataAsTextFile

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearLTCAContactChartDataAsTextFile"
    )

    class _Cast_CylindricalGearLTCAContactChartDataAsTextFile:
        """Special nested class for casting CylindricalGearLTCAContactChartDataAsTextFile to subclasses."""

        def __init__(
            self: "CylindricalGearLTCAContactChartDataAsTextFile._Cast_CylindricalGearLTCAContactChartDataAsTextFile",
            parent: "CylindricalGearLTCAContactChartDataAsTextFile",
        ):
            self._parent = parent

        @property
        def gear_ltca_contact_chart_data_as_text_file(
            self: "CylindricalGearLTCAContactChartDataAsTextFile._Cast_CylindricalGearLTCAContactChartDataAsTextFile",
        ) -> "_1218.GearLTCAContactChartDataAsTextFile":
            return self._parent._cast(_1218.GearLTCAContactChartDataAsTextFile)

        @property
        def cylindrical_gear_ltca_contact_chart_data_as_text_file(
            self: "CylindricalGearLTCAContactChartDataAsTextFile._Cast_CylindricalGearLTCAContactChartDataAsTextFile",
        ) -> "CylindricalGearLTCAContactChartDataAsTextFile":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLTCAContactChartDataAsTextFile._Cast_CylindricalGearLTCAContactChartDataAsTextFile",
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
        instance_to_wrap: "CylindricalGearLTCAContactChartDataAsTextFile.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearLTCAContactChartDataAsTextFile._Cast_CylindricalGearLTCAContactChartDataAsTextFile":
        return self._Cast_CylindricalGearLTCAContactChartDataAsTextFile(self)
