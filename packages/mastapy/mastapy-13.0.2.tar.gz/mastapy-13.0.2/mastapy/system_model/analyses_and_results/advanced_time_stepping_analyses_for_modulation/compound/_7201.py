"""ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7174,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7071,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_7071.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7071.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
