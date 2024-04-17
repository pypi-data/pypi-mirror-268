"""ConicalGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6476
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConicalGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6422,
        _6429,
        _6434,
        _6480,
        _6484,
        _6487,
        _6490,
        _6517,
        _6523,
        _6526,
        _6544,
        _6514,
        _6416,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundDynamicAnalysis")


class ConicalGearSetCompoundDynamicAnalysis(_6476.GearSetCompoundDynamicAnalysis):
    """ConicalGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundDynamicAnalysis"
    )

    class _Cast_ConicalGearSetCompoundDynamicAnalysis:
        """Special nested class for casting ConicalGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
            parent: "ConicalGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6476.GearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6476.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6514.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6416.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6422.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(
                _6422.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6429.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(
                _6429.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6434.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.BevelGearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6480.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6484.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6487.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6490.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6517.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6523.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(
                _6523.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6526.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6544.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6544,
            )

            return self._parent._cast(_6544.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "ConicalGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6319.ConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis]

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
    ) -> "List[_6319.ConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis]

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
    ) -> "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis":
        return self._Cast_ConicalGearSetCompoundDynamicAnalysis(self)
