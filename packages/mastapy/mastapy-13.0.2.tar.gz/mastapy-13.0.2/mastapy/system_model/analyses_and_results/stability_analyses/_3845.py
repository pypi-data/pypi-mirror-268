"""KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3803,
        _3831,
        _3838,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis(
    _3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            return self._parent._cast(
                _3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def conical_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3803.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3831.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(_3831.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis(
            self
        )
