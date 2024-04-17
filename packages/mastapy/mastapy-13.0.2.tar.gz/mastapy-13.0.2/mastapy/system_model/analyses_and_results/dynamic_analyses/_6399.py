"""StraightBevelSunGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelSunGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6301,
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
__all__ = ("StraightBevelSunGearDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearDynamicAnalysis")


class StraightBevelSunGearDynamicAnalysis(_6392.StraightBevelDiffGearDynamicAnalysis):
    """StraightBevelSunGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearDynamicAnalysis")

    class _Cast_StraightBevelSunGearDynamicAnalysis:
        """Special nested class for casting StraightBevelSunGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
            parent: "StraightBevelSunGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6392.StraightBevelDiffGearDynamicAnalysis":
            return self._parent._cast(_6392.StraightBevelDiffGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6301.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6289.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6317.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6345.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "StraightBevelSunGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2557.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis"
    ):
        return self._Cast_StraightBevelSunGearDynamicAnalysis(self)
