"""AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6717,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6696,
        _6701,
        _6747,
        _6784,
        _6790,
        _6793,
        _6811,
        _6743,
        _6781,
        _6683,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis")


class AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis(
    _6717.ConicalGearSetCompoundCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6717.ConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6717.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6743.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(_6743.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6781.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6683.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(
                _6683.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6696.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6701.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(_6701.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6747.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(_6747.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6784.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6790.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6793.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6811.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6811,
            )

            return self._parent._cast(
                _6811.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]

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
    ) -> "List[_6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis(self)
