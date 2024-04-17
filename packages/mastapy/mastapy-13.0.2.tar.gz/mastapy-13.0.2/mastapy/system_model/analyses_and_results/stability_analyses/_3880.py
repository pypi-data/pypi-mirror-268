"""StabilityAnalysisOptions"""

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

_STABILITY_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StabilityAnalysisOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("StabilityAnalysisOptions",)


Self = TypeVar("Self", bound="StabilityAnalysisOptions")


class StabilityAnalysisOptions(_0.APIBase):
    """StabilityAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StabilityAnalysisOptions")

    class _Cast_StabilityAnalysisOptions:
        """Special nested class for casting StabilityAnalysisOptions to subclasses."""

        def __init__(
            self: "StabilityAnalysisOptions._Cast_StabilityAnalysisOptions",
            parent: "StabilityAnalysisOptions",
        ):
            self._parent = parent

        @property
        def stability_analysis_options(
            self: "StabilityAnalysisOptions._Cast_StabilityAnalysisOptions",
        ) -> "StabilityAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "StabilityAnalysisOptions._Cast_StabilityAnalysisOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StabilityAnalysisOptions.TYPE"):
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
    def number_of_modes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfModes

        if temp is None:
            return 0

        return temp

    @number_of_modes.setter
    @enforce_parameter_types
    def number_of_modes(self: Self, value: "int"):
        self.wrapped.NumberOfModes = int(value) if value is not None else 0

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
    def sort_modes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SortModes

        if temp is None:
            return False

        return temp

    @sort_modes.setter
    @enforce_parameter_types
    def sort_modes(self: Self, value: "bool"):
        self.wrapped.SortModes = bool(value) if value is not None else False

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
    ) -> "StabilityAnalysisOptions._Cast_StabilityAnalysisOptions":
        return self._Cast_StabilityAnalysisOptions(self)
