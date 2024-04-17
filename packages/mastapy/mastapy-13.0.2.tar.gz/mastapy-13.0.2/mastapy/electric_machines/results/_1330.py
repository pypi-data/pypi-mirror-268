"""ElectricMachineDQModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DQ_MODEL = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineDQModel"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1320
    from mastapy.electric_machines.results import _1347, _1349


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineDQModel",)


Self = TypeVar("Self", bound="ElectricMachineDQModel")


class ElectricMachineDQModel(_0.APIBase):
    """ElectricMachineDQModel

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DQ_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineDQModel")

    class _Cast_ElectricMachineDQModel:
        """Special nested class for casting ElectricMachineDQModel to subclasses."""

        def __init__(
            self: "ElectricMachineDQModel._Cast_ElectricMachineDQModel",
            parent: "ElectricMachineDQModel",
        ):
            self._parent = parent

        @property
        def linear_dq_model(
            self: "ElectricMachineDQModel._Cast_ElectricMachineDQModel",
        ) -> "_1347.LinearDQModel":
            from mastapy.electric_machines.results import _1347

            return self._parent._cast(_1347.LinearDQModel)

        @property
        def non_linear_dq_model(
            self: "ElectricMachineDQModel._Cast_ElectricMachineDQModel",
        ) -> "_1349.NonLinearDQModel":
            from mastapy.electric_machines.results import _1349

            return self._parent._cast(_1349.NonLinearDQModel)

        @property
        def electric_machine_dq_model(
            self: "ElectricMachineDQModel._Cast_ElectricMachineDQModel",
        ) -> "ElectricMachineDQModel":
            return self._parent

        def __getattr__(
            self: "ElectricMachineDQModel._Cast_ElectricMachineDQModel", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineDQModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conductor_dimension_for_skin_depth_calculation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConductorDimensionForSkinDepthCalculation

        if temp is None:
            return 0.0

        return temp

    @property
    def current_angle_to_maximise_torque_at_maximum_current_at_reference_temperature(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.CurrentAngleToMaximiseTorqueAtMaximumCurrentAtReferenceTemperature
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_peak_phase_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPeakPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_peak_phase_supply_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPeakPhaseSupplyVoltage

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
    def number_of_pole_pairs(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfPolePairs

        if temp is None:
            return 0

        return temp

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistanceAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def steady_state_short_circuit_current_at_reference_temperature(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateShortCircuitCurrentAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_coefficient_for_remanence(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureCoefficientForRemanence

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_coefficient_for_winding_resistivity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureCoefficientForWindingResistivity

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_connection(self: Self) -> "_1320.WindingConnection":
        """mastapy.electric_machines.WindingConnection

        Note:
            This property is readonly.
        """
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

    @property
    def winding_material_relative_permeability_at_reference_temperature(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingMaterialRelativePermeabilityAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_resistivity_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingResistivityAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self: Self) -> "ElectricMachineDQModel._Cast_ElectricMachineDQModel":
        return self._Cast_ElectricMachineDQModel(self)
