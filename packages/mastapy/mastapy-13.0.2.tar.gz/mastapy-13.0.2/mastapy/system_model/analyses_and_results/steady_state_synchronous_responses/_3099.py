"""SteadyStateSynchronousResponseOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2479
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SteadyStateSynchronousResponseOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseOptions",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseOptions")


class SteadyStateSynchronousResponseOptions(_0.APIBase):
    """SteadyStateSynchronousResponseOptions

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseOptions"
    )

    class _Cast_SteadyStateSynchronousResponseOptions:
        """Special nested class for casting SteadyStateSynchronousResponseOptions to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseOptions._Cast_SteadyStateSynchronousResponseOptions",
            parent: "SteadyStateSynchronousResponseOptions",
        ):
            self._parent = parent

        @property
        def steady_state_synchronous_response_options(
            self: "SteadyStateSynchronousResponseOptions._Cast_SteadyStateSynchronousResponseOptions",
        ) -> "SteadyStateSynchronousResponseOptions":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseOptions._Cast_SteadyStateSynchronousResponseOptions",
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
        self: Self, instance_to_wrap: "SteadyStateSynchronousResponseOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def end_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndSpeed

        if temp is None:
            return 0.0

        return temp

    @end_speed.setter
    @enforce_parameter_types
    def end_speed(self: Self, value: "float"):
        self.wrapped.EndSpeed = float(value) if value is not None else 0.0

    @property
    def include_damping_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeDampingEffects

        if temp is None:
            return False

        return temp

    @include_damping_effects.setter
    @enforce_parameter_types
    def include_damping_effects(self: Self, value: "bool"):
        self.wrapped.IncludeDampingEffects = bool(value) if value is not None else False

    @property
    def include_disk_skew_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeDiskSkewEffects

        if temp is None:
            return False

        return temp

    @include_disk_skew_effects.setter
    @enforce_parameter_types
    def include_disk_skew_effects(self: Self, value: "bool"):
        self.wrapped.IncludeDiskSkewEffects = (
            bool(value) if value is not None else False
        )

    @property
    def include_gyroscopic_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGyroscopicEffects

        if temp is None:
            return False

        return temp

    @include_gyroscopic_effects.setter
    @enforce_parameter_types
    def include_gyroscopic_effects(self: Self, value: "bool"):
        self.wrapped.IncludeGyroscopicEffects = (
            bool(value) if value is not None else False
        )

    @property
    def include_shaft_bow_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeShaftBowEffects

        if temp is None:
            return False

        return temp

    @include_shaft_bow_effects.setter
    @enforce_parameter_types
    def include_shaft_bow_effects(self: Self, value: "bool"):
        self.wrapped.IncludeShaftBowEffects = (
            bool(value) if value is not None else False
        )

    @property
    def include_unbalanced_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeUnbalancedEffects

        if temp is None:
            return False

        return temp

    @include_unbalanced_effects.setter
    @enforce_parameter_types
    def include_unbalanced_effects(self: Self, value: "bool"):
        self.wrapped.IncludeUnbalancedEffects = (
            bool(value) if value is not None else False
        )

    @property
    def number_of_speeds(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSpeeds

        if temp is None:
            return 0

        return temp

    @number_of_speeds.setter
    @enforce_parameter_types
    def number_of_speeds(self: Self, value: "int"):
        self.wrapped.NumberOfSpeeds = int(value) if value is not None else 0

    @property
    def reference_power_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.ReferencePowerLoad

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @reference_power_load.setter
    @enforce_parameter_types
    def reference_power_load(self: Self, value: "_2479.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ReferencePowerLoad = value

    @property
    def start_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartSpeed

        if temp is None:
            return 0.0

        return temp

    @start_speed.setter
    @enforce_parameter_types
    def start_speed(self: Self, value: "float"):
        self.wrapped.StartSpeed = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseOptions._Cast_SteadyStateSynchronousResponseOptions":
        return self._Cast_SteadyStateSynchronousResponseOptions(self)
