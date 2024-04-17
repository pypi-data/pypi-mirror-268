"""RootAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6827
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RootAssemblyLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.nodal_analysis.varying_input_components import _98, _97, _102
    from mastapy.math_utility.control import _1583
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6813,
        _6874,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyLoadCase",)


Self = TypeVar("Self", bound="RootAssemblyLoadCase")


class RootAssemblyLoadCase(_6827.AssemblyLoadCase):
    """RootAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyLoadCase")

    class _Cast_RootAssemblyLoadCase:
        """Special nested class for casting RootAssemblyLoadCase to subclasses."""

        def __init__(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
            parent: "RootAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def assembly_load_case(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "_6827.AssemblyLoadCase":
            return self._parent._cast(_6827.AssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_load_case(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase",
        ) -> "RootAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def brake_force_gain(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BrakeForceGain

        if temp is None:
            return 0.0

        return temp

    @brake_force_gain.setter
    @enforce_parameter_types
    def brake_force_gain(self: Self, value: "float"):
        self.wrapped.BrakeForceGain = float(value) if value is not None else 0.0

    @property
    def max_brake_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaxBrakeForce

        if temp is None:
            return 0.0

        return temp

    @max_brake_force.setter
    @enforce_parameter_types
    def max_brake_force(self: Self, value: "float"):
        self.wrapped.MaxBrakeForce = float(value) if value is not None else 0.0

    @property
    def oil_initial_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilInitialTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_initial_temperature.setter
    @enforce_parameter_types
    def oil_initial_temperature(self: Self, value: "float"):
        self.wrapped.OilInitialTemperature = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_alpha(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingAlpha

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_alpha.setter
    @enforce_parameter_types
    def rayleigh_damping_alpha(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingAlpha = value

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
    def brake_force_input_values(self: Self) -> "_98.ForceInputComponent":
        """mastapy.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BrakeForceInputValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def drive_cycle_pid_control_settings(self: Self) -> "_1583.PIDControlSettings":
        """mastapy.math_utility.control.PIDControlSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DriveCyclePIDControlSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case(self: Self) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def road_incline_input_values(self: Self) -> "_97.AngleInputComponent":
        """mastapy.nodal_analysis.varying_input_components.AngleInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoadInclineInputValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def target_vehicle_speed(self: Self) -> "_102.VelocityInputComponent":
        """mastapy.nodal_analysis.varying_input_components.VelocityInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TargetVehicleSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def supercharger_rotor_sets(self: Self) -> "List[_6874.CylindricalGearSetLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerRotorSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "RootAssemblyLoadCase._Cast_RootAssemblyLoadCase":
        return self._Cast_RootAssemblyLoadCase(self)
