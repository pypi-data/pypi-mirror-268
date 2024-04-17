"""FaceGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5315,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5180,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5308,
        _5309,
        _5353,
        _5255,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="FaceGearSetCompoundModalAnalysisAtASpeed")


class FaceGearSetCompoundModalAnalysisAtASpeed(
    _5315.GearSetCompoundModalAnalysisAtASpeed
):
    """FaceGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_FaceGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting FaceGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
            parent: "FaceGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5315.GearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5315.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5255.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
        ) -> "FaceGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "FaceGearSetCompoundModalAnalysisAtASpeed.TYPE"
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
    ) -> "List[_5180.FaceGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FaceGearSetModalAnalysisAtASpeed]

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
    def face_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5308.FaceGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.FaceGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5309.FaceGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.FaceGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5180.FaceGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FaceGearSetModalAnalysisAtASpeed]

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
    ) -> "FaceGearSetCompoundModalAnalysisAtASpeed._Cast_FaceGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_FaceGearSetCompoundModalAnalysisAtASpeed(self)
