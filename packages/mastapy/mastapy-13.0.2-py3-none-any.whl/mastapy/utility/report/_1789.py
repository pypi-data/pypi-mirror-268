"""DynamicCustomReportItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility.report import _1778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_CUSTOM_REPORT_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "DynamicCustomReportItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1770


__docformat__ = "restructuredtext en"
__all__ = ("DynamicCustomReportItem",)


Self = TypeVar("Self", bound="DynamicCustomReportItem")


class DynamicCustomReportItem(_1778.CustomReportNameableItem):
    """DynamicCustomReportItem

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_CUSTOM_REPORT_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicCustomReportItem")

    class _Cast_DynamicCustomReportItem:
        """Special nested class for casting DynamicCustomReportItem to subclasses."""

        def __init__(
            self: "DynamicCustomReportItem._Cast_DynamicCustomReportItem",
            parent: "DynamicCustomReportItem",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "DynamicCustomReportItem._Cast_DynamicCustomReportItem",
        ) -> "_1778.CustomReportNameableItem":
            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "DynamicCustomReportItem._Cast_DynamicCustomReportItem",
        ) -> "_1770.CustomReportItem":
            return self._parent._cast(_1770.CustomReportItem)

        @property
        def dynamic_custom_report_item(
            self: "DynamicCustomReportItem._Cast_DynamicCustomReportItem",
        ) -> "DynamicCustomReportItem":
            return self._parent

        def __getattr__(
            self: "DynamicCustomReportItem._Cast_DynamicCustomReportItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicCustomReportItem.TYPE"):
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
    def inner_item(self: Self) -> "_1770.CustomReportItem":
        """mastapy.utility.report.CustomReportItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerItem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "DynamicCustomReportItem._Cast_DynamicCustomReportItem":
        return self._Cast_DynamicCustomReportItem(self)
