"""RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7156,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7114,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7149,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7114.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7114.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
