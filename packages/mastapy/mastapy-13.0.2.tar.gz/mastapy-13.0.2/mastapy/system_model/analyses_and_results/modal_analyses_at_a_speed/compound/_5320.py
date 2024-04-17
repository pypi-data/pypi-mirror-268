"""InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5290,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5190,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5260,
        _5264,
        _5267,
        _5272,
        _5277,
        _5282,
        _5285,
        _5288,
        _5293,
        _5295,
        _5303,
        _5309,
        _5314,
        _5318,
        _5322,
        _5325,
        _5328,
        _5336,
        _5345,
        _5348,
        _5355,
        _5358,
        _5361,
        _5364,
        _5373,
        _5379,
        _5382,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"
)


class InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5290.ConnectionCompoundModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
            parent: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5290.ConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5290.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5260.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5260,
            )

            return self._parent._cast(
                _5260.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5264.BeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5267.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(
                _5267.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5272.BevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5277.ClutchConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5282.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(
                _5282.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5285.ConceptGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(
                _5285.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5288.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(
                _5288.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5293.CouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(
                _5293.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5295.CVTBeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5303.CylindricalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(
                _5303.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5309.FaceGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5314.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(_5314.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5318.HypoidGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(_5318.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5322.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(
                _5322.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5325.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5328.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(
                _5328.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5336.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(
                _5336.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5345.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5348.RollingRingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5355.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5358.SpringDamperConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5361.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5364.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5373.TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(
                _5373.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5379.WormGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5379,
            )

            return self._parent._cast(_5379.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5382.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5382,
            )

            return self._parent._cast(
                _5382.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5190.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5190.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        return (
            self._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
                self
            )
        )
