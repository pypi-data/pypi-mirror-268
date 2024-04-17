"""RootAssemblyCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "RootAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3867
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3905,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCompoundStabilityAnalysis")


class RootAssemblyCompoundStabilityAnalysis(_3912.AssemblyCompoundStabilityAnalysis):
    """RootAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_RootAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting RootAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
            parent: "RootAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_compound_stability_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "_3912.AssemblyCompoundStabilityAnalysis":
            return self._parent._cast(_3912.AssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
        ) -> "RootAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3867.RootAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.RootAssemblyStabilityAnalysis]

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
    ) -> "List[_3867.RootAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.RootAssemblyStabilityAnalysis]

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
    ) -> "RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis":
        return self._Cast_RootAssemblyCompoundStabilityAnalysis(self)
