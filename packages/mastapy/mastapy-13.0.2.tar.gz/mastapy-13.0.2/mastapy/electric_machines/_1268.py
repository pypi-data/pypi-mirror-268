"""ElectricMachineDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1273
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ELECTRIC_MACHINE_DETAIL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ElectricMachineDetail"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import (
        _1263,
        _1274,
        _1300,
        _1249,
        _1253,
        _1282,
        _1293,
        _1296,
        _1310,
        _1312,
        _1327,
    )
    from mastapy.electric_machines.results import _1349, _1350
    from mastapy.math_utility import _1529
    from mastapy.utility import _1598
    from mastapy import _7567


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineDetail",)


Self = TypeVar("Self", bound="ElectricMachineDetail")


class ElectricMachineDetail(_0.APIBase):
    """ElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineDetail")

    class _Cast_ElectricMachineDetail:
        """Special nested class for casting ElectricMachineDetail to subclasses."""

        def __init__(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
            parent: "ElectricMachineDetail",
        ):
            self._parent = parent

        @property
        def cad_electric_machine_detail(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1253.CADElectricMachineDetail":
            from mastapy.electric_machines import _1253

            return self._parent._cast(_1253.CADElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1282.InteriorPermanentMagnetMachine":
            from mastapy.electric_machines import _1282

            return self._parent._cast(_1282.InteriorPermanentMagnetMachine)

        @property
        def non_cad_electric_machine_detail(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1293.NonCADElectricMachineDetail":
            from mastapy.electric_machines import _1293

            return self._parent._cast(_1293.NonCADElectricMachineDetail)

        @property
        def permanent_magnet_assisted_synchronous_reluctance_machine(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1296.PermanentMagnetAssistedSynchronousReluctanceMachine":
            from mastapy.electric_machines import _1296

            return self._parent._cast(
                _1296.PermanentMagnetAssistedSynchronousReluctanceMachine
            )

        @property
        def surface_permanent_magnet_machine(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1310.SurfacePermanentMagnetMachine":
            from mastapy.electric_machines import _1310

            return self._parent._cast(_1310.SurfacePermanentMagnetMachine)

        @property
        def synchronous_reluctance_machine(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1312.SynchronousReluctanceMachine":
            from mastapy.electric_machines import _1312

            return self._parent._cast(_1312.SynchronousReluctanceMachine)

        @property
        def wound_field_synchronous_machine(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "_1327.WoundFieldSynchronousMachine":
            from mastapy.electric_machines import _1327

            return self._parent._cast(_1327.WoundFieldSynchronousMachine)

        @property
        def electric_machine_detail(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail",
        ) -> "ElectricMachineDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineDetail._Cast_ElectricMachineDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def core_loss_build_factor_specification_method(
        self: Self,
    ) -> "_1263.CoreLossBuildFactorSpecificationMethod":
        """mastapy.electric_machines.CoreLossBuildFactorSpecificationMethod"""
        temp = self.wrapped.CoreLossBuildFactorSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.CoreLossBuildFactorSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1263", "CoreLossBuildFactorSpecificationMethod"
        )(value)

    @core_loss_build_factor_specification_method.setter
    @enforce_parameter_types
    def core_loss_build_factor_specification_method(
        self: Self, value: "_1263.CoreLossBuildFactorSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.CoreLossBuildFactorSpecificationMethod",
        )
        self.wrapped.CoreLossBuildFactorSpecificationMethod = value

    @property
    def dc_bus_voltage(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DCBusVoltage

        if temp is None:
            return 0.0

        return temp

    @dc_bus_voltage.setter
    @enforce_parameter_types
    def dc_bus_voltage(self: Self, value: "float"):
        self.wrapped.DCBusVoltage = float(value) if value is not None else 0.0

    @property
    def eddy_current_core_loss_build_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EddyCurrentCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @eddy_current_core_loss_build_factor.setter
    @enforce_parameter_types
    def eddy_current_core_loss_build_factor(self: Self, value: "float"):
        self.wrapped.EddyCurrentCoreLossBuildFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def effective_machine_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveMachineLength

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_type(self: Self) -> "_1274.ElectricMachineType":
        """mastapy.electric_machines.ElectricMachineType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.ElectricMachineType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1274", "ElectricMachineType"
        )(value)

    @property
    def enclosing_volume(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnclosingVolume

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_core_loss_build_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ExcessCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @excess_core_loss_build_factor.setter
    @enforce_parameter_types
    def excess_core_loss_build_factor(self: Self, value: "float"):
        self.wrapped.ExcessCoreLossBuildFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def has_non_linear_dq_model(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasNonLinearDQModel

        if temp is None:
            return False

        return temp

    @property
    def hysteresis_core_loss_build_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HysteresisCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @hysteresis_core_loss_build_factor.setter
    @enforce_parameter_types
    def hysteresis_core_loss_build_factor(self: Self, value: "float"):
        self.wrapped.HysteresisCoreLossBuildFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def include_default_results_locations(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeDefaultResultsLocations

        if temp is None:
            return False

        return temp

    @include_default_results_locations.setter
    @enforce_parameter_types
    def include_default_results_locations(self: Self, value: "bool"):
        self.wrapped.IncludeDefaultResultsLocations = (
            bool(value) if value is not None else False
        )

    @property
    def include_shaft(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeShaft

        if temp is None:
            return False

        return temp

    @include_shaft.setter
    @enforce_parameter_types
    def include_shaft(self: Self, value: "bool"):
        self.wrapped.IncludeShaft = bool(value) if value is not None else False

    @property
    def line_line_supply_voltage_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineLineSupplyVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def machine_periodicity_factor(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MachinePeriodicityFactor

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @machine_periodicity_factor.setter
    @enforce_parameter_types
    def machine_periodicity_factor(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MachinePeriodicityFactor = value

    @property
    def magnet_loss_build_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnetLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @magnet_loss_build_factor.setter
    @enforce_parameter_types
    def magnet_loss_build_factor(self: Self, value: "float"):
        self.wrapped.MagnetLossBuildFactor = float(value) if value is not None else 0.0

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
    def number_of_phases(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfPhases

        if temp is None:
            return 0

        return temp

    @property
    def number_of_slots_per_phase(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSlotsPerPhase

        if temp is None:
            return 0

        return temp

    @property
    def number_of_slots_per_pole(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSlotsPerPole

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_slots_per_pole_per_phase(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSlotsPerPolePerPhase

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_supply_voltage_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseSupplyVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_supply_voltage_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseSupplyVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_air_gap(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialAirGap

        if temp is None:
            return 0.0

        return temp

    @radial_air_gap.setter
    @enforce_parameter_types
    def radial_air_gap(self: Self, value: "float"):
        self.wrapped.RadialAirGap = float(value) if value is not None else 0.0

    @property
    def rated_inverter_current_peak(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RatedInverterCurrentPeak

        if temp is None:
            return 0.0

        return temp

    @rated_inverter_current_peak.setter
    @enforce_parameter_types
    def rated_inverter_current_peak(self: Self, value: "float"):
        self.wrapped.RatedInverterCurrentPeak = (
            float(value) if value is not None else 0.0
        )

    @property
    def rated_inverter_phase_current_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedInverterPhaseCurrentPeak

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_core_loss_build_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @rotor_core_loss_build_factor.setter
    @enforce_parameter_types
    def rotor_core_loss_build_factor(self: Self, value: "float"):
        self.wrapped.RotorCoreLossBuildFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def select_setup(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup":
        """ListWithSelectedItem[mastapy.electric_machines.ElectricMachineSetup]"""
        temp = self.wrapped.SelectSetup

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ElectricMachineSetup",
        )(temp)

    @select_setup.setter
    @enforce_parameter_types
    def select_setup(self: Self, value: "_1273.ElectricMachineSetup"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectSetup = value

    @property
    def shaft_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftDiameter

        if temp is None:
            return 0.0

        return temp

    @shaft_diameter.setter
    @enforce_parameter_types
    def shaft_diameter(self: Self, value: "float"):
        self.wrapped.ShaftDiameter = float(value) if value is not None else 0.0

    @property
    def shaft_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ShaftMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @shaft_material_database.setter
    @enforce_parameter_types
    def shaft_material_database(self: Self, value: "str"):
        self.wrapped.ShaftMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def stator_core_loss_build_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StatorCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @stator_core_loss_build_factor.setter
    @enforce_parameter_types
    def stator_core_loss_build_factor(self: Self, value: "float"):
        self.wrapped.StatorCoreLossBuildFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def non_linear_dq_model(self: Self) -> "_1349.NonLinearDQModel":
        """mastapy.electric_machines.results.NonLinearDQModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonLinearDQModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def non_linear_dq_model_generator_settings(
        self: Self,
    ) -> "_1350.NonLinearDQModelGeneratorSettings":
        """mastapy.electric_machines.results.NonLinearDQModelGeneratorSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonLinearDQModelGeneratorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor(self: Self) -> "_1300.Rotor":
        """mastapy.electric_machines.Rotor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_setup(self: Self) -> "_1273.ElectricMachineSetup":
        """mastapy.electric_machines.ElectricMachineSetup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedSetup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator(self: Self) -> "_1249.AbstractStator":
        """mastapy.electric_machines.AbstractStator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_locations(self: Self) -> "List[_1529.Named2DLocation]":
        """List[mastapy.math_utility.Named2DLocation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsLocations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def setups(self: Self) -> "List[_1273.ElectricMachineSetup]":
        """List[mastapy.electric_machines.ElectricMachineSetup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Setups

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

    def generate_cad_geometry_model(self: Self):
        """Method does not return."""
        self.wrapped.GenerateCADGeometryModel()

    @enforce_parameter_types
    def add_results_location(self: Self, name: "str"):
        """Method does not return.

        Args:
            name (str)
        """
        name = str(name)
        self.wrapped.AddResultsLocation(name if name else "")

    def add_setup(self: Self) -> "_1273.ElectricMachineSetup":
        """mastapy.electric_machines.ElectricMachineSetup"""
        method_result = self.wrapped.AddSetup()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate_setup(
        self: Self, setup: "_1273.ElectricMachineSetup"
    ) -> "_1273.ElectricMachineSetup":
        """mastapy.electric_machines.ElectricMachineSetup

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """
        method_result = self.wrapped.DuplicateSetup(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def export_to_smt_format(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.ExportToSMTFormat(file_name if file_name else "")

    def generate_design_without_non_linear_dq_model(
        self: Self,
    ) -> "_1598.MethodOutcomeWithResult[ElectricMachineDetail]":
        """mastapy.utility.MethodOutcomeWithResult[mastapy.electric_machines.ElectricMachineDetail]"""
        method_result = self.wrapped.GenerateDesignWithoutNonLinearDQModel()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_results_location(self: Self, name: "str"):
        """Method does not return.

        Args:
            name (str)
        """
        name = str(name)
        self.wrapped.RemoveResultsLocation(name if name else "")

    @enforce_parameter_types
    def remove_setup(self: Self, setup: "_1273.ElectricMachineSetup"):
        """Method does not return.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """
        self.wrapped.RemoveSetup(setup.wrapped if setup else None)

    @enforce_parameter_types
    def setup_named(self: Self, name: "str") -> "_1273.ElectricMachineSetup":
        """mastapy.electric_machines.ElectricMachineSetup

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.SetupNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def try_generate_non_linear_dq_model(
        self: Self,
    ) -> "_1598.MethodOutcomeWithResult[ElectricMachineDetail]":
        """mastapy.utility.MethodOutcomeWithResult[mastapy.electric_machines.ElectricMachineDetail]"""
        method_result = self.wrapped.TryGenerateNonLinearDQModel()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_generate_non_linear_dq_model_with_task_progress(
        self: Self, progress: "_7567.TaskProgress"
    ) -> "_1598.MethodOutcomeWithResult[ElectricMachineDetail]":
        """mastapy.utility.MethodOutcomeWithResult[mastapy.electric_machines.ElectricMachineDetail]

        Args:
            progress (mastapy.TaskProgress)
        """
        method_result = self.wrapped.TryGenerateNonLinearDQModelWithTaskProgress(
            progress.wrapped if progress else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def write_dxf_to(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.WriteDxfTo(file_name if file_name else "")

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
    def cast_to(self: Self) -> "ElectricMachineDetail._Cast_ElectricMachineDetail":
        return self._Cast_ElectricMachineDetail(self)
