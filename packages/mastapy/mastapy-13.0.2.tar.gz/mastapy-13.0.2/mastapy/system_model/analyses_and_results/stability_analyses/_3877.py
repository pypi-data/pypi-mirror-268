"""SpringDamperStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3810
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpringDamperStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3871,
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperStabilityAnalysis",)


Self = TypeVar("Self", bound="SpringDamperStabilityAnalysis")


class SpringDamperStabilityAnalysis(_3810.CouplingStabilityAnalysis):
    """SpringDamperStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperStabilityAnalysis")

    class _Cast_SpringDamperStabilityAnalysis:
        """Special nested class for casting SpringDamperStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
            parent: "SpringDamperStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3810.CouplingStabilityAnalysis":
            return self._parent._cast(_3810.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "SpringDamperStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6967.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis":
        return self._Cast_SpringDamperStabilityAnalysis(self)
