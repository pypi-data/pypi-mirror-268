"""GearLTCAContactChartDataAsTextFile"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE = python_net_import(
    "SMT.MastaAPI.Gears.Cylindrical", "GearLTCAContactChartDataAsTextFile"
)

if TYPE_CHECKING:
    from mastapy.gears.cylindrical import _1214


__docformat__ = "restructuredtext en"
__all__ = ("GearLTCAContactChartDataAsTextFile",)


Self = TypeVar("Self", bound="GearLTCAContactChartDataAsTextFile")


class GearLTCAContactChartDataAsTextFile(_0.APIBase):
    """GearLTCAContactChartDataAsTextFile

    This is a mastapy class.
    """

    TYPE = _GEAR_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearLTCAContactChartDataAsTextFile")

    class _Cast_GearLTCAContactChartDataAsTextFile:
        """Special nested class for casting GearLTCAContactChartDataAsTextFile to subclasses."""

        def __init__(
            self: "GearLTCAContactChartDataAsTextFile._Cast_GearLTCAContactChartDataAsTextFile",
            parent: "GearLTCAContactChartDataAsTextFile",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_ltca_contact_chart_data_as_text_file(
            self: "GearLTCAContactChartDataAsTextFile._Cast_GearLTCAContactChartDataAsTextFile",
        ) -> "_1214.CylindricalGearLTCAContactChartDataAsTextFile":
            from mastapy.gears.cylindrical import _1214

            return self._parent._cast(
                _1214.CylindricalGearLTCAContactChartDataAsTextFile
            )

        @property
        def gear_ltca_contact_chart_data_as_text_file(
            self: "GearLTCAContactChartDataAsTextFile._Cast_GearLTCAContactChartDataAsTextFile",
        ) -> "GearLTCAContactChartDataAsTextFile":
            return self._parent

        def __getattr__(
            self: "GearLTCAContactChartDataAsTextFile._Cast_GearLTCAContactChartDataAsTextFile",
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
        self: Self, instance_to_wrap: "GearLTCAContactChartDataAsTextFile.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "GearLTCAContactChartDataAsTextFile._Cast_GearLTCAContactChartDataAsTextFile":
        return self._Cast_GearLTCAContactChartDataAsTextFile(self)
