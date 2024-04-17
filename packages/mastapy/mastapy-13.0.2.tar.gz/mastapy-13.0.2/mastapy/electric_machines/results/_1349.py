"""NonLinearDQModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines.results import _1330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "NonLinearDQModel"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1872, _1874
    from mastapy.electric_machines.results import _1350


__docformat__ = "restructuredtext en"
__all__ = ("NonLinearDQModel",)


Self = TypeVar("Self", bound="NonLinearDQModel")


class NonLinearDQModel(_1330.ElectricMachineDQModel):
    """NonLinearDQModel

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonLinearDQModel")

    class _Cast_NonLinearDQModel:
        """Special nested class for casting NonLinearDQModel to subclasses."""

        def __init__(
            self: "NonLinearDQModel._Cast_NonLinearDQModel", parent: "NonLinearDQModel"
        ):
            self._parent = parent

        @property
        def electric_machine_dq_model(
            self: "NonLinearDQModel._Cast_NonLinearDQModel",
        ) -> "_1330.ElectricMachineDQModel":
            return self._parent._cast(_1330.ElectricMachineDQModel)

        @property
        def non_linear_dq_model(
            self: "NonLinearDQModel._Cast_NonLinearDQModel",
        ) -> "NonLinearDQModel":
            return self._parent

        def __getattr__(self: "NonLinearDQModel._Cast_NonLinearDQModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonLinearDQModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ac_winding_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ACWindingLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def alignment_torque_map_at_reference_temperatures(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlignmentTorqueMapAtReferenceTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def d_axis_armature_flux_linkage_map(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisArmatureFluxLinkageMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def number_of_current_angle_values(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCurrentAngleValues

        if temp is None:
            return 0

        return temp

    @property
    def number_of_current_values(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCurrentValues

        if temp is None:
            return 0

        return temp

    @property
    def q_axis_armature_flux_linkage_map(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisArmatureFluxLinkageMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reluctance_torque_map_at_reference_temperatures(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReluctanceTorqueMapAtReferenceTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor_eddy_current_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorEddyCurrentLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor_excess_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorExcessLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor_hysteresis_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorHysteresisLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_eddy_current_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorEddyCurrentLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_excess_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorExcessLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_hysteresis_loss_per_frequency_exponent_map(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorHysteresisLossPerFrequencyExponentMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_taken_to_generate_non_linear_dq_model(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeTakenToGenerateNonLinearDQModel

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_map_at_reference_temperatures(
        self: Self,
    ) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueMapAtReferenceTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def torque_at_max_current_and_reference_temperatures(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueAtMaxCurrentAndReferenceTemperatures

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
    def cast_to(self: Self) -> "NonLinearDQModel._Cast_NonLinearDQModel":
        return self._Cast_NonLinearDQModel(self)
