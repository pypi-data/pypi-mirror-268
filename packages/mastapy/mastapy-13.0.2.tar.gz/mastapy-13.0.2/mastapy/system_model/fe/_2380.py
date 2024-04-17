"""ElectricMachineDataSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.fe import _2392
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_DOUBLE = python_net_import("System", "Double")
_STRING = python_net_import("System", "String")
_HARMONIC_LOAD_DATA_TYPE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "HarmonicLoadDataType"
)
_FE_SUBSTRUCTURE_NODE = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureNode"
)
_ELECTRIC_MACHINE_DATA_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ElectricMachineDataSet"
)
_LIST = python_net_import("System.Collections.Generic", "List")
_MEASUREMENT_TYPE = python_net_import(
    "SMT.MastaAPIUtility.UnitsAndMeasurements", "MeasurementType"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.electric_machines.harmonic_load_data import _1389
    from mastapy.units_and_measurements import _7568
    from mastapy.math_utility import _1528


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineDataSet",)


Self = TypeVar("Self", bound="ElectricMachineDataSet")


class ElectricMachineDataSet(_0.APIBase):
    """ElectricMachineDataSet

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DATA_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineDataSet")

    class _Cast_ElectricMachineDataSet:
        """Special nested class for casting ElectricMachineDataSet to subclasses."""

        def __init__(
            self: "ElectricMachineDataSet._Cast_ElectricMachineDataSet",
            parent: "ElectricMachineDataSet",
        ):
            self._parent = parent

        @property
        def electric_machine_data_set(
            self: "ElectricMachineDataSet._Cast_ElectricMachineDataSet",
        ) -> "ElectricMachineDataSet":
            return self._parent

        def __getattr__(
            self: "ElectricMachineDataSet._Cast_ElectricMachineDataSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineDataSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_set_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DataSetName

        if temp is None:
            return ""

        return temp

    @data_set_name.setter
    @enforce_parameter_types
    def data_set_name(self: Self, value: "str"):
        self.wrapped.DataSetName = str(value) if value is not None else ""

    @property
    def node_for_first_tooth(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_FESubstructureNode":
        """ListWithSelectedItem[mastapy.system_model.fe.FESubstructureNode]"""
        temp = self.wrapped.NodeForFirstTooth

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FESubstructureNode",
        )(temp)

    @node_for_first_tooth.setter
    @enforce_parameter_types
    def node_for_first_tooth(self: Self, value: "_2392.FESubstructureNode"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructureNode.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructureNode.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.NodeForFirstTooth = value

    @property
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(
        self: Self, value: "float"
    ):
        self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_x_force_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorXForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_x_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_x_force_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.RotorXForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_y_force_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorYForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_y_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_y_force_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.RotorYForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_z_force_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorZForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_z_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_z_force_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.RotorZForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def stator_axial_loads_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StatorAxialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_axial_loads_amplitude_cut_off.setter
    @enforce_parameter_types
    def stator_axial_loads_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.StatorAxialLoadsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def stator_radial_loads_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StatorRadialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_radial_loads_amplitude_cut_off.setter
    @enforce_parameter_types
    def stator_radial_loads_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.StatorRadialLoadsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def stator_tangential_loads_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StatorTangentialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_tangential_loads_amplitude_cut_off.setter
    @enforce_parameter_types
    def stator_tangential_loads_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.StatorTangentialLoadsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def stator_tooth_moments_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StatorToothMomentsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_tooth_moments_amplitude_cut_off.setter
    @enforce_parameter_types
    def stator_tooth_moments_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.StatorToothMomentsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def torque_ripple_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorqueRippleAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @torque_ripple_amplitude_cut_off.setter
    @enforce_parameter_types
    def torque_ripple_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.TorqueRippleAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def torque_ripple_input_type(self: Self) -> "_6985.TorqueRippleInputType":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueRippleInputType"""
        temp = self.wrapped.TorqueRippleInputType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.TorqueRippleInputType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6985",
            "TorqueRippleInputType",
        )(value)

    @torque_ripple_input_type.setter
    @enforce_parameter_types
    def torque_ripple_input_type(self: Self, value: "_6985.TorqueRippleInputType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.TorqueRippleInputType",
        )
        self.wrapped.TorqueRippleInputType = value

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

    def delete_data_set(self: Self):
        """Method does not return."""
        self.wrapped.DeleteDataSet()

    @enforce_parameter_types
    def add_or_replace_excitation_data_with_amplitudes_phases_and_fe_node(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        node: "_2392.FESubstructureNode",
        speed: "float",
        fourier_series_amplitudes: "List[float]",
        fourier_series_phases: "List[float]",
        fourier_series_mean_value: "float",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7568.MeasurementType",
    ):
        """Method does not return.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            node (mastapy.system_model.fe.FESubstructureNode)
            speed (float)
            fourier_series_amplitudes (List[float])
            fourier_series_phases (List[float])
            fourier_series_mean_value (float)
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        speed = float(speed)
        fourier_series_amplitudes = conversion.mp_to_pn_list_float(
            fourier_series_amplitudes
        )
        fourier_series_phases = conversion.mp_to_pn_list_float(fourier_series_phases)
        fourier_series_mean_value = float(fourier_series_mean_value)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.AddOrReplaceExcitationData.Overloads[
            _HARMONIC_LOAD_DATA_TYPE,
            _FE_SUBSTRUCTURE_NODE,
            _DOUBLE,
            _LIST[_DOUBLE],
            _LIST[_DOUBLE],
            _DOUBLE,
            _STRING,
            _MEASUREMENT_TYPE,
        ](
            harmonic_load_data_type,
            node.wrapped if node else None,
            speed if speed else 0.0,
            fourier_series_amplitudes,
            fourier_series_phases,
            fourier_series_mean_value if fourier_series_mean_value else 0.0,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

    @enforce_parameter_types
    def add_or_replace_excitation_data_with_fe_node(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        node: "_2392.FESubstructureNode",
        speed: "float",
        fourier_series_values: "List[float]",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7568.MeasurementType",
    ):
        """Method does not return.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            node (mastapy.system_model.fe.FESubstructureNode)
            speed (float)
            fourier_series_values (List[float])
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        speed = float(speed)
        fourier_series_values = conversion.mp_to_pn_array_float(fourier_series_values)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.AddOrReplaceExcitationData.Overloads[
            _HARMONIC_LOAD_DATA_TYPE,
            _FE_SUBSTRUCTURE_NODE,
            _DOUBLE,
            _ARRAY[_DOUBLE],
            _STRING,
            _MEASUREMENT_TYPE,
        ](
            harmonic_load_data_type,
            node.wrapped if node else None,
            speed if speed else 0.0,
            fourier_series_values,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

    @enforce_parameter_types
    def add_or_replace_excitation_data_with_amplitudes_and_phases(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        speed: "float",
        fourier_series_amplitudes: "List[float]",
        fourier_series_phases: "List[float]",
        fourier_series_mean_value: "float",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7568.MeasurementType",
    ):
        """Method does not return.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            speed (float)
            fourier_series_amplitudes (List[float])
            fourier_series_phases (List[float])
            fourier_series_mean_value (float)
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        speed = float(speed)
        fourier_series_amplitudes = conversion.mp_to_pn_list_float(
            fourier_series_amplitudes
        )
        fourier_series_phases = conversion.mp_to_pn_list_float(fourier_series_phases)
        fourier_series_mean_value = float(fourier_series_mean_value)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.AddOrReplaceExcitationData.Overloads[
            _HARMONIC_LOAD_DATA_TYPE,
            _DOUBLE,
            _LIST[_DOUBLE],
            _LIST[_DOUBLE],
            _DOUBLE,
            _STRING,
            _MEASUREMENT_TYPE,
        ](
            harmonic_load_data_type,
            speed if speed else 0.0,
            fourier_series_amplitudes,
            fourier_series_phases,
            fourier_series_mean_value if fourier_series_mean_value else 0.0,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

    @enforce_parameter_types
    def add_or_replace_excitation_data(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        speed: "float",
        fourier_series_values: "List[float]",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7568.MeasurementType",
    ):
        """Method does not return.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            speed (float)
            fourier_series_values (List[float])
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        speed = float(speed)
        fourier_series_values = conversion.mp_to_pn_array_float(fourier_series_values)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.AddOrReplaceExcitationData.Overloads[
            _HARMONIC_LOAD_DATA_TYPE,
            _DOUBLE,
            _ARRAY[_DOUBLE],
            _STRING,
            _MEASUREMENT_TYPE,
        ](
            harmonic_load_data_type,
            speed if speed else 0.0,
            fourier_series_values,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

    def clear_all_data(self: Self):
        """Method does not return."""
        self.wrapped.ClearAllData()

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    def derive_rotor_forces_from_stator_loads(self: Self):
        """Method does not return."""
        self.wrapped.DeriveRotorForcesFromStatorLoads()

    def derive_rotor_moments_interpolators_from_stator_axial_loads_interpolators(
        self: Self,
    ):
        """Method does not return."""
        self.wrapped.DeriveRotorMomentsInterpolatorsFromStatorAxialLoadsInterpolators()

    def derive_rotor_z_force_interpolator_from_stator_axial_load_interpolators(
        self: Self,
    ):
        """Method does not return."""
        self.wrapped.DeriveRotorZForceInterpolatorFromStatorAxialLoadInterpolators()

    def derive_stator_tangential_load_interpolators_from_torque_ripple_interpolators(
        self: Self,
    ):
        """Method does not return."""
        self.wrapped.DeriveStatorTangentialLoadInterpolatorsFromTorqueRippleInterpolators()

    def derive_torque_ripple_interpolator_from_stator_tangential_load_interpolators(
        self: Self,
    ):
        """Method does not return."""
        self.wrapped.DeriveTorqueRippleInterpolatorFromStatorTangentialLoadInterpolators()

    @enforce_parameter_types
    def multiple_fourier_series_interpolator_for(
        self: Self, harmonic_load_data_type: "_1389.HarmonicLoadDataType"
    ) -> "_1528.MultipleFourierSeriesInterpolator":
        """mastapy.math_utility.MultipleFourierSeriesInterpolator

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        method_result = self.wrapped.MultipleFourierSeriesInterpolatorFor.Overloads[
            _HARMONIC_LOAD_DATA_TYPE
        ](harmonic_load_data_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def multiple_fourier_series_interpolator_for_with_fe_node(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        node: "_2392.FESubstructureNode",
    ) -> "_1528.MultipleFourierSeriesInterpolator":
        """mastapy.math_utility.MultipleFourierSeriesInterpolator

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            node (mastapy.system_model.fe.FESubstructureNode)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        method_result = self.wrapped.MultipleFourierSeriesInterpolatorFor.Overloads[
            _HARMONIC_LOAD_DATA_TYPE, _FE_SUBSTRUCTURE_NODE
        ](harmonic_load_data_type, node.wrapped if node else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
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
    def cast_to(self: Self) -> "ElectricMachineDataSet._Cast_ElectricMachineDataSet":
        return self._Cast_ElectricMachineDataSet(self)
