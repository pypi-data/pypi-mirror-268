"""BevelGearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6298,
        _6388,
        _6394,
        _6397,
        _6415,
        _6319,
        _6347,
        _6385,
        _6285,
        _6366,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetDynamicAnalysis")


class BevelGearSetDynamicAnalysis(_6291.AGMAGleasonConicalGearSetDynamicAnalysis):
    """BevelGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetDynamicAnalysis")

    class _Cast_BevelGearSetDynamicAnalysis:
        """Special nested class for casting BevelGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
            parent: "BevelGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6291.AGMAGleasonConicalGearSetDynamicAnalysis":
            return self._parent._cast(_6291.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6319.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6347.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(_6347.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6285.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6298.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6388.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6394.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6397.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.StraightBevelGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "_6415.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.ZerolBevelGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
        ) -> "BevelGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2527.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetDynamicAnalysis._Cast_BevelGearSetDynamicAnalysis":
        return self._Cast_BevelGearSetDynamicAnalysis(self)
