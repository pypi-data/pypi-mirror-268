"""ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7188,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7042,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7226,
        _7174,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7042.ClutchHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ClutchHalfAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7042.ClutchHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ClutchHalfAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
