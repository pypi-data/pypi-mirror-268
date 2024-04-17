"""CreateConnectedComponentOptions"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.system_model import _2211
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CREATE_CONNECTED_COMPONENT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "CreateConnectedComponentOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("CreateConnectedComponentOptions",)


Self = TypeVar("Self", bound="CreateConnectedComponentOptions")


class CreateConnectedComponentOptions(_0.APIBase):
    """CreateConnectedComponentOptions

    This is a mastapy class.
    """

    TYPE = _CREATE_CONNECTED_COMPONENT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CreateConnectedComponentOptions")

    class _Cast_CreateConnectedComponentOptions:
        """Special nested class for casting CreateConnectedComponentOptions to subclasses."""

        def __init__(
            self: "CreateConnectedComponentOptions._Cast_CreateConnectedComponentOptions",
            parent: "CreateConnectedComponentOptions",
        ):
            self._parent = parent

        @property
        def create_connected_component_options(
            self: "CreateConnectedComponentOptions._Cast_CreateConnectedComponentOptions",
        ) -> "CreateConnectedComponentOptions":
            return self._parent

        def __getattr__(
            self: "CreateConnectedComponentOptions._Cast_CreateConnectedComponentOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CreateConnectedComponentOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DesignEntityId":
        """EnumWithSelectedValue[mastapy.system_model.DesignEntityId]"""
        temp = self.wrapped.ComponentType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DesignEntityId.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @component_type.setter
    @enforce_parameter_types
    def component_type(self: Self, value: "_2211.DesignEntityId"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DesignEntityId.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ComponentType = value

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

    def create_component(self: Self):
        """Method does not return."""
        self.wrapped.CreateComponent()

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
    ) -> "CreateConnectedComponentOptions._Cast_CreateConnectedComponentOptions":
        return self._Cast_CreateConnectedComponentOptions(self)
