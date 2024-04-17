"""KlingelnbergCycloPalloidConicalGearMeshModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.system_deflections import _2776
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4654,
        _4657,
        _4643,
        _4650,
        _4615,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMeshModalAnalysis")


class KlingelnbergCycloPalloidConicalGearMeshModalAnalysis(
    _4612.ConicalGearMeshModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_4612.ConicalGearMeshModalAnalysis":
            return self._parent._cast(_4612.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_4643.GearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(_4643.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_4650.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_4615.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_4654.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(
                _4654.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "_4657.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(
                _4657.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis.TYPE",
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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis(self)
