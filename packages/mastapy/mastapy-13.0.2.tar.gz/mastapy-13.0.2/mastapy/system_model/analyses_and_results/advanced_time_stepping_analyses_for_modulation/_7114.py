"""RootAssemblyAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7025,
)
from mastapy.system_model.analyses_and_results import _2663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
        _7014,
        _7099,
    )
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5884,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="RootAssemblyAdvancedTimeSteppingAnalysisForModulation")


class RootAssemblyAdvancedTimeSteppingAnalysisForModulation(
    _7025.AssemblyAdvancedTimeSteppingAnalysisForModulation,
    _2663.IHaveRootHarmonicAnalysisResults,
):
    """RootAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RootAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
            parent: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7025.AssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7025.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RootAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RootAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_for_modulation_inputs(
        self: Self,
    ) -> "_7018.AdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2481.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(
        self: Self,
    ) -> "_5884.RootAssemblyHarmonicAnalysisResultsPropertyAccessor":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.RootAssemblyHarmonicAnalysisResultsPropertyAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2808.RootAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation(self)
