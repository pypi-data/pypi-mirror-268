"""AdvancedSystemDeflectionOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.gears import _2539
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AdvancedSystemDeflectionOptions",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _853
    from mastapy.system_model.analyses_and_results import _2692


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedSystemDeflectionOptions",)


Self = TypeVar("Self", bound="AdvancedSystemDeflectionOptions")


class AdvancedSystemDeflectionOptions(_0.APIBase):
    """AdvancedSystemDeflectionOptions

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdvancedSystemDeflectionOptions")

    class _Cast_AdvancedSystemDeflectionOptions:
        """Special nested class for casting AdvancedSystemDeflectionOptions to subclasses."""

        def __init__(
            self: "AdvancedSystemDeflectionOptions._Cast_AdvancedSystemDeflectionOptions",
            parent: "AdvancedSystemDeflectionOptions",
        ):
            self._parent = parent

        @property
        def advanced_system_deflection_options(
            self: "AdvancedSystemDeflectionOptions._Cast_AdvancedSystemDeflectionOptions",
        ) -> "AdvancedSystemDeflectionOptions":
            return self._parent

        def __getattr__(
            self: "AdvancedSystemDeflectionOptions._Cast_AdvancedSystemDeflectionOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdvancedSystemDeflectionOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_pitch_error(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludePitchError

        if temp is None:
            return False

        return temp

    @include_pitch_error.setter
    @enforce_parameter_types
    def include_pitch_error(self: Self, value: "bool"):
        self.wrapped.IncludePitchError = bool(value) if value is not None else False

    @property
    def run_for_single_gear_set(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RunForSingleGearSet

        if temp is None:
            return False

        return temp

    @run_for_single_gear_set.setter
    @enforce_parameter_types
    def run_for_single_gear_set(self: Self, value: "bool"):
        self.wrapped.RunForSingleGearSet = bool(value) if value is not None else False

    @property
    def seed_analysis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SeedAnalysis

        if temp is None:
            return False

        return temp

    @seed_analysis.setter
    @enforce_parameter_types
    def seed_analysis(self: Self, value: "bool"):
        self.wrapped.SeedAnalysis = bool(value) if value is not None else False

    @property
    def specified_gear_set(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_GearSet":
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.GearSet]"""
        temp = self.wrapped.SpecifiedGearSet

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GearSet",
        )(temp)

    @specified_gear_set.setter
    @enforce_parameter_types
    def specified_gear_set(self: Self, value: "_2539.GearSet"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GearSet.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GearSet.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SpecifiedGearSet = value

    @property
    def total_number_of_time_steps(self: Self) -> "int":
        """int"""
        temp = self.wrapped.TotalNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @total_number_of_time_steps.setter
    @enforce_parameter_types
    def total_number_of_time_steps(self: Self, value: "int"):
        self.wrapped.TotalNumberOfTimeSteps = int(value) if value is not None else 0

    @property
    def use_advanced_ltca(self: Self) -> "_853.UseAdvancedLTCAOptions":
        """mastapy.gears.ltca.UseAdvancedLTCAOptions"""
        temp = self.wrapped.UseAdvancedLTCA

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.LTCA.UseAdvancedLTCAOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.ltca._853", "UseAdvancedLTCAOptions"
        )(value)

    @use_advanced_ltca.setter
    @enforce_parameter_types
    def use_advanced_ltca(self: Self, value: "_853.UseAdvancedLTCAOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.LTCA.UseAdvancedLTCAOptions"
        )
        self.wrapped.UseAdvancedLTCA = value

    @property
    def use_data_logger(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDataLogger

        if temp is None:
            return False

        return temp

    @use_data_logger.setter
    @enforce_parameter_types
    def use_data_logger(self: Self, value: "bool"):
        self.wrapped.UseDataLogger = bool(value) if value is not None else False

    @property
    def time_options(self: Self) -> "_2692.TimeOptions":
        """mastapy.system_model.analyses_and_results.TimeOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedSystemDeflectionOptions._Cast_AdvancedSystemDeflectionOptions":
        return self._Cast_AdvancedSystemDeflectionOptions(self)
