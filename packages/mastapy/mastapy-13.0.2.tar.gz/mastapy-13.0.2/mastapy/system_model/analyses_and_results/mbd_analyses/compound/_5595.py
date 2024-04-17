"""GearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "GearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5447
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5541,
        _5548,
        _5551,
        _5552,
        _5553,
        _5566,
        _5569,
        _5584,
        _5587,
        _5590,
        _5599,
        _5603,
        _5606,
        _5609,
        _5636,
        _5642,
        _5645,
        _5648,
        _5649,
        _5660,
        _5663,
        _5562,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearCompoundMultibodyDynamicsAnalysis")


class GearCompoundMultibodyDynamicsAnalysis(
    _5614.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """GearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_GearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting GearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
            parent: "GearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.MountableComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5614.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5541.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5548.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(
                _5548.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5551.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5552.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(
                _5552.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(
                _5566.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5569.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5587.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(
                _5587.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(_5590.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5599.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(_5599.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5603.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5606.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5609.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5636.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5642.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5645.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5649.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5660.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5660,
            )

            return self._parent._cast(_5660.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5663.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5663,
            )

            return self._parent._cast(
                _5663.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "GearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "GearCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5447.GearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5447.GearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_GearCompoundMultibodyDynamicsAnalysis(self)
