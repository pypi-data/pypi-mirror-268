"""RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7247,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7112,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7149,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _ROLLING_RING_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2605.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7112.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7112.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
