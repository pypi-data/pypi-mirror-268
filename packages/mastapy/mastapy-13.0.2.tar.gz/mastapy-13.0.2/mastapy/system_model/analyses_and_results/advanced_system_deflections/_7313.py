"""ConicalGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7341
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConicalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7285,
        _7292,
        _7295,
        _7296,
        _7297,
        _7345,
        _7349,
        _7352,
        _7355,
        _7383,
        _7389,
        _7392,
        _7395,
        _7396,
        _7411,
        _7361,
        _7306,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearAdvancedSystemDeflection")


class ConicalGearAdvancedSystemDeflection(_7341.GearAdvancedSystemDeflection):
    """ConicalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearAdvancedSystemDeflection")

    class _Cast_ConicalGearAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
            parent: "ConicalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7341.GearAdvancedSystemDeflection":
            return self._parent._cast(_7341.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7285.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7292.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(
                _7292.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7295.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(
                _7295.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7296.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(
                _7296.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7297.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.BevelGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7345.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(_7345.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7349.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7383.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7389.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(
                _7389.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7392.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7395.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(
                _7395.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7396.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "_7411.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(_7411.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "ConicalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection"
    ):
        return self._Cast_ConicalGearAdvancedSystemDeflection(self)
