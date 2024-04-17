"""BevelGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5398,
        _5400,
        _5401,
        _5499,
        _5505,
        _5508,
        _5510,
        _5511,
        _5529,
        _5420,
        _5447,
        _5472,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearMultibodyDynamicsAnalysis")


class BevelGearMultibodyDynamicsAnalysis(
    _5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
):
    """BevelGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMultibodyDynamicsAnalysis")

    class _Cast_BevelGearMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
            parent: "BevelGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5420.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5447.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(_5447.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5398.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(
                _5398.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5400.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(
                _5400.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5401.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5499.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(_5499.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5505.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5508.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(_5508.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5510.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5511.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "_5529.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "BevelGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMultibodyDynamicsAnalysis.TYPE"
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
    ) -> "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearMultibodyDynamicsAnalysis(self)
