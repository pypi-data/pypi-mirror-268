"""KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4932,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.analyses_and_results.static_loads import _6925
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4897,
        _4924,
        _4931,
        _4900,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness"
)


class KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness(
    _4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4897.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4924.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(_4924.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4931.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(
                _4931.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4900.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(_4900.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "_6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness(
                self
            )
        )
