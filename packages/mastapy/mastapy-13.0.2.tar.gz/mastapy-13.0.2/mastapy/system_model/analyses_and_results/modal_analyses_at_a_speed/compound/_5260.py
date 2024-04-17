"""AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5288,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5129,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5267,
        _5272,
        _5318,
        _5355,
        _5361,
        _5364,
        _5382,
        _5314,
        _5320,
        _5290,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed")


class AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed(
    _5288.ConicalGearMeshCompoundModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5288.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5288.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5314.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(_5314.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5290.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5267.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(
                _5267.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5272.BevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5318.HypoidGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(_5318.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5355.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5361.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5364.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5382.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5382,
            )

            return self._parent._cast(
                _5382.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5129.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5129.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed(self)
