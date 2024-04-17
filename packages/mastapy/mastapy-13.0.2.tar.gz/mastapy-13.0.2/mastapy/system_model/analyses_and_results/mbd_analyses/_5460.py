"""KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5421
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5463,
        _5466,
        _5448,
        _5497,
        _5384,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis(
    _5421.ConicalGearSetMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5421.ConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5421.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5448.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(_5448.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5463.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(
                _5463.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> (
            "_5466.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis(
                self
            )
        )
