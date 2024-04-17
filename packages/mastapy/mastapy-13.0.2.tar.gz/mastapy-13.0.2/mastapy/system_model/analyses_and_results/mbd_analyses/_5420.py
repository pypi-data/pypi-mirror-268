"""ConicalGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConicalGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5389,
        _5398,
        _5400,
        _5401,
        _5403,
        _5451,
        _5459,
        _5462,
        _5465,
        _5499,
        _5505,
        _5508,
        _5510,
        _5511,
        _5529,
        _5472,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMultibodyDynamicsAnalysis")


class ConicalGearMultibodyDynamicsAnalysis(_5447.GearMultibodyDynamicsAnalysis):
    """ConicalGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMultibodyDynamicsAnalysis")

    class _Cast_ConicalGearMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
            parent: "ConicalGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5447.GearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5447.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5398.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(
                _5398.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5400.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(
                _5400.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5401.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5403.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.BevelGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5451.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(_5451.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5459.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(
                _5459.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5462.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462

            return self._parent._cast(
                _5462.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5465.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5499.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(_5499.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5505.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5508.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(_5508.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5510.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5511.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5529.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
        ) -> "ConicalGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMultibodyDynamicsAnalysis.TYPE"
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
    def planetaries(self: Self) -> "List[ConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMultibodyDynamicsAnalysis]

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
    ) -> "ConicalGearMultibodyDynamicsAnalysis._Cast_ConicalGearMultibodyDynamicsAnalysis":
        return self._Cast_ConicalGearMultibodyDynamicsAnalysis(self)
