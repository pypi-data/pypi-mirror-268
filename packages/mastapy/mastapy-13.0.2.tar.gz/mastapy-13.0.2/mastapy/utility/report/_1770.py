"""CustomReportItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItem"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1039
    from mastapy.utility.report import (
        _1749,
        _1757,
        _1758,
        _1759,
        _1760,
        _1761,
        _1762,
        _1763,
        _1765,
        _1766,
        _1767,
        _1768,
        _1769,
        _1771,
        _1772,
        _1773,
        _1774,
        _1776,
        _1777,
        _1778,
        _1779,
        _1781,
        _1782,
        _1783,
        _1784,
        _1786,
        _1787,
        _1789,
    )
    from mastapy.utility_gui.charts import _1861, _1862
    from mastapy.bearings.bearing_results import _1953, _1954, _1957, _1965
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2857,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4394
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4725,
        _4729,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItem",)


Self = TypeVar("Self", bound="CustomReportItem")


class CustomReportItem(_0.APIBase):
    """CustomReportItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportItem")

    class _Cast_CustomReportItem:
        """Special nested class for casting CustomReportItem to subclasses."""

        def __init__(
            self: "CustomReportItem._Cast_CustomReportItem", parent: "CustomReportItem"
        ):
            self._parent = parent

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1039.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1039

            return self._parent._cast(_1039.CylindricalGearTableWithMGCharts)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1749.AdHocCustomTable":
            from mastapy.utility.report import _1749

            return self._parent._cast(_1749.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1757.CustomChart":
            from mastapy.utility.report import _1757

            return self._parent._cast(_1757.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1758.CustomDrawing":
            from mastapy.utility.report import _1758

            return self._parent._cast(_1758.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1759.CustomGraphic":
            from mastapy.utility.report import _1759

            return self._parent._cast(_1759.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1760.CustomImage":
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomImage)

        @property
        def custom_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1761.CustomReport":
            from mastapy.utility.report import _1761

            return self._parent._cast(_1761.CustomReport)

        @property
        def custom_report_cad_drawing(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1762.CustomReportCadDrawing":
            from mastapy.utility.report import _1762

            return self._parent._cast(_1762.CustomReportCadDrawing)

        @property
        def custom_report_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1763.CustomReportChart":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_column(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1765.CustomReportColumn":
            from mastapy.utility.report import _1765

            return self._parent._cast(_1765.CustomReportColumn)

        @property
        def custom_report_columns(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1766.CustomReportColumns":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.CustomReportColumns)

        @property
        def custom_report_definition_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1767.CustomReportDefinitionItem":
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_horizontal_line(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1768.CustomReportHorizontalLine":
            from mastapy.utility.report import _1768

            return self._parent._cast(_1768.CustomReportHorizontalLine)

        @property
        def custom_report_html_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1769.CustomReportHtmlItem":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportHtmlItem)

        @property
        def custom_report_item_container(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1771.CustomReportItemContainer":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportItemContainer)

        @property
        def custom_report_item_container_collection(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1772.CustomReportItemContainerCollection":
            from mastapy.utility.report import _1772

            return self._parent._cast(_1772.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1773.CustomReportItemContainerCollectionBase":
            from mastapy.utility.report import _1773

            return self._parent._cast(_1773.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1774.CustomReportItemContainerCollectionItem":
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1776.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_named_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1779.CustomReportNamedItem":
            from mastapy.utility.report import _1779

            return self._parent._cast(_1779.CustomReportNamedItem)

        @property
        def custom_report_status_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1781.CustomReportStatusItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportStatusItem)

        @property
        def custom_report_tab(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1782.CustomReportTab":
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.CustomReportTab)

        @property
        def custom_report_tabs(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1783.CustomReportTabs":
            from mastapy.utility.report import _1783

            return self._parent._cast(_1783.CustomReportTabs)

        @property
        def custom_report_text(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1784.CustomReportText":
            from mastapy.utility.report import _1784

            return self._parent._cast(_1784.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1786.CustomSubReport":
            from mastapy.utility.report import _1786

            return self._parent._cast(_1786.CustomSubReport)

        @property
        def custom_table(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1787.CustomTable":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomTable)

        @property
        def dynamic_custom_report_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1789.DynamicCustomReportItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.DynamicCustomReportItem)

        @property
        def custom_line_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1861.CustomLineChart":
            from mastapy.utility_gui.charts import _1861

            return self._parent._cast(_1861.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1862.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1862

            return self._parent._cast(_1862.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1953.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1953

            return self._parent._cast(_1953.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1954.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1957.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1965.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1965

            return self._parent._cast(_1965.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_2857.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2857,
            )

            return self._parent._cast(_2857.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_4394.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(_4394.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_4725.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4725,
            )

            return self._parent._cast(_4725.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_4729.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4729,
            )

            return self._parent._cast(_4729.PerModeResultsReport)

        @property
        def custom_report_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "CustomReportItem":
            return self._parent

        def __getattr__(self: "CustomReportItem._Cast_CustomReportItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportItem.TYPE"):
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
    def item_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ItemType

        if temp is None:
            return ""

        return temp

    def add_condition(self: Self):
        """Method does not return."""
        self.wrapped.AddCondition()

    @property
    def cast_to(self: Self) -> "CustomReportItem._Cast_CustomReportItem":
        return self._Cast_CustomReportItem(self)
