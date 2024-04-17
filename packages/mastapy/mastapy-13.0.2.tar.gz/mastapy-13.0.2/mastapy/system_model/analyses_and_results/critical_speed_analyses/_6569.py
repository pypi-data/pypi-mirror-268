"""BevelGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6564,
        _6655,
        _6661,
        _6664,
        _6682,
        _6585,
        _6614,
        _6652,
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCriticalSpeedAnalysis")


class BevelGearSetCriticalSpeedAnalysis(
    _6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
):
    """BevelGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCriticalSpeedAnalysis")

    class _Cast_BevelGearSetCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
            parent: "BevelGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(
                _6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6585.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6614.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6564.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(
                _6564.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6655.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6661.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(
                _6661.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6664.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "_6682.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
        ) -> "BevelGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCriticalSpeedAnalysis.TYPE"
    ):
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
    ) -> "BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis":
        return self._Cast_BevelGearSetCriticalSpeedAnalysis(self)
