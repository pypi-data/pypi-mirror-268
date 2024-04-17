"""CustomTable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE = python_net_import("SMT.MastaAPI.Utility.Report", "CustomTable")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1039
    from mastapy.utility_gui.charts import _1862
    from mastapy.utility.report import _1777, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomTable",)


Self = TypeVar("Self", bound="CustomTable")


class CustomTable(_1776.CustomReportMultiPropertyItem["_1785.CustomRow"]):
    """CustomTable

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomTable")

    class _Cast_CustomTable:
        """Special nested class for casting CustomTable to subclasses."""

        def __init__(self: "CustomTable._Cast_CustomTable", parent: "CustomTable"):
            self._parent = parent

        @property
        def custom_report_multi_property_item(
            self: "CustomTable._Cast_CustomTable",
        ) -> "_1776.CustomReportMultiPropertyItem":
            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomTable._Cast_CustomTable",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomTable._Cast_CustomTable",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomTable._Cast_CustomTable",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomTable._Cast_CustomTable",
        ) -> "_1039.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1039

            return self._parent._cast(_1039.CylindricalGearTableWithMGCharts)

        @property
        def custom_table_and_chart(
            self: "CustomTable._Cast_CustomTable",
        ) -> "_1862.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1862

            return self._parent._cast(_1862.CustomTableAndChart)

        @property
        def custom_table(self: "CustomTable._Cast_CustomTable") -> "CustomTable":
            return self._parent

        def __getattr__(self: "CustomTable._Cast_CustomTable", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomTable.TYPE"):
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
    def cast_to(self: Self) -> "CustomTable._Cast_CustomTable":
        return self._Cast_CustomTable(self)
