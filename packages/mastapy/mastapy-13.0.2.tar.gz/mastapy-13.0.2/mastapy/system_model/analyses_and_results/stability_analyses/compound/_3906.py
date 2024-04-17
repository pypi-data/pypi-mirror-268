"""AbstractShaftCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractShaftCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3773
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3950,
        _4000,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundStabilityAnalysis")


class AbstractShaftCompoundStabilityAnalysis(
    _3907.AbstractShaftOrHousingCompoundStabilityAnalysis
):
    """AbstractShaftCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundStabilityAnalysis"
    )

    class _Cast_AbstractShaftCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
            parent: "AbstractShaftCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3907.AbstractShaftOrHousingCompoundStabilityAnalysis":
            return self._parent._cast(
                _3907.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def component_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3950.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_4000.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(_4000.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "AbstractShaftCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3773.AbstractShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftStabilityAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3773.AbstractShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis":
        return self._Cast_AbstractShaftCompoundStabilityAnalysis(self)
