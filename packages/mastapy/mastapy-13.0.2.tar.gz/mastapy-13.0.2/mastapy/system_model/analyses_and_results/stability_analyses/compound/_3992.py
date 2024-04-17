"""PowerLoadCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4027
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PowerLoadCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.stability_analyses import _3860
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3982,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PowerLoadCompoundStabilityAnalysis")


class PowerLoadCompoundStabilityAnalysis(
    _4027.VirtualComponentCompoundStabilityAnalysis
):
    """PowerLoadCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCompoundStabilityAnalysis")

    class _Cast_PowerLoadCompoundStabilityAnalysis:
        """Special nested class for casting PowerLoadCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
            parent: "PowerLoadCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_stability_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_4027.VirtualComponentCompoundStabilityAnalysis":
            return self._parent._cast(_4027.VirtualComponentCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
        ) -> "PowerLoadCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_3860.PowerLoadStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PowerLoadStabilityAnalysis]

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
    ) -> "List[_3860.PowerLoadStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PowerLoadStabilityAnalysis]

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
    ) -> "PowerLoadCompoundStabilityAnalysis._Cast_PowerLoadCompoundStabilityAnalysis":
        return self._Cast_PowerLoadCompoundStabilityAnalysis(self)
