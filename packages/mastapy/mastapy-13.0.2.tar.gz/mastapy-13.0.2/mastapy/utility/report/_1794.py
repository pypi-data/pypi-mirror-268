"""UserTextRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_TEXT_ROW = python_net_import("SMT.MastaAPI.Utility.Report", "UserTextRow")

if TYPE_CHECKING:
    from mastapy.utility.report import _1792, _1780


__docformat__ = "restructuredtext en"
__all__ = ("UserTextRow",)


Self = TypeVar("Self", bound="UserTextRow")


class UserTextRow(_1785.CustomRow):
    """UserTextRow

    This is a mastapy class.
    """

    TYPE = _USER_TEXT_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UserTextRow")

    class _Cast_UserTextRow:
        """Special nested class for casting UserTextRow to subclasses."""

        def __init__(self: "UserTextRow._Cast_UserTextRow", parent: "UserTextRow"):
            self._parent = parent

        @property
        def custom_row(self: "UserTextRow._Cast_UserTextRow") -> "_1785.CustomRow":
            return self._parent._cast(_1785.CustomRow)

        @property
        def custom_report_property_item(
            self: "UserTextRow._Cast_UserTextRow",
        ) -> "_1780.CustomReportPropertyItem":
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomReportPropertyItem)

        @property
        def user_text_row(self: "UserTextRow._Cast_UserTextRow") -> "UserTextRow":
            return self._parent

        def __getattr__(self: "UserTextRow._Cast_UserTextRow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UserTextRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_text(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AdditionalText

        if temp is None:
            return ""

        return temp

    @additional_text.setter
    @enforce_parameter_types
    def additional_text(self: Self, value: "str"):
        self.wrapped.AdditionalText = str(value) if value is not None else ""

    @property
    def heading_size(self: Self) -> "_1792.HeadingSize":
        """mastapy.utility.report.HeadingSize"""
        temp = self.wrapped.HeadingSize

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Report.HeadingSize"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1792", "HeadingSize"
        )(value)

    @heading_size.setter
    @enforce_parameter_types
    def heading_size(self: Self, value: "_1792.HeadingSize"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.HeadingSize"
        )
        self.wrapped.HeadingSize = value

    @property
    def is_heading(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsHeading

        if temp is None:
            return False

        return temp

    @is_heading.setter
    @enforce_parameter_types
    def is_heading(self: Self, value: "bool"):
        self.wrapped.IsHeading = bool(value) if value is not None else False

    @property
    def show_additional_text(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAdditionalText

        if temp is None:
            return False

        return temp

    @show_additional_text.setter
    @enforce_parameter_types
    def show_additional_text(self: Self, value: "bool"):
        self.wrapped.ShowAdditionalText = bool(value) if value is not None else False

    @property
    def text(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Text

        if temp is None:
            return ""

        return temp

    @text.setter
    @enforce_parameter_types
    def text(self: Self, value: "str"):
        self.wrapped.Text = str(value) if value is not None else ""

    @property
    def cast_to(self: Self) -> "UserTextRow._Cast_UserTextRow":
        return self._Cast_UserTextRow(self)
