"""CycloidalDiscCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3906
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CycloidalDiscCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.stability_analyses import _3818
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3907,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundStabilityAnalysis")


class CycloidalDiscCompoundStabilityAnalysis(
    _3906.AbstractShaftCompoundStabilityAnalysis
):
    """CycloidalDiscCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundStabilityAnalysis"
    )

    class _Cast_CycloidalDiscCompoundStabilityAnalysis:
        """Special nested class for casting CycloidalDiscCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
            parent: "CycloidalDiscCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_3906.AbstractShaftCompoundStabilityAnalysis":
            return self._parent._cast(_3906.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_3907.AbstractShaftOrHousingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def component_compound_stability_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
        ) -> "CycloidalDiscCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_3818.CycloidalDiscStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CycloidalDiscStabilityAnalysis]

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
    ) -> "List[_3818.CycloidalDiscStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CycloidalDiscStabilityAnalysis]

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
    ) -> "CycloidalDiscCompoundStabilityAnalysis._Cast_CycloidalDiscCompoundStabilityAnalysis":
        return self._Cast_CycloidalDiscCompoundStabilityAnalysis(self)
