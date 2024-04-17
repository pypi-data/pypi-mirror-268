"""FlexiblePinAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "FlexiblePinAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.utility import _1596
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.static_loads import _6815, _6937
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyLoadCase",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyLoadCase")


class FlexiblePinAssemblyLoadCase(_6961.SpecialisedAssemblyLoadCase):
    """FlexiblePinAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyLoadCase")

    class _Cast_FlexiblePinAssemblyLoadCase:
        """Special nested class for casting FlexiblePinAssemblyLoadCase to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
            parent: "FlexiblePinAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_load_case(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
        ) -> "FlexiblePinAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_inner_race_distortion_for_flexible_pin_spindle(
        self: Self,
    ) -> "_1596.LoadCaseOverrideOption":
        """mastapy.utility.LoadCaseOverrideOption"""
        temp = self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility._1596", "LoadCaseOverrideOption"
        )(value)

    @include_inner_race_distortion_for_flexible_pin_spindle.setter
    @enforce_parameter_types
    def include_inner_race_distortion_for_flexible_pin_spindle(
        self: Self, value: "_1596.LoadCaseOverrideOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )
        self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle = value

    @property
    def assembly_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyLoadCase._Cast_FlexiblePinAssemblyLoadCase":
        return self._Cast_FlexiblePinAssemblyLoadCase(self)
