"""PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7188,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7102,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7226,
        _7174,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_7102.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7102.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
