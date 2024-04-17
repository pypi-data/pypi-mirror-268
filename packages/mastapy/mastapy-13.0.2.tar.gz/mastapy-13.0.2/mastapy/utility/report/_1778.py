"""CustomReportNameableItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMEABLE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportNameableItem"
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
        _1762,
        _1763,
        _1767,
        _1769,
        _1776,
        _1777,
        _1779,
        _1781,
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
__all__ = ("CustomReportNameableItem",)


Self = TypeVar("Self", bound="CustomReportNameableItem")


class CustomReportNameableItem(_1770.CustomReportItem):
    """CustomReportNameableItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMEABLE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportNameableItem")

    class _Cast_CustomReportNameableItem:
        """Special nested class for casting CustomReportNameableItem to subclasses."""

        def __init__(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
            parent: "CustomReportNameableItem",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1770.CustomReportItem":
            return self._parent._cast(_1770.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1039.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1039

            return self._parent._cast(_1039.CylindricalGearTableWithMGCharts)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1749.AdHocCustomTable":
            from mastapy.utility.report import _1749

            return self._parent._cast(_1749.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1757.CustomChart":
            from mastapy.utility.report import _1757

            return self._parent._cast(_1757.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1758.CustomDrawing":
            from mastapy.utility.report import _1758

            return self._parent._cast(_1758.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1759.CustomGraphic":
            from mastapy.utility.report import _1759

            return self._parent._cast(_1759.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1760.CustomImage":
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomImage)

        @property
        def custom_report_cad_drawing(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1762.CustomReportCadDrawing":
            from mastapy.utility.report import _1762

            return self._parent._cast(_1762.CustomReportCadDrawing)

        @property
        def custom_report_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1763.CustomReportChart":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_definition_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1767.CustomReportDefinitionItem":
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_html_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1769.CustomReportHtmlItem":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportHtmlItem)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1776.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_named_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1779.CustomReportNamedItem":
            from mastapy.utility.report import _1779

            return self._parent._cast(_1779.CustomReportNamedItem)

        @property
        def custom_report_status_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1781.CustomReportStatusItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportStatusItem)

        @property
        def custom_report_text(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1784.CustomReportText":
            from mastapy.utility.report import _1784

            return self._parent._cast(_1784.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1786.CustomSubReport":
            from mastapy.utility.report import _1786

            return self._parent._cast(_1786.CustomSubReport)

        @property
        def custom_table(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1787.CustomTable":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomTable)

        @property
        def dynamic_custom_report_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1789.DynamicCustomReportItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.DynamicCustomReportItem)

        @property
        def custom_line_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1861.CustomLineChart":
            from mastapy.utility_gui.charts import _1861

            return self._parent._cast(_1861.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1862.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1862

            return self._parent._cast(_1862.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1953.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1953

            return self._parent._cast(_1953.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1954.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1957.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1965.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1965

            return self._parent._cast(_1965.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_2857.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2857,
            )

            return self._parent._cast(_2857.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4394.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(_4394.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4725.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4725,
            )

            return self._parent._cast(_4725.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4729.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4729,
            )

            return self._parent._cast(_4729.PerModeResultsReport)

        @property
        def custom_report_nameable_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "CustomReportNameableItem":
            return self._parent

        def __getattr__(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportNameableItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def x_position_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @x_position_for_cad.setter
    @enforce_parameter_types
    def x_position_for_cad(self: Self, value: "float"):
        self.wrapped.XPositionForCAD = float(value) if value is not None else 0.0

    @property
    def y_position_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @y_position_for_cad.setter
    @enforce_parameter_types
    def y_position_for_cad(self: Self, value: "float"):
        self.wrapped.YPositionForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportNameableItem._Cast_CustomReportNameableItem":
        return self._Cast_CustomReportNameableItem(self)
