"""StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7125,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.system_deflections import _2828
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7035,
        _7022,
        _7051,
        _7077,
        _7097,
        _7044,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"
)


class StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation(
    _7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7022.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7051.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2828.StraightBevelSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation(
            self
        )
