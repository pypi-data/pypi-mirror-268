"""CustomReportTab"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_TAB = python_net_import("SMT.MastaAPI.Utility.Report", "CustomReportTab")

if TYPE_CHECKING:
    from mastapy.utility.report import _1771, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportTab",)


Self = TypeVar("Self", bound="CustomReportTab")


class CustomReportTab(_1774.CustomReportItemContainerCollectionItem):
    """CustomReportTab

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_TAB
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportTab")

    class _Cast_CustomReportTab:
        """Special nested class for casting CustomReportTab to subclasses."""

        def __init__(
            self: "CustomReportTab._Cast_CustomReportTab", parent: "CustomReportTab"
        ):
            self._parent = parent

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportTab._Cast_CustomReportTab",
        ) -> "_1774.CustomReportItemContainerCollectionItem":
            return self._parent._cast(_1774.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_item_container(
            self: "CustomReportTab._Cast_CustomReportTab",
        ) -> "_1771.CustomReportItemContainer":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportItemContainer)

        @property
        def custom_report_item(
            self: "CustomReportTab._Cast_CustomReportTab",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_tab(
            self: "CustomReportTab._Cast_CustomReportTab",
        ) -> "CustomReportTab":
            return self._parent

        def __getattr__(self: "CustomReportTab._Cast_CustomReportTab", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportTab.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hide_when_has_no_content(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HideWhenHasNoContent

        if temp is None:
            return False

        return temp

    @hide_when_has_no_content.setter
    @enforce_parameter_types
    def hide_when_has_no_content(self: Self, value: "bool"):
        self.wrapped.HideWhenHasNoContent = bool(value) if value is not None else False

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def show_if_empty(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowIfEmpty

        if temp is None:
            return False

        return temp

    @show_if_empty.setter
    @enforce_parameter_types
    def show_if_empty(self: Self, value: "bool"):
        self.wrapped.ShowIfEmpty = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomReportTab._Cast_CustomReportTab":
        return self._Cast_CustomReportTab(self)
