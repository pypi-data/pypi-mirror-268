"""CustomReportNamedItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportNamedItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportNamedItem",)


Self = TypeVar("Self", bound="CustomReportNamedItem")


class CustomReportNamedItem(_1778.CustomReportNameableItem):
    """CustomReportNamedItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMED_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportNamedItem")

    class _Cast_CustomReportNamedItem:
        """Special nested class for casting CustomReportNamedItem to subclasses."""

        def __init__(
            self: "CustomReportNamedItem._Cast_CustomReportNamedItem",
            parent: "CustomReportNamedItem",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportNamedItem._Cast_CustomReportNamedItem",
        ) -> "_1778.CustomReportNameableItem":
            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportNamedItem._Cast_CustomReportNamedItem",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_named_item(
            self: "CustomReportNamedItem._Cast_CustomReportNamedItem",
        ) -> "CustomReportNamedItem":
            return self._parent

        def __getattr__(
            self: "CustomReportNamedItem._Cast_CustomReportNamedItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportNamedItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomReportNamedItem._Cast_CustomReportNamedItem":
        return self._Cast_CustomReportNamedItem(self)
