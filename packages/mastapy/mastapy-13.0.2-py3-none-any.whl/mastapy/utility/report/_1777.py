"""CustomReportMultiPropertyItemBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportMultiPropertyItemBase"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1039
    from mastapy.utility.report import _1763, _1776, _1787, _1770
    from mastapy.utility_gui.charts import _1861, _1862
    from mastapy.bearings.bearing_results import _1953, _1957, _1965
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2857,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4725,
        _4729,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportMultiPropertyItemBase",)


Self = TypeVar("Self", bound="CustomReportMultiPropertyItemBase")


class CustomReportMultiPropertyItemBase(_1778.CustomReportNameableItem):
    """CustomReportMultiPropertyItemBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportMultiPropertyItemBase")

    class _Cast_CustomReportMultiPropertyItemBase:
        """Special nested class for casting CustomReportMultiPropertyItemBase to subclasses."""

        def __init__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            parent: "CustomReportMultiPropertyItemBase",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1778.CustomReportNameableItem":
            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1039.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1039

            return self._parent._cast(_1039.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1763.CustomReportChart":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1776.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_table(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1787.CustomTable":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomTable)

        @property
        def custom_line_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1861.CustomLineChart":
            from mastapy.utility_gui.charts import _1861

            return self._parent._cast(_1861.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1862.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1862

            return self._parent._cast(_1862.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1953.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1953

            return self._parent._cast(_1953.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1957.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1965.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1965

            return self._parent._cast(_1965.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_2857.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2857,
            )

            return self._parent._cast(_2857.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_4725.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4725,
            )

            return self._parent._cast(_4725.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_4729.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4729,
            )

            return self._parent._cast(_4729.PerModeResultsReport)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "CustomReportMultiPropertyItemBase":
            return self._parent

        def __getattr__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CustomReportMultiPropertyItemBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase":
        return self._Cast_CustomReportMultiPropertyItemBase(self)
