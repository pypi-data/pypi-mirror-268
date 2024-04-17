"""ConicalGearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConicalGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4614
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4742,
        _4749,
        _4754,
        _4800,
        _4804,
        _4807,
        _4810,
        _4837,
        _4843,
        _4846,
        _4864,
        _4834,
        _4736,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundModalAnalysis")


class ConicalGearSetCompoundModalAnalysis(_4796.GearSetCompoundModalAnalysis):
    """ConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetCompoundModalAnalysis")

    class _Cast_ConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting ConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
            parent: "ConicalGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4796.GearSetCompoundModalAnalysis":
            return self._parent._cast(_4796.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4742.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4749.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(
                _4749.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4754.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.BevelGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4800.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(
                _4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4837.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4843.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(
                _4843.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4846.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "_4864.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4864,
            )

            return self._parent._cast(_4864.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "ConicalGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4614.ConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4614.ConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis]

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
    ) -> (
        "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis"
    ):
        return self._Cast_ConicalGearSetCompoundModalAnalysis(self)
