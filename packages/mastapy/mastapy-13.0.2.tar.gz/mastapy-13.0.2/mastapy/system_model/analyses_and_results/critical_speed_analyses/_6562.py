"""BevelDifferentialGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelDifferentialGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.static_loads import _6831
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6565,
        _6566,
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
__all__ = ("BevelDifferentialGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCriticalSpeedAnalysis")


class BevelDifferentialGearCriticalSpeedAnalysis(_6567.BevelGearCriticalSpeedAnalysis):
    """BevelDifferentialGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
            parent: "BevelDifferentialGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6567.BevelGearCriticalSpeedAnalysis":
            return self._parent._cast(_6567.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6555.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6583.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6612.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(_6612.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6565.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(
                _6565.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6566.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(
                _6566.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "BevelDifferentialGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6831.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

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
    ) -> "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialGearCriticalSpeedAnalysis(self)
