"""RootAssemblyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RootAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5473,
        _5384,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyMultibodyDynamicsAnalysis")


class RootAssemblyMultibodyDynamicsAnalysis(_5392.AssemblyMultibodyDynamicsAnalysis):
    """RootAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_RootAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting RootAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
            parent: "RootAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_multibody_dynamics_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5392.AssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(_5392.AssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
        ) -> "RootAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_torque_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualTorqueRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def actual_torque_ratio_turbine_to_output(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualTorqueRatioTurbineToOutput

        if temp is None:
            return 0.0

        return temp

    @property
    def brake_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BrakeForce

        if temp is None:
            return 0.0

        return temp

    @brake_force.setter
    @enforce_parameter_types
    def brake_force(self: Self, value: "float"):
        self.wrapped.BrakeForce = float(value) if value is not None else 0.0

    @property
    def current_target_vehicle_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentTargetVehicleSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_lost(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLost

        if temp is None:
            return 0.0

        return temp

    @property
    def force_from_road_incline(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceFromRoadIncline

        if temp is None:
            return 0.0

        return temp

    @property
    def force_from_wheels(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceFromWheels

        if temp is None:
            return 0.0

        return temp

    @property
    def input_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def input_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def log_10_time_step(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Log10TimeStep

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_vehicle_speed_error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVehicleSpeedError

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_dynamic_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilDynamicTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_error_in_vehicle_speed_compared_to_drive_cycle(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageErrorInVehicleSpeedComparedToDriveCycle

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def road_incline(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RoadIncline

        if temp is None:
            return 0.0

        return temp

    @road_incline.setter
    @enforce_parameter_types
    def road_incline(self: Self, value: "float"):
        self.wrapped.RoadIncline = float(value) if value is not None else 0.0

    @property
    def total_force_on_vehicle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalForceOnVehicle

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_acceleration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehicleAcceleration

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_drag(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehicleDrag

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_position(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehiclePosition

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehicleSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_speed_drive_cycle_error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehicleSpeedDriveCycleError

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_design(self: Self) -> "_2481.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def multibody_dynamics_analysis_inputs(
        self: Self,
    ) -> "_5473.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyMultibodyDynamicsAnalysis._Cast_RootAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_RootAssemblyMultibodyDynamicsAnalysis(self)
