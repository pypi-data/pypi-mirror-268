"""SystemDirectoryPopulator"""

from __future__ import annotations

from typing import TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility import _1607
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DIRECTORY_POPULATOR = python_net_import(
    "SMT.MastaAPI.Utility", "SystemDirectoryPopulator"
)


__docformat__ = "restructuredtext en"
__all__ = ("SystemDirectoryPopulator",)


Self = TypeVar("Self", bound="SystemDirectoryPopulator")


class SystemDirectoryPopulator(_0.APIBase):
    """SystemDirectoryPopulator

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DIRECTORY_POPULATOR

    class SetupFrom(Enum):
        """SetupFrom is a nested enum."""

        @classmethod
        def type_(cls):
            return _SYSTEM_DIRECTORY_POPULATOR.SetupFrom

        DONT_COPY = 0
        LATEST_VERSION = 1
        SPECIFIED_VERSION = 2

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    SetupFrom.__setattr__ = __enum_setattr
    SetupFrom.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemDirectoryPopulator")

    class _Cast_SystemDirectoryPopulator:
        """Special nested class for casting SystemDirectoryPopulator to subclasses."""

        def __init__(
            self: "SystemDirectoryPopulator._Cast_SystemDirectoryPopulator",
            parent: "SystemDirectoryPopulator",
        ):
            self._parent = parent

        @property
        def system_directory_populator(
            self: "SystemDirectoryPopulator._Cast_SystemDirectoryPopulator",
        ) -> "SystemDirectoryPopulator":
            return self._parent

        def __getattr__(
            self: "SystemDirectoryPopulator._Cast_SystemDirectoryPopulator", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemDirectoryPopulator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def copy_from(self: Self) -> "SystemDirectoryPopulator.SetupFrom":
        """mastapy.utility.SystemDirectoryPopulator.SetupFrom"""
        temp = self.wrapped.CopyFrom

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.SystemDirectoryPopulator+SetupFrom"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.SystemDirectoryPopulator.SystemDirectoryPopulator",
            "SetupFrom",
        )(value)

    @copy_from.setter
    @enforce_parameter_types
    def copy_from(self: Self, value: "SystemDirectoryPopulator.SetupFrom"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.SystemDirectoryPopulator+SetupFrom"
        )
        self.wrapped.CopyFrom = value

    @property
    def selected_version(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_SystemDirectory":
        """ListWithSelectedItem[mastapy.utility.SystemDirectory]"""
        temp = self.wrapped.SelectedVersion

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_SystemDirectory",
        )(temp)

    @selected_version.setter
    @enforce_parameter_types
    def selected_version(self: Self, value: "_1607.SystemDirectory"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_SystemDirectory.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_SystemDirectory.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectedVersion = value

    @property
    def current_version(self: Self) -> "_1607.SystemDirectory":
        """mastapy.utility.SystemDirectory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentVersion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def version_to_copy(self: Self) -> "_1607.SystemDirectory":
        """mastapy.utility.SystemDirectory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VersionToCopy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    ) -> "SystemDirectoryPopulator._Cast_SystemDirectoryPopulator":
        return self._Cast_SystemDirectoryPopulator(self)
