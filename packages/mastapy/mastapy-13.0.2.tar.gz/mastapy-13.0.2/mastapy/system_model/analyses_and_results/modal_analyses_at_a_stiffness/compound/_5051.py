"""FaceGearSetCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5056,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4921,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5049,
        _5050,
        _5094,
        _4996,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="FaceGearSetCompoundModalAnalysisAtAStiffness")


class FaceGearSetCompoundModalAnalysisAtAStiffness(
    _5056.GearSetCompoundModalAnalysisAtAStiffness
):
    """FaceGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_FaceGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting FaceGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
            parent: "FaceGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5056.GearSetCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5056.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "FaceGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness",
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
        self: Self,
        instance_to_wrap: "FaceGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4921.FaceGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.FaceGearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5049.FaceGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.FaceGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5050.FaceGearMeshCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.FaceGearMeshCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4921.FaceGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.FaceGearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetCompoundModalAnalysisAtAStiffness._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_FaceGearSetCompoundModalAnalysisAtAStiffness(self)
