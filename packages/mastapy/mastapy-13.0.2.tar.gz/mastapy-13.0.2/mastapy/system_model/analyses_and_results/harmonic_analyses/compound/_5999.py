"""StraightBevelSunGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5992
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5834
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5903,
        _5891,
        _5919,
        _5945,
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundHarmonicAnalysis")


class StraightBevelSunGearCompoundHarmonicAnalysis(
    _5992.StraightBevelDiffGearCompoundHarmonicAnalysis
):
    """StraightBevelSunGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelSunGearCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelSunGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
            parent: "StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5992.StraightBevelDiffGearCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5992.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5903.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5891.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5919.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5945.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(_5945.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "StraightBevelSunGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "StraightBevelSunGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5834.StraightBevelSunGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5834.StraightBevelSunGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelSunGearCompoundHarmonicAnalysis(self)
