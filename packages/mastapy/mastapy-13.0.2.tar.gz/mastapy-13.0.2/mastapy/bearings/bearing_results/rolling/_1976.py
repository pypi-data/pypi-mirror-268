"""DIN7322010Results"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN7322010_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "DIN7322010Results"
)


__docformat__ = "restructuredtext en"
__all__ = ("DIN7322010Results",)


Self = TypeVar("Self", bound="DIN7322010Results")


class DIN7322010Results(_0.APIBase):
    """DIN7322010Results

    This is a mastapy class.
    """

    TYPE = _DIN7322010_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DIN7322010Results")

    class _Cast_DIN7322010Results:
        """Special nested class for casting DIN7322010Results to subclasses."""

        def __init__(
            self: "DIN7322010Results._Cast_DIN7322010Results",
            parent: "DIN7322010Results",
        ):
            self._parent = parent

        @property
        def din7322010_results(
            self: "DIN7322010Results._Cast_DIN7322010Results",
        ) -> "DIN7322010Results":
            return self._parent

        def __getattr__(self: "DIN7322010Results._Cast_DIN7322010Results", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DIN7322010Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_convection_heat_dissipation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AirConvectionHeatDissipation

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def external_cooling_or_heating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalCoolingOrHeating

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def heat_dissipation_capacity_of_bearing_lubrication(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeatDissipationCapacityOfBearingLubrication

        if temp is None:
            return 0.0

        return temp

    @property
    def heat_emitting_reference_surface_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeatEmittingReferenceSurfaceArea

        if temp is None:
            return 0.0

        return temp

    @property
    def limiting_speed_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingSpeedWarning

        if temp is None:
            return ""

        return temp

    @property
    def load_dependent_frictional_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDependentFrictionalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_dip_coefficient_f0_adjustment_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilDipCoefficientF0AdjustmentFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_speed_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceSpeedWarning

        if temp is None:
            return ""

        return temp

    @property
    def required_oil_flow_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredOilFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_dependent_frictional_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedDependentFrictionalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_limiting_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalLimitingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_limiting_speed_f0(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalLimitingSpeedF0

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_limiting_speed_f1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalLimitingSpeedF1

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_reference_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_reference_speed_f0r(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalReferenceSpeedF0r

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_reference_speed_f1r(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalReferenceSpeedF1r

        if temp is None:
            return 0.0

        return temp

    @property
    def total_heat_emitted(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalHeatEmitted

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self: Self) -> "DIN7322010Results._Cast_DIN7322010Results":
        return self._Cast_DIN7322010Results(self)
