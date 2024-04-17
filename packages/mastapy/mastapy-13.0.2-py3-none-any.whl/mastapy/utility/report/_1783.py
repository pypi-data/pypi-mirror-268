"""CustomReportTabs"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1772
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_TABS = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportTabs"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1773, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportTabs",)


Self = TypeVar("Self", bound="CustomReportTabs")


class CustomReportTabs(
    _1772.CustomReportItemContainerCollection["_1782.CustomReportTab"]
):
    """CustomReportTabs

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_TABS

    class ReportLayoutOrientation(Enum):
        """ReportLayoutOrientation is a nested enum."""

        @classmethod
        def type_(cls):
            return _CUSTOM_REPORT_TABS.ReportLayoutOrientation

        HORIZONTAL = 0
        VERTICAL = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    ReportLayoutOrientation.__setattr__ = __enum_setattr
    ReportLayoutOrientation.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportTabs")

    class _Cast_CustomReportTabs:
        """Special nested class for casting CustomReportTabs to subclasses."""

        def __init__(
            self: "CustomReportTabs._Cast_CustomReportTabs", parent: "CustomReportTabs"
        ):
            self._parent = parent

        @property
        def custom_report_item_container_collection(
            self: "CustomReportTabs._Cast_CustomReportTabs",
        ) -> "_1772.CustomReportItemContainerCollection":
            return self._parent._cast(_1772.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportTabs._Cast_CustomReportTabs",
        ) -> "_1773.CustomReportItemContainerCollectionBase":
            from mastapy.utility.report import _1773

            return self._parent._cast(_1773.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item(
            self: "CustomReportTabs._Cast_CustomReportTabs",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_tabs(
            self: "CustomReportTabs._Cast_CustomReportTabs",
        ) -> "CustomReportTabs":
            return self._parent

        def __getattr__(self: "CustomReportTabs._Cast_CustomReportTabs", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportTabs.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMainReportItem

        if temp is None:
            return False

        return temp

    @is_main_report_item.setter
    @enforce_parameter_types
    def is_main_report_item(self: Self, value: "bool"):
        self.wrapped.IsMainReportItem = bool(value) if value is not None else False

    @property
    def number_of_tabs(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTabs

        if temp is None:
            return 0

        return temp

    @number_of_tabs.setter
    @enforce_parameter_types
    def number_of_tabs(self: Self, value: "int"):
        self.wrapped.NumberOfTabs = int(value) if value is not None else 0

    @property
    def scroll_content(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ScrollContent

        if temp is None:
            return False

        return temp

    @scroll_content.setter
    @enforce_parameter_types
    def scroll_content(self: Self, value: "bool"):
        self.wrapped.ScrollContent = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomReportTabs._Cast_CustomReportTabs":
        return self._Cast_CustomReportTabs(self)
