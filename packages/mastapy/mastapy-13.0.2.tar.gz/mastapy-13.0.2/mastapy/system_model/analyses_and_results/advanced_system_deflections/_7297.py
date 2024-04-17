"""BevelGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7285
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7292,
        _7295,
        _7296,
        _7383,
        _7389,
        _7392,
        _7395,
        _7396,
        _7411,
        _7313,
        _7341,
        _7361,
        _7306,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearAdvancedSystemDeflection")


class BevelGearAdvancedSystemDeflection(
    _7285.AGMAGleasonConicalGearAdvancedSystemDeflection
):
    """BevelGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearAdvancedSystemDeflection")

    class _Cast_BevelGearAdvancedSystemDeflection:
        """Special nested class for casting BevelGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
            parent: "BevelGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7285.AGMAGleasonConicalGearAdvancedSystemDeflection":
            return self._parent._cast(
                _7285.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def conical_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7313.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7341.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(_7341.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7292.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(
                _7292.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7295.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(
                _7295.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7296.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(
                _7296.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7383.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7389.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(
                _7389.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7392.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7395.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(
                _7395.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7396.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "_7411.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(_7411.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_advanced_system_deflection(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
        ) -> "BevelGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

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
    ) -> "BevelGearAdvancedSystemDeflection._Cast_BevelGearAdvancedSystemDeflection":
        return self._Cast_BevelGearAdvancedSystemDeflection(self)
