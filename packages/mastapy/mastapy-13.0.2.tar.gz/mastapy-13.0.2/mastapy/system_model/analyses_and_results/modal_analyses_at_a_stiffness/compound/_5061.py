"""InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5031,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4931,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5001,
        _5005,
        _5008,
        _5013,
        _5018,
        _5023,
        _5026,
        _5029,
        _5034,
        _5036,
        _5044,
        _5050,
        _5055,
        _5059,
        _5063,
        _5066,
        _5069,
        _5077,
        _5086,
        _5089,
        _5096,
        _5099,
        _5102,
        _5105,
        _5114,
        _5120,
        _5123,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
)


class InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
    _5031.ConnectionCompoundModalAnalysisAtAStiffness
):
    """InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
            parent: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.ConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5031.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5001.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5005.BeltConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5008.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5008,
            )

            return self._parent._cast(
                _5008.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.BevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(
                _5013.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5018.ClutchConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.ConceptGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(
                _5026.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(
                _5034.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.CVTBeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.CylindricalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(
                _5044.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5050.FaceGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(
                _5050.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(_5055.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5059.HypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5063.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(
                _5063.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(
                _5069.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5077.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(
                _5077.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5089.RollingRingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.RollingRingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5096.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5099.SpringDamperConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5102.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5105.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5114.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5114,
            )

            return self._parent._cast(
                _5114.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5120.WormGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5120,
            )

            return self._parent._cast(
                _5120.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5123.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5123,
            )

            return self._parent._cast(
                _5123.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4931.InterMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.InterMountableComponentConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4931.InterMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.InterMountableComponentConnectionModalAnalysisAtAStiffness]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
