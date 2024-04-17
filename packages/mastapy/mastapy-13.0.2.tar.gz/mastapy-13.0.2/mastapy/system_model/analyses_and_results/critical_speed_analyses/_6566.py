"""BevelDifferentialSunGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6567,
        _6555,
        _6583,
        _6612,
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCriticalSpeedAnalysis")


class BevelDifferentialSunGearCriticalSpeedAnalysis(
    _6562.BevelDifferentialGearCriticalSpeedAnalysis
):
    """BevelDifferentialSunGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
            parent: "BevelDifferentialSunGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6562.BevelDifferentialGearCriticalSpeedAnalysis":
            return self._parent._cast(_6562.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6567.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6555.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6583.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6612.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(_6612.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
        ) -> "BevelDifferentialSunGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialSunGearCriticalSpeedAnalysis(self)
