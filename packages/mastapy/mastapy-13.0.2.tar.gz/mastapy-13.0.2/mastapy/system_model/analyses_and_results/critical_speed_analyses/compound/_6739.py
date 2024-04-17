"""FEPartCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6685,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "FEPartCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FEPartCompoundCriticalSpeedAnalysis")


class FEPartCompoundCriticalSpeedAnalysis(
    _6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
):
    """FEPartCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundCriticalSpeedAnalysis")

    class _Cast_FEPartCompoundCriticalSpeedAnalysis:
        """Special nested class for casting FEPartCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
            parent: "FEPartCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "FEPartCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FEPartCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_6610.FEPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FEPartCriticalSpeedAnalysis]

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
    def planetaries(self: Self) -> "List[FEPartCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.FEPartCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6610.FEPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FEPartCriticalSpeedAnalysis]

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
    ) -> (
        "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis"
    ):
        return self._Cast_FEPartCompoundCriticalSpeedAnalysis(self)
