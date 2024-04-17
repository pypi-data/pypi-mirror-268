"""HypoidGearMeshCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5001,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4928,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5029,
        _5055,
        _5061,
        _5031,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundModalAnalysisAtAStiffness")


class HypoidGearMeshCompoundModalAnalysisAtAStiffness(
    _5001.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
):
    """HypoidGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting HypoidGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
            parent: "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5001.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5001.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(_5055.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(_5031.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "HypoidGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "HypoidGearMeshCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

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
    ) -> "List[_4928.HypoidGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearMeshModalAnalysisAtAStiffness]

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
    ) -> "List[_4928.HypoidGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearMeshModalAnalysisAtAStiffness]

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
    ) -> "HypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_HypoidGearMeshCompoundModalAnalysisAtAStiffness(self)
