"""KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5322,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5197,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5288,
        _5314,
        _5320,
        _5290,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed(
    _5322.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5322.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ):
            return self._parent._cast(
                _5322.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5288.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(
                _5288.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5314.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(_5314.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5290.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5197.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5197.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed(
            self
        )
