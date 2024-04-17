"""BevelDifferentialPlanetGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5403,
        _5389,
        _5420,
        _5447,
        _5472,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearMultibodyDynamicsAnalysis")


class BevelDifferentialPlanetGearMultibodyDynamicsAnalysis(
    _5398.BevelDifferentialGearMultibodyDynamicsAnalysis
):
    """BevelDifferentialPlanetGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5398.BevelDifferentialGearMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5398.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5403.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5420.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5447.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(_5447.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialPlanetGearMultibodyDynamicsAnalysis(self)
