"""BevelGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5399,
        _5500,
        _5506,
        _5509,
        _5530,
        _5421,
        _5448,
        _5497,
        _5384,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetMultibodyDynamicsAnalysis")


class BevelGearSetMultibodyDynamicsAnalysis(
    _5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
):
    """BevelGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
            parent: "BevelGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5421.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5448.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(_5448.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5399.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(
                _5399.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5500.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5506.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(
                _5506.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5509.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(
                _5509.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5530.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5530

            return self._parent._cast(_5530.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "BevelGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2527.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearSetMultibodyDynamicsAnalysis(self)
