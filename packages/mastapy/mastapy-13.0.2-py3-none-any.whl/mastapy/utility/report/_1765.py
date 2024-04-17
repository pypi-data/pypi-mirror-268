"""CustomReportColumn"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_COLUMN = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportColumn"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1771, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportColumn",)


Self = TypeVar("Self", bound="CustomReportColumn")


class CustomReportColumn(_1774.CustomReportItemContainerCollectionItem):
    """CustomReportColumn

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_COLUMN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportColumn")

    class _Cast_CustomReportColumn:
        """Special nested class for casting CustomReportColumn to subclasses."""

        def __init__(
            self: "CustomReportColumn._Cast_CustomReportColumn",
            parent: "CustomReportColumn",
        ):
            self._parent = parent

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportColumn._Cast_CustomReportColumn",
        ) -> "_1774.CustomReportItemContainerCollectionItem":
            return self._parent._cast(_1774.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_item_container(
            self: "CustomReportColumn._Cast_CustomReportColumn",
        ) -> "_1771.CustomReportItemContainer":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportItemContainer)

        @property
        def custom_report_item(
            self: "CustomReportColumn._Cast_CustomReportColumn",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_column(
            self: "CustomReportColumn._Cast_CustomReportColumn",
        ) -> "CustomReportColumn":
            return self._parent

        def __getattr__(self: "CustomReportColumn._Cast_CustomReportColumn", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportColumn.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auto_width(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AutoWidth

        if temp is None:
            return False

        return temp

    @auto_width.setter
    @enforce_parameter_types
    def auto_width(self: Self, value: "bool"):
        self.wrapped.AutoWidth = bool(value) if value is not None else False

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "CustomReportColumn._Cast_CustomReportColumn":
        return self._Cast_CustomReportColumn(self)
