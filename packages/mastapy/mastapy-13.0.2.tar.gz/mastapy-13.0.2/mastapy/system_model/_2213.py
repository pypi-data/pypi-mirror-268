"""DutyCycleImporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results.load_case_groups import _5671
from mastapy._internal import conversion
from mastapy.system_model.part_model import _2478, _2479
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_IMPORTER = python_net_import(
    "SMT.MastaAPI.SystemModel", "DutyCycleImporter"
)

if TYPE_CHECKING:
    from mastapy.system_model import _2214, _2218


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleImporter",)


Self = TypeVar("Self", bound="DutyCycleImporter")


class DutyCycleImporter(_0.APIBase):
    """DutyCycleImporter

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_IMPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleImporter")

    class _Cast_DutyCycleImporter:
        """Special nested class for casting DutyCycleImporter to subclasses."""

        def __init__(
            self: "DutyCycleImporter._Cast_DutyCycleImporter",
            parent: "DutyCycleImporter",
        ):
            self._parent = parent

        @property
        def duty_cycle_importer(
            self: "DutyCycleImporter._Cast_DutyCycleImporter",
        ) -> "DutyCycleImporter":
            return self._parent

        def __getattr__(self: "DutyCycleImporter._Cast_DutyCycleImporter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycleImporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_state_destinations(
        self: Self,
    ) -> "List[_2214.DutyCycleImporterDesignEntityMatch[_5671.DesignState]]":
        """List[mastapy.system_model.DutyCycleImporterDesignEntityMatch[mastapy.system_model.analyses_and_results.load_case_groups.DesignState]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStateDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def duty_cycles_to_import(self: Self) -> "List[_2218.IncludeDutyCycleOption]":
        """List[mastapy.system_model.IncludeDutyCycleOption]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCyclesToImport

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_load_destinations(
        self: Self,
    ) -> "List[_2214.DutyCycleImporterDesignEntityMatch[_2478.PointLoad]]":
        """List[mastapy.system_model.DutyCycleImporterDesignEntityMatch[mastapy.system_model.part_model.PointLoad]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointLoadDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_load_destinations(
        self: Self,
    ) -> "List[_2214.DutyCycleImporterDesignEntityMatch[_2479.PowerLoad]]":
        """List[mastapy.system_model.DutyCycleImporterDesignEntityMatch[mastapy.system_model.part_model.PowerLoad]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoadDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def cast_to(self: Self) -> "DutyCycleImporter._Cast_DutyCycleImporter":
        return self._Cast_DutyCycleImporter(self)
