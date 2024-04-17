"""CustomReportColumns"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1772
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_COLUMNS = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportColumns"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1773, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportColumns",)


Self = TypeVar("Self", bound="CustomReportColumns")


class CustomReportColumns(
    _1772.CustomReportItemContainerCollection["_1765.CustomReportColumn"]
):
    """CustomReportColumns

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_COLUMNS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportColumns")

    class _Cast_CustomReportColumns:
        """Special nested class for casting CustomReportColumns to subclasses."""

        def __init__(
            self: "CustomReportColumns._Cast_CustomReportColumns",
            parent: "CustomReportColumns",
        ):
            self._parent = parent

        @property
        def custom_report_item_container_collection(
            self: "CustomReportColumns._Cast_CustomReportColumns",
        ) -> "_1772.CustomReportItemContainerCollection":
            return self._parent._cast(_1772.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportColumns._Cast_CustomReportColumns",
        ) -> "_1773.CustomReportItemContainerCollectionBase":
            from mastapy.utility.report import _1773

            return self._parent._cast(_1773.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item(
            self: "CustomReportColumns._Cast_CustomReportColumns",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_columns(
            self: "CustomReportColumns._Cast_CustomReportColumns",
        ) -> "CustomReportColumns":
            return self._parent

        def __getattr__(
            self: "CustomReportColumns._Cast_CustomReportColumns", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportColumns.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_columns(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfColumns

        if temp is None:
            return 0

        return temp

    @number_of_columns.setter
    @enforce_parameter_types
    def number_of_columns(self: Self, value: "int"):
        self.wrapped.NumberOfColumns = int(value) if value is not None else 0

    @property
    def show_adjustable_column_divider(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAdjustableColumnDivider

        if temp is None:
            return False

        return temp

    @show_adjustable_column_divider.setter
    @enforce_parameter_types
    def show_adjustable_column_divider(self: Self, value: "bool"):
        self.wrapped.ShowAdjustableColumnDivider = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "CustomReportColumns._Cast_CustomReportColumns":
        return self._Cast_CustomReportColumns(self)
