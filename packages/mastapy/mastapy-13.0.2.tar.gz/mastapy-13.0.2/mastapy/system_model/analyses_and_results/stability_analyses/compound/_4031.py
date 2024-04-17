"""ZerolBevelGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ZerolBevelGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.stability_analyses import _3904
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3909,
        _3937,
        _3963,
        _3982,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundStabilityAnalysis")


class ZerolBevelGearCompoundStabilityAnalysis(_3921.BevelGearCompoundStabilityAnalysis):
    """ZerolBevelGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundStabilityAnalysis"
    )

    class _Cast_ZerolBevelGearCompoundStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
            parent: "ZerolBevelGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3921.BevelGearCompoundStabilityAnalysis":
            return self._parent._cast(_3921.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3909.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3937.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3963.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
        ) -> "ZerolBevelGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2560.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

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
    ) -> "List[_3904.ZerolBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearStabilityAnalysis]

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
    ) -> "List[_3904.ZerolBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearStabilityAnalysis]

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
    ) -> "ZerolBevelGearCompoundStabilityAnalysis._Cast_ZerolBevelGearCompoundStabilityAnalysis":
        return self._Cast_ZerolBevelGearCompoundStabilityAnalysis(self)
