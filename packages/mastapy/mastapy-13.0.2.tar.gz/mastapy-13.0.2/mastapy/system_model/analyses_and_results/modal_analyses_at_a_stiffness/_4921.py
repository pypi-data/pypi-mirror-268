"""FaceGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4926,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "FaceGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6895
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4920,
        _4919,
        _4965,
        _4865,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="FaceGearSetModalAnalysisAtAStiffness")


class FaceGearSetModalAnalysisAtAStiffness(_4926.GearSetModalAnalysisAtAStiffness):
    """FaceGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetModalAnalysisAtAStiffness")

    class _Cast_FaceGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting FaceGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
            parent: "FaceGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_4926.GearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4926.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_4865.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
        ) -> "FaceGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "FaceGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2536.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6895.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4920.FaceGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.FaceGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4919.FaceGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.FaceGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetModalAnalysisAtAStiffness._Cast_FaceGearSetModalAnalysisAtAStiffness":
        return self._Cast_FaceGearSetModalAnalysisAtAStiffness(self)
