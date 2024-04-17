"""BevelGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6427,
        _6430,
        _6431,
        _6515,
        _6521,
        _6524,
        _6527,
        _6528,
        _6542,
        _6448,
        _6474,
        _6493,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundDynamicAnalysis")


class BevelGearCompoundDynamicAnalysis(
    _6420.AGMAGleasonConicalGearCompoundDynamicAnalysis
):
    """BevelGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundDynamicAnalysis")

    class _Cast_BevelGearCompoundDynamicAnalysis:
        """Special nested class for casting BevelGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
            parent: "BevelGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6420.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            return self._parent._cast(
                _6420.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6448.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(_6448.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6474.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6427.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(
                _6427.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6430.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(
                _6430.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6431.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(
                _6431.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6515.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(_6515.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6521.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(
                _6521.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6524.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6527.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(
                _6527.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6528.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "_6542.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6542,
            )

            return self._parent._cast(_6542.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
        ) -> "BevelGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6301.BevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6301.BevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearCompoundDynamicAnalysis._Cast_BevelGearCompoundDynamicAnalysis":
        return self._Cast_BevelGearCompoundDynamicAnalysis(self)
