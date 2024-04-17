"""ConceptCouplingLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2479
from mastapy.system_model.analyses_and_results.static_loads import _6862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptCouplingLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model import _2209
    from mastapy.math_utility import _1542
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.math_utility.control import _1583
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingLoadCase",)


Self = TypeVar("Self", bound="ConceptCouplingLoadCase")


class ConceptCouplingLoadCase(_6862.CouplingLoadCase):
    """ConceptCouplingLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingLoadCase")

    class _Cast_ConceptCouplingLoadCase:
        """Special nested class for casting ConceptCouplingLoadCase to subclasses."""

        def __init__(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
            parent: "ConceptCouplingLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_load_case(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_6862.CouplingLoadCase":
            return self._parent._cast(_6862.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_load_case(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase",
        ) -> "ConceptCouplingLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def efficiency(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @efficiency.setter
    @enforce_parameter_types
    def efficiency(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Efficiency = value

    @property
    def power_load_for_reference_speed(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.PowerLoadForReferenceSpeed

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @power_load_for_reference_speed.setter
    @enforce_parameter_types
    def power_load_for_reference_speed(self: Self, value: "_2479.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.PowerLoadForReferenceSpeed = value

    @property
    def speed_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @speed_ratio.setter
    @enforce_parameter_types
    def speed_ratio(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpeedRatio = value

    @property
    def speed_ratio_specification_method(
        self: Self,
    ) -> "_2209.ConceptCouplingSpeedRatioSpecificationMethod":
        """mastapy.system_model.ConceptCouplingSpeedRatioSpecificationMethod"""
        temp = self.wrapped.SpeedRatioSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.ConceptCouplingSpeedRatioSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2209", "ConceptCouplingSpeedRatioSpecificationMethod"
        )(value)

    @speed_ratio_specification_method.setter
    @enforce_parameter_types
    def speed_ratio_specification_method(
        self: Self, value: "_2209.ConceptCouplingSpeedRatioSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.ConceptCouplingSpeedRatioSpecificationMethod",
        )
        self.wrapped.SpeedRatioSpecificationMethod = value

    @property
    def speed_ratio_vs_time(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioVsTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def speed_ratio_pid_control(self: Self) -> "_1583.PIDControlSettings":
        """mastapy.math_utility.control.PIDControlSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioPIDControl

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase":
        return self._Cast_ConceptCouplingLoadCase(self)
