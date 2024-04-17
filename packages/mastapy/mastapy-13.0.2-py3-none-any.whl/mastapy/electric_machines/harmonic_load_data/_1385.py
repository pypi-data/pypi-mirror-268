"""ElectricMachineHarmonicLoadDataBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.electric_machines.harmonic_load_data import _1389, _1386, _1390
from mastapy.electric_machines import _1302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_BASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData",
    "ElectricMachineHarmonicLoadDataBase",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1873, _1869
    from mastapy.math_utility import _1528
    from mastapy.electric_machines.harmonic_load_data import _1392, _1393, _1387
    from mastapy.electric_machines.results import _1328
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6880,
        _6881,
        _6882,
        _6883,
        _6884,
        _6885,
        _6886,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataBase",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataBase")


class ElectricMachineHarmonicLoadDataBase(_1390.SpeedDependentHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataBase")

    class _Cast_ElectricMachineHarmonicLoadDataBase:
        """Special nested class for casting ElectricMachineHarmonicLoadDataBase to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
            parent: "ElectricMachineHarmonicLoadDataBase",
        ):
            self._parent = parent

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_1328.DynamicForceResults":
            from mastapy.electric_machines.results import _1328

            return self._parent._cast(_1328.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6880.ElectricMachineHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6880

            return self._parent._cast(_6880.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6881.ElectricMachineHarmonicLoadDataFromExcel":
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6882.ElectricMachineHarmonicLoadDataFromFlux":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6883.ElectricMachineHarmonicLoadDataFromJMAG":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6884.ElectricMachineHarmonicLoadDataFromMASTA":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6885.ElectricMachineHarmonicLoadDataFromMotorCAD":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "_6886.ElectricMachineHarmonicLoadDataFromMotorPackages":
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(
                _6886.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
        ) -> "ElectricMachineHarmonicLoadDataBase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase",
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
        self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadDataBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads
        )

        if temp is None:
            return False

        return temp

    @compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads.setter
    @enforce_parameter_types
    def compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads(
        self: Self, value: "bool"
    ):
        self.wrapped.CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads = (
            bool(value) if value is not None else False
        )

    @property
    def data_type_for_force_moment_distribution_and_temporal_spatial_harmonics_charts(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType":
        """EnumWithSelectedValue[mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType]"""
        temp = (
            self.wrapped.DataTypeForForceMomentDistributionAndTemporalSpatialHarmonicsCharts
        )

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @data_type_for_force_moment_distribution_and_temporal_spatial_harmonics_charts.setter
    @enforce_parameter_types
    def data_type_for_force_moment_distribution_and_temporal_spatial_harmonics_charts(
        self: Self, value: "_1389.HarmonicLoadDataType"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataTypeForForceMomentDistributionAndTemporalSpatialHarmonicsCharts = (
            value
        )

    @property
    def display_interpolated_data(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DisplayInterpolatedData

        if temp is None:
            return False

        return temp

    @display_interpolated_data.setter
    @enforce_parameter_types
    def display_interpolated_data(self: Self, value: "bool"):
        self.wrapped.DisplayInterpolatedData = (
            bool(value) if value is not None else False
        )

    @property
    def display_option_for_slice_data(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption":
        """EnumWithSelectedValue[mastapy.electric_machines.harmonic_load_data.ForceDisplayOption]"""
        temp = self.wrapped.DisplayOptionForSliceData

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @display_option_for_slice_data.setter
    @enforce_parameter_types
    def display_option_for_slice_data(self: Self, value: "_1386.ForceDisplayOption"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DisplayOptionForSliceData = value

    @property
    def force_distribution_3d(self: Self) -> "_1873.ThreeDVectorChartDefinition":
        """mastapy.utility_gui.charts.ThreeDVectorChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceDistribution3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_moment_distribution(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceMomentDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def invert_axis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.InvertAxis

        if temp is None:
            return False

        return temp

    @invert_axis.setter
    @enforce_parameter_types
    def invert_axis(self: Self, value: "bool"):
        self.wrapped.InvertAxis = bool(value) if value is not None else False

    @property
    def plot_as_vectors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PlotAsVectors

        if temp is None:
            return False

        return temp

    @plot_as_vectors.setter
    @enforce_parameter_types
    def plot_as_vectors(self: Self, value: "bool"):
        self.wrapped.PlotAsVectors = bool(value) if value is not None else False

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
    def show_all_forces(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllForces

        if temp is None:
            return False

        return temp

    @show_all_forces.setter
    @enforce_parameter_types
    def show_all_forces(self: Self, value: "bool"):
        self.wrapped.ShowAllForces = bool(value) if value is not None else False

    @property
    def show_all_teeth(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllTeeth

        if temp is None:
            return False

        return temp

    @show_all_teeth.setter
    @enforce_parameter_types
    def show_all_teeth(self: Self, value: "bool"):
        self.wrapped.ShowAllTeeth = bool(value) if value is not None else False

    @property
    def slice(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_RotorSkewSlice":
        """ListWithSelectedItem[mastapy.electric_machines.RotorSkewSlice]"""
        temp = self.wrapped.Slice

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_RotorSkewSlice",
        )(temp)

    @slice.setter
    @enforce_parameter_types
    def slice(self: Self, value: "_1302.RotorSkewSlice"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Slice = value

    @property
    def speed_to_view(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpeedToView

        if temp is None:
            return 0.0

        return temp

    @speed_to_view.setter
    @enforce_parameter_types
    def speed_to_view(self: Self, value: "float"):
        self.wrapped.SpeedToView = float(value) if value is not None else 0.0

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
    def sum_over_all_nodes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SumOverAllNodes

        if temp is None:
            return False

        return temp

    @sum_over_all_nodes.setter
    @enforce_parameter_types
    def sum_over_all_nodes(self: Self, value: "bool"):
        self.wrapped.SumOverAllNodes = bool(value) if value is not None else False

    @property
    def temporal_spatial_harmonics_chart(self: Self) -> "_1869.ScatterChartDefinition":
        """mastapy.utility_gui.charts.ScatterChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemporalSpatialHarmonicsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def use_log_scale_for_temporal_spatial_harmonics_chart(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseLogScaleForTemporalSpatialHarmonicsChart

        if temp is None:
            return False

        return temp

    @use_log_scale_for_temporal_spatial_harmonics_chart.setter
    @enforce_parameter_types
    def use_log_scale_for_temporal_spatial_harmonics_chart(self: Self, value: "bool"):
        self.wrapped.UseLogScaleForTemporalSpatialHarmonicsChart = (
            bool(value) if value is not None else False
        )

    @property
    def rotor_x_force(self: Self) -> "_1528.MultipleFourierSeriesInterpolator":
        """mastapy.math_utility.MultipleFourierSeriesInterpolator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorXForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor_y_force(self: Self) -> "_1528.MultipleFourierSeriesInterpolator":
        """mastapy.math_utility.MultipleFourierSeriesInterpolator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorYForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_axial_loads(self: Self) -> "_1392.StatorToothLoadInterpolator":
        """mastapy.electric_machines.harmonic_load_data.StatorToothLoadInterpolator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorAxialLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_radial_loads(self: Self) -> "_1392.StatorToothLoadInterpolator":
        """mastapy.electric_machines.harmonic_load_data.StatorToothLoadInterpolator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorRadialLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_tangential_loads(self: Self) -> "_1392.StatorToothLoadInterpolator":
        """mastapy.electric_machines.harmonic_load_data.StatorToothLoadInterpolator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorTangentialLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_tooth_moments(self: Self) -> "_1393.StatorToothMomentInterpolator":
        """mastapy.electric_machines.harmonic_load_data.StatorToothMomentInterpolator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorToothMoments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def multiple_fourier_series_interpolator_for(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        slice_index: "int",
    ) -> "_1528.MultipleFourierSeriesInterpolator":
        """mastapy.math_utility.MultipleFourierSeriesInterpolator

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            slice_index (int)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        slice_index = int(slice_index)
        method_result = self.wrapped.MultipleFourierSeriesInterpolatorFor(
            harmonic_load_data_type, slice_index if slice_index else 0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def stator_tooth_load_interpolator_for(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        slice_index: "int",
    ) -> "_1392.StatorToothLoadInterpolator":
        """mastapy.electric_machines.harmonic_load_data.StatorToothLoadInterpolator

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            slice_index (int)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        slice_index = int(slice_index)
        method_result = self.wrapped.StatorToothLoadInterpolatorFor(
            harmonic_load_data_type, slice_index if slice_index else 0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def stator_tooth_moment_interpolator_for(
        self: Self,
        harmonic_load_data_type: "_1389.HarmonicLoadDataType",
        slice_index: "int",
    ) -> "_1393.StatorToothMomentInterpolator":
        """mastapy.electric_machines.harmonic_load_data.StatorToothMomentInterpolator

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            slice_index (int)
        """
        harmonic_load_data_type = conversion.mp_to_pn_enum(
            harmonic_load_data_type,
            "SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType",
        )
        slice_index = int(slice_index)
        method_result = self.wrapped.StatorToothMomentInterpolatorFor(
            harmonic_load_data_type, slice_index if slice_index else 0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase"
    ):
        return self._Cast_ElectricMachineHarmonicLoadDataBase(self)
