"""StraightBevelDiffGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelDiffGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6398,
        _6399,
        _6289,
        _6317,
        _6345,
        _6364,
        _6310,
        _6366,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearDynamicAnalysis")


class StraightBevelDiffGearDynamicAnalysis(_6301.BevelGearDynamicAnalysis):
    """StraightBevelDiffGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearDynamicAnalysis")

    class _Cast_StraightBevelDiffGearDynamicAnalysis:
        """Special nested class for casting StraightBevelDiffGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
            parent: "StraightBevelDiffGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6301.BevelGearDynamicAnalysis":
            return self._parent._cast(_6301.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6289.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6317.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6345.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6398.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "_6399.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.StraightBevelSunGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "StraightBevelDiffGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6968.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

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
    ) -> "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis":
        return self._Cast_StraightBevelDiffGearDynamicAnalysis(self)
