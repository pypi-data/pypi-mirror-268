"""PartToPartShearCouplingHalfCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfCriticalSpeedAnalysis")


class PartToPartShearCouplingHalfCriticalSpeedAnalysis(
    _6590.CouplingHalfCriticalSpeedAnalysis
):
    """PartToPartShearCouplingHalfCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
            parent: "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_6590.CouplingHalfCriticalSpeedAnalysis":
            return self._parent._cast(_6590.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
        ) -> "PartToPartShearCouplingHalfCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCriticalSpeedAnalysis.TYPE",
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
    def component_load_case(self: Self) -> "_6939.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingHalfCriticalSpeedAnalysis._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis":
        return self._Cast_PartToPartShearCouplingHalfCriticalSpeedAnalysis(self)
