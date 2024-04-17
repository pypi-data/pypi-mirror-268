"""ZerolBevelGearSetModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2561
    from mastapy.system_model.analyses_and_results.static_loads import _6996
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5253,
        _5252,
        _5131,
        _5159,
        _5185,
        _5224,
        _5125,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ZerolBevelGearSetModalAnalysisAtASpeed")


class ZerolBevelGearSetModalAnalysisAtASpeed(_5143.BevelGearSetModalAnalysisAtASpeed):
    """ZerolBevelGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetModalAnalysisAtASpeed"
    )

    class _Cast_ZerolBevelGearSetModalAnalysisAtASpeed:
        """Special nested class for casting ZerolBevelGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
            parent: "ZerolBevelGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5143.BevelGearSetModalAnalysisAtASpeed":
            return self._parent._cast(_5143.BevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5131.AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(
                _5131.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5159.ConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5185.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(_5185.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5224.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5125.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
        ) -> "ZerolBevelGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2561.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6996.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5253.ZerolBevelGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ZerolBevelGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5252.ZerolBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ZerolBevelGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetModalAnalysisAtASpeed._Cast_ZerolBevelGearSetModalAnalysisAtASpeed":
        return self._Cast_ZerolBevelGearSetModalAnalysisAtASpeed(self)
