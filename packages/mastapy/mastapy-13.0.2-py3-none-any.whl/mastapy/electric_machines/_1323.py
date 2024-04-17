"""Windings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_WINDINGS = python_net_import("SMT.MastaAPI.ElectricMachines", "Windings")

if TYPE_CHECKING:
    from mastapy.electric_machines import (
        _1265,
        _1275,
        _1304,
        _1320,
        _1325,
        _1326,
        _1324,
        _1259,
        _1319,
        _1298,
        _1305,
    )
    from mastapy.electric_machines.load_cases_and_analyses import _1369
    from mastapy.utility_gui.charts import _1874
    from mastapy.math_utility import _1520


__docformat__ = "restructuredtext en"
__all__ = ("Windings",)


Self = TypeVar("Self", bound="Windings")


class Windings(_0.APIBase):
    """Windings

    This is a mastapy class.
    """

    TYPE = _WINDINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Windings")

    class _Cast_Windings:
        """Special nested class for casting Windings to subclasses."""

        def __init__(self: "Windings._Cast_Windings", parent: "Windings"):
            self._parent = parent

        @property
        def windings(self: "Windings._Cast_Windings") -> "Windings":
            return self._parent

        def __getattr__(self: "Windings._Cast_Windings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Windings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def awg_selector(self: Self) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.AWGSelector

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @awg_selector.setter
    @enforce_parameter_types
    def awg_selector(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.AWGSelector = value

    @property
    def double_layer_winding_slot_positions(
        self: Self,
    ) -> "_1265.DoubleLayerWindingSlotPositions":
        """mastapy.electric_machines.DoubleLayerWindingSlotPositions"""
        temp = self.wrapped.DoubleLayerWindingSlotPositions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.DoubleLayerWindingSlotPositions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1265", "DoubleLayerWindingSlotPositions"
        )(value)

    @double_layer_winding_slot_positions.setter
    @enforce_parameter_types
    def double_layer_winding_slot_positions(
        self: Self, value: "_1265.DoubleLayerWindingSlotPositions"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.DoubleLayerWindingSlotPositions"
        )
        self.wrapped.DoubleLayerWindingSlotPositions = value

    @property
    def end_winding_inductance_rosa_and_grover(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EndWindingInductanceRosaAndGrover

        if temp is None:
            return 0.0

        return temp

    @property
    def end_winding_inductance_method(self: Self) -> "_1369.EndWindingInductanceMethod":
        """mastapy.electric_machines.load_cases_and_analyses.EndWindingInductanceMethod"""
        temp = self.wrapped.EndWindingInductanceMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.EndWindingInductanceMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1369",
            "EndWindingInductanceMethod",
        )(value)

    @end_winding_inductance_method.setter
    @enforce_parameter_types
    def end_winding_inductance_method(
        self: Self, value: "_1369.EndWindingInductanceMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.EndWindingInductanceMethod",
        )
        self.wrapped.EndWindingInductanceMethod = value

    @property
    def end_winding_pole_pitch_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndWindingPolePitchFactor

        if temp is None:
            return 0.0

        return temp

    @end_winding_pole_pitch_factor.setter
    @enforce_parameter_types
    def end_winding_pole_pitch_factor(self: Self, value: "float"):
        self.wrapped.EndWindingPolePitchFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def factor_for_phase_circle_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FactorForPhaseCircleSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @factor_for_phase_circle_size.setter
    @enforce_parameter_types
    def factor_for_phase_circle_size(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FactorForPhaseCircleSize = value

    @property
    def fill_factor_specification_method(
        self: Self,
    ) -> "_1275.FillFactorSpecificationMethod":
        """mastapy.electric_machines.FillFactorSpecificationMethod"""
        temp = self.wrapped.FillFactorSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.FillFactorSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1275", "FillFactorSpecificationMethod"
        )(value)

    @fill_factor_specification_method.setter
    @enforce_parameter_types
    def fill_factor_specification_method(
        self: Self, value: "_1275.FillFactorSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.FillFactorSpecificationMethod"
        )
        self.wrapped.FillFactorSpecificationMethod = value

    @property
    def iec60228_wire_gauge_selector(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_float":
        """ListWithSelectedItem[float]"""
        temp = self.wrapped.IEC60228WireGaugeSelector

        if temp is None:
            return 0.0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_float",
        )(temp)

    @iec60228_wire_gauge_selector.setter
    @enforce_parameter_types
    def iec60228_wire_gauge_selector(self: Self, value: "float"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0
        )
        self.wrapped.IEC60228WireGaugeSelector = value

    @property
    def include_individual_conductors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeIndividualConductors

        if temp is None:
            return False

        return temp

    @include_individual_conductors.setter
    @enforce_parameter_types
    def include_individual_conductors(self: Self, value: "bool"):
        self.wrapped.IncludeIndividualConductors = (
            bool(value) if value is not None else False
        )

    @property
    def mmf(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MMF

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def material_cost(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialCost

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_length_per_turn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanLengthPerTurn

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_coils_per_parallel_path(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCoilsPerParallelPath

        if temp is None:
            return 0

        return temp

    @property
    def number_of_coils_per_phase(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCoilsPerPhase

        if temp is None:
            return 0

        return temp

    @property
    def number_of_coils_per_phase_per_parallel_path(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCoilsPerPhasePerParallelPath

        if temp is None:
            return 0

        return temp

    @property
    def number_of_electrical_orders_for_mmf_chart(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfElectricalOrdersForMMFChart

        if temp is None:
            return 0

        return temp

    @number_of_electrical_orders_for_mmf_chart.setter
    @enforce_parameter_types
    def number_of_electrical_orders_for_mmf_chart(self: Self, value: "int"):
        self.wrapped.NumberOfElectricalOrdersForMMFChart = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_parallel_paths(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfParallelPaths

        if temp is None:
            return 0

        return temp

    @number_of_parallel_paths.setter
    @enforce_parameter_types
    def number_of_parallel_paths(self: Self, value: "int"):
        self.wrapped.NumberOfParallelPaths = int(value) if value is not None else 0

    @property
    def number_of_strands_per_turn(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStrandsPerTurn

        if temp is None:
            return 0

        return temp

    @number_of_strands_per_turn.setter
    @enforce_parameter_types
    def number_of_strands_per_turn(self: Self, value: "int"):
        self.wrapped.NumberOfStrandsPerTurn = int(value) if value is not None else 0

    @property
    def number_of_turns(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTurns

        if temp is None:
            return 0

        return temp

    @number_of_turns.setter
    @enforce_parameter_types
    def number_of_turns(self: Self, value: "int"):
        self.wrapped.NumberOfTurns = int(value) if value is not None else 0

    @property
    def number_of_turns_per_phase(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTurnsPerPhase

        if temp is None:
            return 0

        return temp

    @property
    def number_of_winding_layers(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfWindingLayers

        if temp is None:
            return 0

        return temp

    @number_of_winding_layers.setter
    @enforce_parameter_types
    def number_of_winding_layers(self: Self, value: "int"):
        self.wrapped.NumberOfWindingLayers = int(value) if value is not None else 0

    @property
    def overall_fill_factor_windings(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OverallFillFactorWindings

        if temp is None:
            return 0.0

        return temp

    @overall_fill_factor_windings.setter
    @enforce_parameter_types
    def overall_fill_factor_windings(self: Self, value: "float"):
        self.wrapped.OverallFillFactorWindings = (
            float(value) if value is not None else 0.0
        )

    @property
    def overall_winding_material_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallWindingMaterialArea

        if temp is None:
            return 0.0

        return temp

    @property
    def single_double_layer_windings(self: Self) -> "_1304.SingleOrDoubleLayerWindings":
        """mastapy.electric_machines.SingleOrDoubleLayerWindings"""
        temp = self.wrapped.SingleDoubleLayerWindings

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.SingleOrDoubleLayerWindings"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1304", "SingleOrDoubleLayerWindings"
        )(value)

    @single_double_layer_windings.setter
    @enforce_parameter_types
    def single_double_layer_windings(
        self: Self, value: "_1304.SingleOrDoubleLayerWindings"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.SingleOrDoubleLayerWindings"
        )
        self.wrapped.SingleDoubleLayerWindings = value

    @property
    def throw_for_automated_winding_generation(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.ThrowForAutomatedWindingGeneration

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @throw_for_automated_winding_generation.setter
    @enforce_parameter_types
    def throw_for_automated_winding_generation(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.ThrowForAutomatedWindingGeneration = value

    @property
    def total_length_of_conductors_in_phase(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalLengthOfConductorsInPhase

        if temp is None:
            return 0.0

        return temp

    @property
    def total_slot_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSlotArea

        if temp is None:
            return 0.0

        return temp

    @property
    def user_specified_end_winding_inductance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedEndWindingInductance

        if temp is None:
            return 0.0

        return temp

    @user_specified_end_winding_inductance.setter
    @enforce_parameter_types
    def user_specified_end_winding_inductance(self: Self, value: "float"):
        self.wrapped.UserSpecifiedEndWindingInductance = (
            float(value) if value is not None else 0.0
        )

    @property
    def winding_connection(self: Self) -> "_1320.WindingConnection":
        """mastapy.electric_machines.WindingConnection"""
        temp = self.wrapped.WindingConnection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.WindingConnection"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1320", "WindingConnection"
        )(value)

    @winding_connection.setter
    @enforce_parameter_types
    def winding_connection(self: Self, value: "_1320.WindingConnection"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.WindingConnection"
        )
        self.wrapped.WindingConnection = value

    @property
    def winding_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.WindingMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @winding_material_database.setter
    @enforce_parameter_types
    def winding_material_database(self: Self, value: "str"):
        self.wrapped.WindingMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def winding_material_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WindingMaterialDiameter

        if temp is None:
            return 0.0

        return temp

    @winding_material_diameter.setter
    @enforce_parameter_types
    def winding_material_diameter(self: Self, value: "float"):
        self.wrapped.WindingMaterialDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def winding_type(self: Self) -> "_1325.WindingType":
        """mastapy.electric_machines.WindingType"""
        temp = self.wrapped.WindingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.WindingType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1325", "WindingType"
        )(value)

    @winding_type.setter
    @enforce_parameter_types
    def winding_type(self: Self, value: "_1325.WindingType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.WindingType"
        )
        self.wrapped.WindingType = value

    @property
    def wire_size_specification_method(
        self: Self,
    ) -> "_1326.WireSizeSpecificationMethod":
        """mastapy.electric_machines.WireSizeSpecificationMethod"""
        temp = self.wrapped.WireSizeSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.WireSizeSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1326", "WireSizeSpecificationMethod"
        )(value)

    @wire_size_specification_method.setter
    @enforce_parameter_types
    def wire_size_specification_method(
        self: Self, value: "_1326.WireSizeSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.WireSizeSpecificationMethod"
        )
        self.wrapped.WireSizeSpecificationMethod = value

    @property
    def mmf_fourier_series_electrical(self: Self) -> "_1520.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MMFFourierSeriesElectrical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mmf_fourier_series_mechanical(self: Self) -> "_1520.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MMFFourierSeriesMechanical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def windings_viewer(self: Self) -> "_1324.WindingsViewer":
        """mastapy.electric_machines.WindingsViewer

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingsViewer

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coils(self: Self) -> "List[_1259.Coil]":
        """List[mastapy.electric_machines.Coil]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Coils

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conductors(self: Self) -> "List[_1319.WindingConductor]":
        """List[mastapy.electric_machines.WindingConductor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Conductors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def phases(self: Self) -> "List[_1298.Phase]":
        """List[mastapy.electric_machines.Phase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Phases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def slot_section_details(self: Self) -> "List[_1305.SlotSectionDetail]":
        """List[mastapy.electric_machines.SlotSectionDetail]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlotSectionDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def generate_default_winding_configuration_coils(self: Self):
        """Method does not return."""
        self.wrapped.GenerateDefaultWindingConfigurationCoils()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "Windings._Cast_Windings":
        return self._Cast_Windings(self)
