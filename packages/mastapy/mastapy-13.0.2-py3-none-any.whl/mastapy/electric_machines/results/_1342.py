"""ElectricMachineResultsTimeStep"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_TIME_STEP = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineResultsTimeStep"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.electric_machines.results import _1340, _1343, _1341, _1339


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsTimeStep",)


Self = TypeVar("Self", bound="ElectricMachineResultsTimeStep")


class ElectricMachineResultsTimeStep(_0.APIBase):
    """ElectricMachineResultsTimeStep

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_TIME_STEP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineResultsTimeStep")

    class _Cast_ElectricMachineResultsTimeStep:
        """Special nested class for casting ElectricMachineResultsTimeStep to subclasses."""

        def __init__(
            self: "ElectricMachineResultsTimeStep._Cast_ElectricMachineResultsTimeStep",
            parent: "ElectricMachineResultsTimeStep",
        ):
            self._parent = parent

        @property
        def electric_machine_results_time_step(
            self: "ElectricMachineResultsTimeStep._Cast_ElectricMachineResultsTimeStep",
        ) -> "ElectricMachineResultsTimeStep":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsTimeStep._Cast_ElectricMachineResultsTimeStep",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineResultsTimeStep.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ac_winding_loss(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ACWindingLoss

        if temp is None:
            return 0.0

        return temp

    @ac_winding_loss.setter
    @enforce_parameter_types
    def ac_winding_loss(self: Self, value: "float"):
        self.wrapped.ACWindingLoss = float(value) if value is not None else 0.0

    @property
    def apparent_d_axis_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentDAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_q_axis_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentQAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_armature_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisArmatureFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_reactive_voltages(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisReactiveVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_resistive_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisResistiveVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_terminal_voltages(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisTerminalVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricalAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def flux_density_in_air_gap_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluxDensityInAirGapChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_density_in_air_gap_mst_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceDensityInAirGapMSTChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mechanical_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MechanicalAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def q_axis_armature_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisArmatureFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_reactive_voltages(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisReactiveVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_resistive_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisResistiveVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_terminal_voltages(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisTerminalVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_resultant_x_force_mst_single_contour(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorResultantXForceMSTSingleContour

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_resultant_y_force_mst_single_contour(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorResultantYForceMSTSingleContour

        if temp is None:
            return 0.0

        return temp

    @property
    def time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Time

        if temp is None:
            return 0.0

        return temp

    @property
    def time_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeIndex

        if temp is None:
            return 0

        return temp

    @property
    def torque_from_stator_tooth_tangential_forces(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueFromStatorToothTangentialForces

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_mst_single_contour(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueMSTSingleContour

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_mst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueMST

        if temp is None:
            return 0.0

        return temp

    @property
    def results_for_stator_teeth(
        self: Self,
    ) -> "List[_1340.ElectricMachineResultsForStatorToothAtTimeStep]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsForStatorToothAtTimeStep]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForStatorTeeth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_at_locations(
        self: Self,
    ) -> "List[_1343.ElectricMachineResultsTimeStepAtLocation]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsTimeStepAtLocation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsAtLocations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_line_to_line(
        self: Self,
    ) -> "List[_1341.ElectricMachineResultsLineToLineAtTimeStep]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsLineToLineAtTimeStep]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForLineToLine

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_phases(
        self: Self,
    ) -> "List[_1339.ElectricMachineResultsForPhaseAtTimeStep]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsForPhaseAtTimeStep]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForPhases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def elemental_flux_densities(self: Self) -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementalFluxDensities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

        if value is None:
            return None

        return value

    @property
    def magnetic_vector_potential(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagneticVectorPotential

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def nodal_positions(self: Self) -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodalPositions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

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

    @enforce_parameter_types
    def elements_node_id_for(self: Self, node_number: "int") -> "List[int]":
        """List[int]

        Args:
            node_number (int)
        """
        node_number = int(node_number)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ElementsNodeIDFor(node_number if node_number else 0), int
        )

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
    def cast_to(
        self: Self,
    ) -> "ElectricMachineResultsTimeStep._Cast_ElectricMachineResultsTimeStep":
        return self._Cast_ElectricMachineResultsTimeStep(self)
