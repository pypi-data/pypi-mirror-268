"""GaussKronrodOptions"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GAUSS_KRONROD_OPTIONS = python_net_import(
    "SMT.MastaAPI.MathUtility.Integration", "GaussKronrodOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("GaussKronrodOptions",)


Self = TypeVar("Self", bound="GaussKronrodOptions")


class GaussKronrodOptions(_0.APIBase):
    """GaussKronrodOptions

    This is a mastapy class.
    """

    TYPE = _GAUSS_KRONROD_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GaussKronrodOptions")

    class _Cast_GaussKronrodOptions:
        """Special nested class for casting GaussKronrodOptions to subclasses."""

        def __init__(
            self: "GaussKronrodOptions._Cast_GaussKronrodOptions",
            parent: "GaussKronrodOptions",
        ):
            self._parent = parent

        @property
        def gauss_kronrod_options(
            self: "GaussKronrodOptions._Cast_GaussKronrodOptions",
        ) -> "GaussKronrodOptions":
            return self._parent

        def __getattr__(
            self: "GaussKronrodOptions._Cast_GaussKronrodOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GaussKronrodOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_sample_points_when_finding_zero_regions(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSamplePointsWhenFindingZeroRegions

        if temp is None:
            return 0

        return temp

    @number_of_sample_points_when_finding_zero_regions.setter
    @enforce_parameter_types
    def number_of_sample_points_when_finding_zero_regions(self: Self, value: "int"):
        self.wrapped.NumberOfSamplePointsWhenFindingZeroRegions = (
            int(value) if value is not None else 0
        )

    @property
    def pre_scan_domains_for_endpoint_zero_regions(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PreScanDomainsForEndpointZeroRegions

        if temp is None:
            return False

        return temp

    @pre_scan_domains_for_endpoint_zero_regions.setter
    @enforce_parameter_types
    def pre_scan_domains_for_endpoint_zero_regions(self: Self, value: "bool"):
        self.wrapped.PreScanDomainsForEndpointZeroRegions = (
            bool(value) if value is not None else False
        )

    @property
    def precision_for_refining_zero_regions(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PrecisionForRefiningZeroRegions

        if temp is None:
            return 0.0

        return temp

    @precision_for_refining_zero_regions.setter
    @enforce_parameter_types
    def precision_for_refining_zero_regions(self: Self, value: "float"):
        self.wrapped.PrecisionForRefiningZeroRegions = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_advanced_zero_region_detection_when_subdividing_domains(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedZeroRegionDetectionWhenSubdividingDomains

        if temp is None:
            return False

        return temp

    @use_advanced_zero_region_detection_when_subdividing_domains.setter
    @enforce_parameter_types
    def use_advanced_zero_region_detection_when_subdividing_domains(
        self: Self, value: "bool"
    ):
        self.wrapped.UseAdvancedZeroRegionDetectionWhenSubdividingDomains = (
            bool(value) if value is not None else False
        )

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
    def cast_to(self: Self) -> "GaussKronrodOptions._Cast_GaussKronrodOptions":
        return self._Cast_GaussKronrodOptions(self)
