"""SynchroniserPartCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3944
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SynchroniserPartCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3890
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4019,
        _4021,
        _3982,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundStabilityAnalysis")


class SynchroniserPartCompoundStabilityAnalysis(
    _3944.CouplingHalfCompoundStabilityAnalysis
):
    """SynchroniserPartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundStabilityAnalysis"
    )

    class _Cast_SynchroniserPartCompoundStabilityAnalysis:
        """Special nested class for casting SynchroniserPartCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
            parent: "SynchroniserPartCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3944.CouplingHalfCompoundStabilityAnalysis":
            return self._parent._cast(_3944.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_4019.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_4021.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "SynchroniserPartCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3890.SynchroniserPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserPartStabilityAnalysis]

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
    ) -> "List[_3890.SynchroniserPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserPartStabilityAnalysis]

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
    ) -> "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis":
        return self._Cast_SynchroniserPartCompoundStabilityAnalysis(self)
