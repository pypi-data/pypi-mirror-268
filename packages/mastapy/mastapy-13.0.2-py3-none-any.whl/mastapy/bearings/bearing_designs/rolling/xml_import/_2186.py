"""XmlBearingTypeMapping"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_XML_BEARING_TYPE_MAPPING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport", "XmlBearingTypeMapping"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling.xml_import import _2184, _2183


__docformat__ = "restructuredtext en"
__all__ = ("XmlBearingTypeMapping",)


Self = TypeVar("Self", bound="XmlBearingTypeMapping")


class XmlBearingTypeMapping(_0.APIBase):
    """XmlBearingTypeMapping

    This is a mastapy class.
    """

    TYPE = _XML_BEARING_TYPE_MAPPING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_XmlBearingTypeMapping")

    class _Cast_XmlBearingTypeMapping:
        """Special nested class for casting XmlBearingTypeMapping to subclasses."""

        def __init__(
            self: "XmlBearingTypeMapping._Cast_XmlBearingTypeMapping",
            parent: "XmlBearingTypeMapping",
        ):
            self._parent = parent

        @property
        def xml_bearing_type_mapping(
            self: "XmlBearingTypeMapping._Cast_XmlBearingTypeMapping",
        ) -> "XmlBearingTypeMapping":
            return self._parent

        def __getattr__(
            self: "XmlBearingTypeMapping._Cast_XmlBearingTypeMapping", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "XmlBearingTypeMapping.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_bearings(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfBearings

        if temp is None:
            return 0

        return temp

    @property
    def number_of_unassigned_variables(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfUnassignedVariables

        if temp is None:
            return 0

        return temp

    @property
    def number_of_variables(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfVariables

        if temp is None:
            return 0

        return temp

    @property
    def source_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SourceName

        if temp is None:
            return ""

        return temp

    @property
    def target_type(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.TargetType

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @target_type.setter
    @enforce_parameter_types
    def target_type(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.TargetType = value

    @property
    def files(self: Self) -> "List[_2184.BearingImportFile]":
        """List[mastapy.bearings.bearing_designs.rolling.xml_import.BearingImportFile]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Files

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def variables(self: Self) -> "List[_2183.AbstractXmlVariableAssignment]":
        """List[mastapy.bearings.bearing_designs.rolling.xml_import.AbstractXmlVariableAssignment]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Variables

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

    def import_all(self: Self):
        """Method does not return."""
        self.wrapped.ImportAll()

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
    def cast_to(self: Self) -> "XmlBearingTypeMapping._Cast_XmlBearingTypeMapping":
        return self._Cast_XmlBearingTypeMapping(self)
