"""ShaftProfile"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_PROFILE = python_net_import("SMT.MastaAPI.Shafts", "ShaftProfile")

if TYPE_CHECKING:
    from mastapy.shafts import _31


__docformat__ = "restructuredtext en"
__all__ = ("ShaftProfile",)


Self = TypeVar("Self", bound="ShaftProfile")


class ShaftProfile(_0.APIBase):
    """ShaftProfile

    This is a mastapy class.
    """

    TYPE = _SHAFT_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftProfile")

    class _Cast_ShaftProfile:
        """Special nested class for casting ShaftProfile to subclasses."""

        def __init__(self: "ShaftProfile._Cast_ShaftProfile", parent: "ShaftProfile"):
            self._parent = parent

        @property
        def shaft_profile(self: "ShaftProfile._Cast_ShaftProfile") -> "ShaftProfile":
            return self._parent

        def __getattr__(self: "ShaftProfile._Cast_ShaftProfile", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def points(self: Self) -> "List[_31.ShaftProfilePoint]":
        """List[mastapy.shafts.ShaftProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Points

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

    def add(self: Self):
        """Method does not return."""
        self.wrapped.Add()

    def add_for_context_menu(self: Self):
        """Method does not return."""
        self.wrapped.AddForContextMenu()

    def import_from_clipboard(self: Self):
        """Method does not return."""
        self.wrapped.ImportFromClipboard()

    @enforce_parameter_types
    def add_profile_point(self: Self, offset: "float", diameter: "float"):
        """Method does not return.

        Args:
            offset (float)
            diameter (float)
        """
        offset = float(offset)
        diameter = float(diameter)
        self.wrapped.AddProfilePoint(
            offset if offset else 0.0, diameter if diameter else 0.0
        )

    def clear(self: Self):
        """Method does not return."""
        self.wrapped.Clear()

    def make_valid(self: Self):
        """Method does not return."""
        self.wrapped.MakeValid()

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
    def cast_to(self: Self) -> "ShaftProfile._Cast_ShaftProfile":
        return self._Cast_ShaftProfile(self)
