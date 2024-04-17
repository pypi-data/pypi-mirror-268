"""MBDAnalysisOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import (
    overridable,
    enum_with_selected_value,
    list_with_selected_item,
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.mbd_analyses import _5394, _5446, _5492
from mastapy.system_model.part_model import _2479
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MBD_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "MBDAnalysisOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5391,
        _5453,
        _5454,
        _5470,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses.external_interfaces import (
        _5536,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import _4642
    from mastapy.nodal_analysis import _91


__docformat__ = "restructuredtext en"
__all__ = ("MBDAnalysisOptions",)


Self = TypeVar("Self", bound="MBDAnalysisOptions")


class MBDAnalysisOptions(_0.APIBase):
    """MBDAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _MBD_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MBDAnalysisOptions")

    class _Cast_MBDAnalysisOptions:
        """Special nested class for casting MBDAnalysisOptions to subclasses."""

        def __init__(
            self: "MBDAnalysisOptions._Cast_MBDAnalysisOptions",
            parent: "MBDAnalysisOptions",
        ):
            self._parent = parent

        @property
        def mbd_analysis_options(
            self: "MBDAnalysisOptions._Cast_MBDAnalysisOptions",
        ) -> "MBDAnalysisOptions":
            return self._parent

        def __getattr__(self: "MBDAnalysisOptions._Cast_MBDAnalysisOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MBDAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_type(self: Self) -> "_5391.AnalysisTypes":
        """mastapy.system_model.analyses_and_results.mbd_analyses.AnalysisTypes"""
        temp = self.wrapped.AnalysisType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.AnalysisTypes",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5391",
            "AnalysisTypes",
        )(value)

    @analysis_type.setter
    @enforce_parameter_types
    def analysis_type(self: Self, value: "_5391.AnalysisTypes"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.AnalysisTypes",
        )
        self.wrapped.AnalysisType = value

    @property
    def bearing_rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingRayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_rayleigh_damping_beta.setter
    @enforce_parameter_types
    def bearing_rayleigh_damping_beta(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingRayleighDampingBeta = value

    @property
    def bearing_stiffness_model(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BearingStiffnessModel":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.mbd_analyses.BearingStiffnessModel]"""
        temp = self.wrapped.BearingStiffnessModel

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BearingStiffnessModel.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @bearing_stiffness_model.setter
    @enforce_parameter_types
    def bearing_stiffness_model(self: Self, value: "_5394.BearingStiffnessModel"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BearingStiffnessModel.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingStiffnessModel = value

    @property
    def belt_rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BeltRayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @belt_rayleigh_damping_beta.setter
    @enforce_parameter_types
    def belt_rayleigh_damping_beta(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BeltRayleighDampingBeta = value

    @property
    def create_inertia_adjusted_static_load_cases(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateInertiaAdjustedStaticLoadCases

        if temp is None:
            return False

        return temp

    @create_inertia_adjusted_static_load_cases.setter
    @enforce_parameter_types
    def create_inertia_adjusted_static_load_cases(self: Self, value: "bool"):
        self.wrapped.CreateInertiaAdjustedStaticLoadCases = (
            bool(value) if value is not None else False
        )

    @property
    def filter_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilterCutOff

        if temp is None:
            return 0.0

        return temp

    @filter_cut_off.setter
    @enforce_parameter_types
    def filter_cut_off(self: Self, value: "float"):
        self.wrapped.FilterCutOff = float(value) if value is not None else 0.0

    @property
    def gear_mesh_rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GearMeshRayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @gear_mesh_rayleigh_damping_beta.setter
    @enforce_parameter_types
    def gear_mesh_rayleigh_damping_beta(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GearMeshRayleighDampingBeta = value

    @property
    def gear_mesh_stiffness_model(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_GearMeshStiffnessModel":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshStiffnessModel]"""
        temp = self.wrapped.GearMeshStiffnessModel

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_GearMeshStiffnessModel.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @gear_mesh_stiffness_model.setter
    @enforce_parameter_types
    def gear_mesh_stiffness_model(self: Self, value: "_5446.GearMeshStiffnessModel"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_GearMeshStiffnessModel.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.GearMeshStiffnessModel = value

    @property
    def include_gear_backlash(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGearBacklash

        if temp is None:
            return False

        return temp

    @include_gear_backlash.setter
    @enforce_parameter_types
    def include_gear_backlash(self: Self, value: "bool"):
        self.wrapped.IncludeGearBacklash = bool(value) if value is not None else False

    @property
    def include_microgeometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeMicrogeometry

        if temp is None:
            return False

        return temp

    @include_microgeometry.setter
    @enforce_parameter_types
    def include_microgeometry(self: Self, value: "bool"):
        self.wrapped.IncludeMicrogeometry = bool(value) if value is not None else False

    @property
    def include_shaft_and_housing_flexibilities(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ShaftAndHousingFlexibilityOption":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftAndHousingFlexibilityOption]"""
        temp = self.wrapped.IncludeShaftAndHousingFlexibilities

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftAndHousingFlexibilityOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @include_shaft_and_housing_flexibilities.setter
    @enforce_parameter_types
    def include_shaft_and_housing_flexibilities(
        self: Self, value: "_5492.ShaftAndHousingFlexibilityOption"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftAndHousingFlexibilityOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.IncludeShaftAndHousingFlexibilities = value

    @property
    def interference_fit_rayleigh_damping_beta(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InterferenceFitRayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @interference_fit_rayleigh_damping_beta.setter
    @enforce_parameter_types
    def interference_fit_rayleigh_damping_beta(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InterferenceFitRayleighDampingBeta = value

    @property
    def load_case_for_component_speed_ratios(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.LoadCaseForComponentSpeedRatios

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @load_case_for_component_speed_ratios.setter
    @enforce_parameter_types
    def load_case_for_component_speed_ratios(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.LoadCaseForComponentSpeedRatios = value

    @property
    def load_case_for_linearised_bearing_stiffness(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.LoadCaseForLinearisedBearingStiffness

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @load_case_for_linearised_bearing_stiffness.setter
    @enforce_parameter_types
    def load_case_for_linearised_bearing_stiffness(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.LoadCaseForLinearisedBearingStiffness = value

    @property
    def maximum_angular_jerk(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumAngularJerk

        if temp is None:
            return 0.0

        return temp

    @maximum_angular_jerk.setter
    @enforce_parameter_types
    def maximum_angular_jerk(self: Self, value: "float"):
        self.wrapped.MaximumAngularJerk = float(value) if value is not None else 0.0

    @property
    def maximum_frequency_in_signal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumFrequencyInSignal

        if temp is None:
            return 0.0

        return temp

    @maximum_frequency_in_signal.setter
    @enforce_parameter_types
    def maximum_frequency_in_signal(self: Self, value: "float"):
        self.wrapped.MaximumFrequencyInSignal = (
            float(value) if value is not None else 0.0
        )

    @property
    def method_to_define_period(
        self: Self,
    ) -> "_5453.InertiaAdjustedLoadCasePeriodMethod":
        """mastapy.system_model.analyses_and_results.mbd_analyses.InertiaAdjustedLoadCasePeriodMethod"""
        temp = self.wrapped.MethodToDefinePeriod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InertiaAdjustedLoadCasePeriodMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5453",
            "InertiaAdjustedLoadCasePeriodMethod",
        )(value)

    @method_to_define_period.setter
    @enforce_parameter_types
    def method_to_define_period(
        self: Self, value: "_5453.InertiaAdjustedLoadCasePeriodMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InertiaAdjustedLoadCasePeriodMethod",
        )
        self.wrapped.MethodToDefinePeriod = value

    @property
    def number_of_static_load_cases(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStaticLoadCases

        if temp is None:
            return 0

        return temp

    @number_of_static_load_cases.setter
    @enforce_parameter_types
    def number_of_static_load_cases(self: Self, value: "int"):
        self.wrapped.NumberOfStaticLoadCases = int(value) if value is not None else 0

    @property
    def power_load_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PowerLoadRotation

        if temp is None:
            return 0.0

        return temp

    @power_load_rotation.setter
    @enforce_parameter_types
    def power_load_rotation(self: Self, value: "float"):
        self.wrapped.PowerLoadRotation = float(value) if value is not None else 0.0

    @property
    def reference_power_load_to_define_period(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.ReferencePowerLoadToDefinePeriod

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @reference_power_load_to_define_period.setter
    @enforce_parameter_types
    def reference_power_load_to_define_period(self: Self, value: "_2479.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ReferencePowerLoadToDefinePeriod = value

    @property
    def sample_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SampleLength

        if temp is None:
            return 0.0

        return temp

    @sample_length.setter
    @enforce_parameter_types
    def sample_length(self: Self, value: "float"):
        self.wrapped.SampleLength = float(value) if value is not None else 0.0

    @property
    def shaft_and_housing_rayleigh_damping_beta(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ShaftAndHousingRayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @shaft_and_housing_rayleigh_damping_beta.setter
    @enforce_parameter_types
    def shaft_and_housing_rayleigh_damping_beta(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ShaftAndHousingRayleighDampingBeta = value

    @property
    def spline_rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SplineRayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @spline_rayleigh_damping_beta.setter
    @enforce_parameter_types
    def spline_rayleigh_damping_beta(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SplineRayleighDampingBeta = value

    @property
    def start_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartTime

        if temp is None:
            return 0.0

        return temp

    @start_time.setter
    @enforce_parameter_types
    def start_time(self: Self, value: "float"):
        self.wrapped.StartTime = float(value) if value is not None else 0.0

    @property
    def start_at_zero_angle(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.StartAtZeroAngle

        if temp is None:
            return False

        return temp

    @start_at_zero_angle.setter
    @enforce_parameter_types
    def start_at_zero_angle(self: Self, value: "bool"):
        self.wrapped.StartAtZeroAngle = bool(value) if value is not None else False

    @property
    def static_load_cases_to_create(
        self: Self,
    ) -> "_5454.InertiaAdjustedLoadCaseResultsToCreate":
        """mastapy.system_model.analyses_and_results.mbd_analyses.InertiaAdjustedLoadCaseResultsToCreate"""
        temp = self.wrapped.StaticLoadCasesToCreate

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InertiaAdjustedLoadCaseResultsToCreate",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5454",
            "InertiaAdjustedLoadCaseResultsToCreate",
        )(value)

    @static_load_cases_to_create.setter
    @enforce_parameter_types
    def static_load_cases_to_create(
        self: Self, value: "_5454.InertiaAdjustedLoadCaseResultsToCreate"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InertiaAdjustedLoadCaseResultsToCreate",
        )
        self.wrapped.StaticLoadCasesToCreate = value

    @property
    def use_load_sensitive_stiffness(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseLoadSensitiveStiffness

        if temp is None:
            return False

        return temp

    @use_load_sensitive_stiffness.setter
    @enforce_parameter_types
    def use_load_sensitive_stiffness(self: Self, value: "bool"):
        self.wrapped.UseLoadSensitiveStiffness = (
            bool(value) if value is not None else False
        )

    @property
    def use_temperature_model(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseTemperatureModel

        if temp is None:
            return False

        return temp

    @use_temperature_model.setter
    @enforce_parameter_types
    def use_temperature_model(self: Self, value: "bool"):
        self.wrapped.UseTemperatureModel = bool(value) if value is not None else False

    @property
    def external_interface_options(
        self: Self,
    ) -> "_5536.DynamicExternalInterfaceOptions":
        """mastapy.system_model.analyses_and_results.mbd_analyses.external_interfaces.DynamicExternalInterfaceOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalInterfaceOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def frequency_response_options(
        self: Self,
    ) -> "_4642.FrequencyResponseAnalysisOptions":
        """mastapy.system_model.analyses_and_results.modal_analyses.FrequencyResponseAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyResponseOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def run_up_analysis_options(self: Self) -> "_5470.MBDRunUpAnalysisOptions":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MBDRunUpAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunUpAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transient_solver_options(self: Self) -> "_91.TransientSolverOptions":
        """mastapy.nodal_analysis.TransientSolverOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransientSolverOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "MBDAnalysisOptions._Cast_MBDAnalysisOptions":
        return self._Cast_MBDAnalysisOptions(self)
