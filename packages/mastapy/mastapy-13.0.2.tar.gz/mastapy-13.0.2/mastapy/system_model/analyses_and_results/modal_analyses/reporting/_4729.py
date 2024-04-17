"""PerModeResultsReport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MODE_RESULTS_REPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "PerModeResultsReport",
)

if TYPE_CHECKING:
    from mastapy.utility.enums import _1827
    from mastapy.utility.report import _1776, _1777, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("PerModeResultsReport",)


Self = TypeVar("Self", bound="PerModeResultsReport")


class PerModeResultsReport(_1763.CustomReportChart):
    """PerModeResultsReport

    This is a mastapy class.
    """

    TYPE = _PER_MODE_RESULTS_REPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PerModeResultsReport")

    class _Cast_PerModeResultsReport:
        """Special nested class for casting PerModeResultsReport to subclasses."""

        def __init__(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
            parent: "PerModeResultsReport",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
        ) -> "_1763.CustomReportChart":
            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
        ) -> "_1776.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def per_mode_results_report(
            self: "PerModeResultsReport._Cast_PerModeResultsReport",
        ) -> "PerModeResultsReport":
            return self._parent

        def __getattr__(
            self: "PerModeResultsReport._Cast_PerModeResultsReport", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PerModeResultsReport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display_option(self: Self) -> "_1827.TableAndChartOptions":
        """mastapy.utility.enums.TableAndChartOptions"""
        temp = self.wrapped.DisplayOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.enums._1827", "TableAndChartOptions"
        )(value)

    @display_option.setter
    @enforce_parameter_types
    def display_option(self: Self, value: "_1827.TableAndChartOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )
        self.wrapped.DisplayOption = value

    @property
    def include_connected_parts_for_connections(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeConnectedPartsForConnections

        if temp is None:
            return False

        return temp

    @include_connected_parts_for_connections.setter
    @enforce_parameter_types
    def include_connected_parts_for_connections(self: Self, value: "bool"):
        self.wrapped.IncludeConnectedPartsForConnections = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_number_of_modes_to_show_on_a_single_table_or_chart(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfModesToShowOnASingleTableOrChart

        if temp is None:
            return 0

        return temp

    @maximum_number_of_modes_to_show_on_a_single_table_or_chart.setter
    @enforce_parameter_types
    def maximum_number_of_modes_to_show_on_a_single_table_or_chart(
        self: Self, value: "int"
    ):
        self.wrapped.MaximumNumberOfModesToShowOnASingleTableOrChart = (
            int(value) if value is not None else 0
        )

    @property
    def show_all_modes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllModes

        if temp is None:
            return False

        return temp

    @show_all_modes.setter
    @enforce_parameter_types
    def show_all_modes(self: Self, value: "bool"):
        self.wrapped.ShowAllModes = bool(value) if value is not None else False

    @property
    def transpose_chart(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TransposeChart

        if temp is None:
            return False

        return temp

    @transpose_chart.setter
    @enforce_parameter_types
    def transpose_chart(self: Self, value: "bool"):
        self.wrapped.TransposeChart = bool(value) if value is not None else False

    @property
    def transpose_table(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TransposeTable

        if temp is None:
            return False

        return temp

    @transpose_table.setter
    @enforce_parameter_types
    def transpose_table(self: Self, value: "bool"):
        self.wrapped.TransposeTable = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "PerModeResultsReport._Cast_PerModeResultsReport":
        return self._Cast_PerModeResultsReport(self)
