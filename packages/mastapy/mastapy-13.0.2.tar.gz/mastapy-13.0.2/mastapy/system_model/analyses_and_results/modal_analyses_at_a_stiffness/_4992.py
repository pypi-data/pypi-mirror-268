"""WormGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4926,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "WormGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.static_loads import _6993
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4991,
        _4990,
        _4965,
        _4865,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="WormGearSetModalAnalysisAtAStiffness")


class WormGearSetModalAnalysisAtAStiffness(_4926.GearSetModalAnalysisAtAStiffness):
    """WormGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetModalAnalysisAtAStiffness")

    class _Cast_WormGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting WormGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
            parent: "WormGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_4926.GearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4926.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_4865.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
        ) -> "WormGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "WormGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6993.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4991.WormGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.WormGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4990.WormGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.WormGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetModalAnalysisAtAStiffness._Cast_WormGearSetModalAnalysisAtAStiffness":
        return self._Cast_WormGearSetModalAnalysisAtAStiffness(self)
