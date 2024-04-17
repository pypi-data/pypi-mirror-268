"""GearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "GearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4645
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4742,
        _4749,
        _4754,
        _4767,
        _4770,
        _4785,
        _4791,
        _4800,
        _4804,
        _4807,
        _4810,
        _4820,
        _4837,
        _4843,
        _4846,
        _4861,
        _4864,
        _4736,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="GearSetCompoundModalAnalysis")


class GearSetCompoundModalAnalysis(_4834.SpecialisedAssemblyCompoundModalAnalysis):
    """GearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundModalAnalysis")

    class _Cast_GearSetCompoundModalAnalysis:
        """Special nested class for casting GearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
            parent: "GearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4742.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4749.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(
                _4749.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4754.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.BevelGearSetCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4767.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4770.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.ConicalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4785.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4791.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.FaceGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4800.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(
                _4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4820.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4837.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4843.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(
                _4843.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4846.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4861.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "_4864.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4864,
            )

            return self._parent._cast(_4864.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
        ) -> "GearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4645.GearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis]

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
    def assembly_analysis_cases_ready(self: Self) -> "List[_4645.GearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundModalAnalysis._Cast_GearSetCompoundModalAnalysis":
        return self._Cast_GearSetCompoundModalAnalysis(self)
