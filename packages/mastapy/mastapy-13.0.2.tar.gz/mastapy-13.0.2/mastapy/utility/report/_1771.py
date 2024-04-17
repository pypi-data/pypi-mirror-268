"""CustomReportItemContainer"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainer"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1761, _1765, _1774, _1782


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainer",)


Self = TypeVar("Self", bound="CustomReportItemContainer")


class CustomReportItemContainer(_1770.CustomReportItem):
    """CustomReportItemContainer

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportItemContainer")

    class _Cast_CustomReportItemContainer:
        """Special nested class for casting CustomReportItemContainer to subclasses."""

        def __init__(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
            parent: "CustomReportItemContainer",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1770.CustomReportItem":
            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1761.CustomReport":
            from mastapy.utility.report import _1761

            return self._parent._cast(_1761.CustomReport)

        @property
        def custom_report_column(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1765.CustomReportColumn":
            from mastapy.utility.report import _1765

            return self._parent._cast(_1765.CustomReportColumn)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1774.CustomReportItemContainerCollectionItem":
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_tab(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1782.CustomReportTab":
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.CustomReportTab)

        @property
        def custom_report_item_container(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "CustomReportItemContainer":
            return self._parent

        def __getattr__(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportItemContainer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportItemContainer._Cast_CustomReportItemContainer":
        return self._Cast_CustomReportItemContainer(self)
