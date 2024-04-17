"""BevelDifferentialGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3789
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelDifferentialGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.static_loads import _6831
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3785,
        _3786,
        _3777,
        _3805,
        _3833,
        _3850,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearStabilityAnalysis")


class BevelDifferentialGearStabilityAnalysis(_3789.BevelGearStabilityAnalysis):
    """BevelDifferentialGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearStabilityAnalysis"
    )

    class _Cast_BevelDifferentialGearStabilityAnalysis:
        """Special nested class for casting BevelDifferentialGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
            parent: "BevelDifferentialGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3789.BevelGearStabilityAnalysis":
            return self._parent._cast(_3789.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3777.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3805.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3833.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(_3833.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3850.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3785.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(
                _3785.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "_3786.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
        ) -> "BevelDifferentialGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearStabilityAnalysis.TYPE"
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
    ) -> "BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis":
        return self._Cast_BevelDifferentialGearStabilityAnalysis(self)
