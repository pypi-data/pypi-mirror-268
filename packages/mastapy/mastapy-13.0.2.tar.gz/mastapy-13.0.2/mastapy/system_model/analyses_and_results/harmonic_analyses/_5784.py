"""KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5721
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.system_deflections import _2776
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5787,
        _5790,
        _5763,
        _5782,
        _5723,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis")


class KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis(
    _5721.ConicalGearMeshHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_5721.ConicalGearMeshHarmonicAnalysis":
            return self._parent._cast(_5721.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_5763.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5763,
            )

            return self._parent._cast(_5763.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_5782.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_5787.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(
                _5787.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "_5790.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(
                _5790.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2776.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis(self)
