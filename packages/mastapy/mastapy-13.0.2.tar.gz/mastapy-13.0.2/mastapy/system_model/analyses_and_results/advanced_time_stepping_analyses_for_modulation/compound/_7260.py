"""StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7254,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7131,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7165,
        _7153,
        _7181,
        _7207,
        _7226,
        _7174,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7153.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7181.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7207.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7131.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7131.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
