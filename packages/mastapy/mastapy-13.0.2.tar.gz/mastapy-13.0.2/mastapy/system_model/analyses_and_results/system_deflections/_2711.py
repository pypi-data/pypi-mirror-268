"""BevelDifferentialGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2716
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelDifferentialGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.gears.rating.bevel import _558
    from mastapy.system_model.analyses_and_results.static_loads import _6831
    from mastapy.system_model.analyses_and_results.power_flows import _4052
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2712,
        _2713,
        _2699,
        _2734,
        _2769,
        _2790,
        _2723,
        _2793,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearSystemDeflection")


class BevelDifferentialGearSystemDeflection(_2716.BevelGearSystemDeflection):
    """BevelDifferentialGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSystemDeflection"
    )

    class _Cast_BevelDifferentialGearSystemDeflection:
        """Special nested class for casting BevelDifferentialGearSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
            parent: "BevelDifferentialGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2716.BevelGearSystemDeflection":
            return self._parent._cast(_2716.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2699.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2734.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2769.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2712.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "_2713.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
        ) -> "BevelDifferentialGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSystemDeflection.TYPE"
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
    def component_detailed_analysis(self: Self) -> "_558.BevelGearRating":
        """mastapy.gears.rating.bevel.BevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

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
    def power_flow_results(self: Self) -> "_4052.BevelDifferentialGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSystemDeflection._Cast_BevelDifferentialGearSystemDeflection":
        return self._Cast_BevelDifferentialGearSystemDeflection(self)
