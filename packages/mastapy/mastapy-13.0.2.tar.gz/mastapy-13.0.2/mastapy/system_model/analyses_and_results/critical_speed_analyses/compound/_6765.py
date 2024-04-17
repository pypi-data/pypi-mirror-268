"""PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6722,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6636
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6760,
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis")


class PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis(
    _6722.CouplingHalfCompoundCriticalSpeedAnalysis
):
    """PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
            parent: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6722.CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6722.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_6636.PartToPartShearCouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PartToPartShearCouplingHalfCriticalSpeedAnalysis]

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
    ) -> "List[_6636.PartToPartShearCouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PartToPartShearCouplingHalfCriticalSpeedAnalysis]

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
    ) -> "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
        return self._Cast_PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis(self)
