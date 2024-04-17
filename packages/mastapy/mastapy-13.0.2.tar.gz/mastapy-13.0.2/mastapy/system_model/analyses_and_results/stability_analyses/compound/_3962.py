"""FlexiblePinAssemblyCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4003
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.stability_analyses import _3830
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3905,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundStabilityAnalysis")


class FlexiblePinAssemblyCompoundStabilityAnalysis(
    _4003.SpecialisedAssemblyCompoundStabilityAnalysis
):
    """FlexiblePinAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_FlexiblePinAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
            parent: "FlexiblePinAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "FlexiblePinAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
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
        instance_to_wrap: "FlexiblePinAssemblyCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_3830.FlexiblePinAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FlexiblePinAssemblyStabilityAnalysis]

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
    ) -> "List[_3830.FlexiblePinAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FlexiblePinAssemblyStabilityAnalysis]

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
    ) -> "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis":
        return self._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis(self)
