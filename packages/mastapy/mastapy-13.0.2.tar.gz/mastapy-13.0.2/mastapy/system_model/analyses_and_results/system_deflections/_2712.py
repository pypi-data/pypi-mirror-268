"""BevelDifferentialPlanetGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelDifferentialPlanetGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.power_flows import _4054
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2716,
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
__all__ = ("BevelDifferentialPlanetGearSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearSystemDeflection")


class BevelDifferentialPlanetGearSystemDeflection(
    _2711.BevelDifferentialGearSystemDeflection
):
    """BevelDifferentialPlanetGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearSystemDeflection"
    )

    class _Cast_BevelDifferentialPlanetGearSystemDeflection:
        """Special nested class for casting BevelDifferentialPlanetGearSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
            parent: "BevelDifferentialPlanetGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2711.BevelDifferentialGearSystemDeflection":
            return self._parent._cast(_2711.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2716.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2699.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2734.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2769.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "BevelDifferentialPlanetGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelDifferentialPlanetGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2524.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4054.BevelDifferentialPlanetGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow

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
    ) -> "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection":
        return self._Cast_BevelDifferentialPlanetGearSystemDeflection(self)
