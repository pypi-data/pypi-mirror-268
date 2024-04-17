"""GearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2790
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.math_utility.measured_vectors import _1567
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2768,
        _2699,
        _2711,
        _2712,
        _2713,
        _2716,
        _2730,
        _2734,
        _2753,
        _2754,
        _2755,
        _2758,
        _2764,
        _2773,
        _2778,
        _2781,
        _2784,
        _2817,
        _2823,
        _2826,
        _2827,
        _2828,
        _2846,
        _2849,
        _2723,
        _2793,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4102
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSystemDeflection",)


Self = TypeVar("Self", bound="GearSystemDeflection")


class GearSystemDeflection(_2790.MountableComponentSystemDeflection):
    """GearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSystemDeflection")

    class _Cast_GearSystemDeflection:
        """Special nested class for casting GearSystemDeflection to subclasses."""

        def __init__(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
            parent: "GearSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2699.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2711.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2712.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2713.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2716.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.BevelGearSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2730.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2734.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ConicalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2753.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2754.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2755.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(
                _2755.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2758.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2764.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.FaceGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2773.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2778.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(
                _2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def spiral_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2817.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2823.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2826.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2827.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2828.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.StraightBevelSunGearSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2846.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "_2849.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2849,
            )

            return self._parent._cast(_2849.ZerolBevelGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "GearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSystemDeflection._Cast_GearSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2537.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_point_results_in_wcs(
        self: Self,
    ) -> "List[_1567.ForceAndDisplacementResults]":
        """List[mastapy.math_utility.measured_vectors.ForceAndDisplacementResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPointResultsInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set(self: Self) -> "_2768.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4102.GearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSystemDeflection._Cast_GearSystemDeflection":
        return self._Cast_GearSystemDeflection(self)
