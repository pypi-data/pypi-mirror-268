"""BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5014,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4878,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5007,
        _5008,
        _5002,
        _5030,
        _5056,
        _5094,
        _4996,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"
)


class BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness(
    _5014.BevelGearSetCompoundModalAnalysisAtAStiffness
):
    """BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
            parent: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5014.BevelGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5014.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5002.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5030.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(
                _5030.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5056.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(_5056.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2523.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

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
    ) -> "List[_4878.BevelDifferentialGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelDifferentialGearSetModalAnalysisAtAStiffness]

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
    def bevel_differential_gears_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5007.BevelDifferentialGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.BevelDifferentialGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5008.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4878.BevelDifferentialGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelDifferentialGearSetModalAnalysisAtAStiffness]

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
    ) -> "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness(
            self
        )
