"""DutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import _5668
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups", "DutyCycle"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import _5675, _5667
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7010,
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6813


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycle",)


Self = TypeVar("Self", bound="DutyCycle")


class DutyCycle(_5668.AbstractStaticLoadCaseGroup):
    """DutyCycle

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycle")

    class _Cast_DutyCycle:
        """Special nested class for casting DutyCycle to subclasses."""

        def __init__(self: "DutyCycle._Cast_DutyCycle", parent: "DutyCycle"):
            self._parent = parent

        @property
        def abstract_static_load_case_group(
            self: "DutyCycle._Cast_DutyCycle",
        ) -> "_5668.AbstractStaticLoadCaseGroup":
            return self._parent._cast(_5668.AbstractStaticLoadCaseGroup)

        @property
        def abstract_load_case_group(
            self: "DutyCycle._Cast_DutyCycle",
        ) -> "_5667.AbstractLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5667

            return self._parent._cast(_5667.AbstractLoadCaseGroup)

        @property
        def duty_cycle(self: "DutyCycle._Cast_DutyCycle") -> "DutyCycle":
            return self._parent

        def __getattr__(self: "DutyCycle._Cast_DutyCycle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_design_states(
        self: Self,
    ) -> "List[_5675.SubGroupInSingleDesignState]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.SubGroupInSingleDesignState]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleDesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def time_series_importer(self: Self) -> "_7010.TimeSeriesImporter":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.TimeSeriesImporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesImporter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def convert_to_condensed_parametric_study_tool_duty_cycle(self: Self):
        """Method does not return."""
        self.wrapped.ConvertToCondensedParametricStudyToolDutyCycle()

    @enforce_parameter_types
    def add_static_load(self: Self, static_load: "_6813.StaticLoadCase"):
        """Method does not return.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
        """
        self.wrapped.AddStaticLoad(static_load.wrapped if static_load else None)

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def remove_design_state_sub_group(
        self: Self, sub_group: "_5675.SubGroupInSingleDesignState"
    ):
        """Method does not return.

        Args:
            sub_group (mastapy.system_model.analyses_and_results.load_case_groups.SubGroupInSingleDesignState)
        """
        self.wrapped.RemoveDesignStateSubGroup(sub_group.wrapped if sub_group else None)

    @enforce_parameter_types
    def remove_static_load(self: Self, static_load: "_6813.StaticLoadCase"):
        """Method does not return.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
        """
        self.wrapped.RemoveStaticLoad(static_load.wrapped if static_load else None)

    @property
    def cast_to(self: Self) -> "DutyCycle._Cast_DutyCycle":
        return self._Cast_DutyCycle(self)
