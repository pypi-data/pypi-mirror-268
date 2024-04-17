"""CustomReportHtmlItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_HTML_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportHtmlItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportHtmlItem",)


Self = TypeVar("Self", bound="CustomReportHtmlItem")


class CustomReportHtmlItem(_1767.CustomReportDefinitionItem):
    """CustomReportHtmlItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_HTML_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportHtmlItem")

    class _Cast_CustomReportHtmlItem:
        """Special nested class for casting CustomReportHtmlItem to subclasses."""

        def __init__(
            self: "CustomReportHtmlItem._Cast_CustomReportHtmlItem",
            parent: "CustomReportHtmlItem",
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "CustomReportHtmlItem._Cast_CustomReportHtmlItem",
        ) -> "_1767.CustomReportDefinitionItem":
            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomReportHtmlItem._Cast_CustomReportHtmlItem",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportHtmlItem._Cast_CustomReportHtmlItem",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_html_item(
            self: "CustomReportHtmlItem._Cast_CustomReportHtmlItem",
        ) -> "CustomReportHtmlItem":
            return self._parent

        def __getattr__(
            self: "CustomReportHtmlItem._Cast_CustomReportHtmlItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportHtmlItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomReportHtmlItem._Cast_CustomReportHtmlItem":
        return self._Cast_CustomReportHtmlItem(self)
