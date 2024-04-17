"""SynchroniserShift"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.load_case_groups import _5671
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SHIFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SynchroniserAnalysis",
    "SynchroniserShift",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612, _2614


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserShift",)


Self = TypeVar("Self", bound="SynchroniserShift")


class SynchroniserShift(_0.APIBase):
    """SynchroniserShift

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SHIFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserShift")

    class _Cast_SynchroniserShift:
        """Special nested class for casting SynchroniserShift to subclasses."""

        def __init__(
            self: "SynchroniserShift._Cast_SynchroniserShift",
            parent: "SynchroniserShift",
        ):
            self._parent = parent

        @property
        def synchroniser_shift(
            self: "SynchroniserShift._Cast_SynchroniserShift",
        ) -> "SynchroniserShift":
            return self._parent

        def __getattr__(self: "SynchroniserShift._Cast_SynchroniserShift", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserShift.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_inertia(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClutchInertia

        if temp is None:
            return 0.0

        return temp

    @clutch_inertia.setter
    @enforce_parameter_types
    def clutch_inertia(self: Self, value: "float"):
        self.wrapped.ClutchInertia = float(value) if value is not None else 0.0

    @property
    def cone_normal_pressure_when_all_cones_take_equal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConeNormalPressureWhenAllConesTakeEqualForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cone_torque_index_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConeTorqueIndexTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def downstream_component(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DownstreamComponent

        if temp is None:
            return ""

        return temp

    @property
    def engine_power_load_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnginePowerLoadName

        if temp is None:
            return ""

        return temp

    @property
    def final_design_state(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_DesignState":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.load_case_groups.DesignState]"""
        temp = self.wrapped.FinalDesignState

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_DesignState",
        )(temp)

    @final_design_state.setter
    @enforce_parameter_types
    def final_design_state(self: Self, value: "_5671.DesignState"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_DesignState.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_DesignState.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.FinalDesignState = value

    @property
    def final_synchronised_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinalSynchronisedSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_energy_per_area_for_shift_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalEnergyPerAreaForShiftTime

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_work(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalWork

        if temp is None:
            return 0.0

        return temp

    @property
    def hand_ball_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HandBallForce

        if temp is None:
            return 0.0

        return temp

    @hand_ball_force.setter
    @enforce_parameter_types
    def hand_ball_force(self: Self, value: "float"):
        self.wrapped.HandBallForce = float(value) if value is not None else 0.0

    @property
    def hand_ball_impulse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HandBallImpulse

        if temp is None:
            return 0.0

        return temp

    @property
    def indexing_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IndexingTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def initial_design_state(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_DesignState":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.load_case_groups.DesignState]"""
        temp = self.wrapped.InitialDesignState

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_DesignState",
        )(temp)

    @initial_design_state.setter
    @enforce_parameter_types
    def initial_design_state(self: Self, value: "_5671.DesignState"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_DesignState.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_DesignState.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.InitialDesignState = value

    @property
    def initial_downstream_component_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InitialDownstreamComponentSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def initial_engine_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialEngineSpeed

        if temp is None:
            return 0.0

        return temp

    @initial_engine_speed.setter
    @enforce_parameter_types
    def initial_engine_speed(self: Self, value: "float"):
        self.wrapped.InitialEngineSpeed = float(value) if value is not None else 0.0

    @property
    def initial_upstream_component_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InitialUpstreamComponentSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_cone_normal_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumConeNormalPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_frictional_power_for_shift_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanFrictionalPowerForShiftTime

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_frictional_power_per_area_for_shift_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanFrictionalPowerPerAreaForShiftTime

        if temp is None:
            return 0.0

        return temp

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
    def shift_mechanism_efficiency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShiftMechanismEfficiency

        if temp is None:
            return 0.0

        return temp

    @shift_mechanism_efficiency.setter
    @enforce_parameter_types
    def shift_mechanism_efficiency(self: Self, value: "float"):
        self.wrapped.ShiftMechanismEfficiency = (
            float(value) if value is not None else 0.0
        )

    @property
    def shift_mechanism_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShiftMechanismRatio

        if temp is None:
            return 0.0

        return temp

    @shift_mechanism_ratio.setter
    @enforce_parameter_types
    def shift_mechanism_ratio(self: Self, value: "float"):
        self.wrapped.ShiftMechanismRatio = float(value) if value is not None else 0.0

    @property
    def shift_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShiftTime

        if temp is None:
            return 0.0

        return temp

    @shift_time.setter
    @enforce_parameter_types
    def shift_time(self: Self, value: "float"):
        self.wrapped.ShiftTime = float(value) if value is not None else 0.0

    @property
    def sleeve_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SleeveAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def sleeve_impulse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SleeveImpulse

        if temp is None:
            return 0.0

        return temp

    @property
    def slipping_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlippingVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def synchronisation_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SynchronisationTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def time_specified(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TimeSpecified

        if temp is None:
            return False

        return temp

    @time_specified.setter
    @enforce_parameter_types
    def time_specified(self: Self, value: "bool"):
        self.wrapped.TimeSpecified = bool(value) if value is not None else False

    @property
    def total_normal_force_on_cones(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalNormalForceOnCones

        if temp is None:
            return 0.0

        return temp

    @property
    def upstream_component(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpstreamComponent

        if temp is None:
            return ""

        return temp

    @property
    def upstream_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpstreamInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def cone(self: Self) -> "_2612.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cone

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sleeve(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Sleeve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "SynchroniserShift._Cast_SynchroniserShift":
        return self._Cast_SynchroniserShift(self)
