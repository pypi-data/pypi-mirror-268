"""CustomSubReport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_SUB_REPORT = python_net_import("SMT.MastaAPI.Utility.Report", "CustomSubReport")

if TYPE_CHECKING:
    from mastapy.utility.report import _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomSubReport",)


Self = TypeVar("Self", bound="CustomSubReport")


class CustomSubReport(_1767.CustomReportDefinitionItem):
    """CustomSubReport

    This is a mastapy class.
    """

    TYPE = _CUSTOM_SUB_REPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomSubReport")

    class _Cast_CustomSubReport:
        """Special nested class for casting CustomSubReport to subclasses."""

        def __init__(
            self: "CustomSubReport._Cast_CustomSubReport", parent: "CustomSubReport"
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "CustomSubReport._Cast_CustomSubReport",
        ) -> "_1767.CustomReportDefinitionItem":
            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomSubReport._Cast_CustomSubReport",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomSubReport._Cast_CustomSubReport",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_sub_report(
            self: "CustomSubReport._Cast_CustomSubReport",
        ) -> "CustomSubReport":
            return self._parent

        def __getattr__(self: "CustomSubReport._Cast_CustomSubReport", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomSubReport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_new_page(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateNewPage

        if temp is None:
            return False

        return temp

    @create_new_page.setter
    @enforce_parameter_types
    def create_new_page(self: Self, value: "bool"):
        self.wrapped.CreateNewPage = bool(value) if value is not None else False

    @property
    def is_read_only_in_editor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsReadOnlyInEditor

        if temp is None:
            return False

        return temp

    @is_read_only_in_editor.setter
    @enforce_parameter_types
    def is_read_only_in_editor(self: Self, value: "bool"):
        self.wrapped.IsReadOnlyInEditor = bool(value) if value is not None else False

    @property
    def scale(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    @enforce_parameter_types
    def scale(self: Self, value: "float"):
        self.wrapped.Scale = float(value) if value is not None else 0.0

    @property
    def show_report_edit_toolbar(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowReportEditToolbar

        if temp is None:
            return False

        return temp

    @show_report_edit_toolbar.setter
    @enforce_parameter_types
    def show_report_edit_toolbar(self: Self, value: "bool"):
        self.wrapped.ShowReportEditToolbar = bool(value) if value is not None else False

    @property
    def show_table_of_contents(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTableOfContents

        if temp is None:
            return False

        return temp

    @show_table_of_contents.setter
    @enforce_parameter_types
    def show_table_of_contents(self: Self, value: "bool"):
        self.wrapped.ShowTableOfContents = bool(value) if value is not None else False

    @property
    def show_as_report_in_the_editor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAsReportInTheEditor

        if temp is None:
            return False

        return temp

    @show_as_report_in_the_editor.setter
    @enforce_parameter_types
    def show_as_report_in_the_editor(self: Self, value: "bool"):
        self.wrapped.ShowAsReportInTheEditor = (
            bool(value) if value is not None else False
        )

    def report_source(self: Self):
        """Method does not return."""
        self.wrapped.ReportSource()

    @property
    def cast_to(self: Self) -> "CustomSubReport._Cast_CustomSubReport":
        return self._Cast_CustomSubReport(self)
