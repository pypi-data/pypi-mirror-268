"""InterMountableComponentConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "InterMountableComponentConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4650
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4741,
        _4745,
        _4748,
        _4753,
        _4758,
        _4763,
        _4766,
        _4769,
        _4774,
        _4776,
        _4784,
        _4790,
        _4795,
        _4799,
        _4803,
        _4806,
        _4809,
        _4817,
        _4826,
        _4829,
        _4836,
        _4839,
        _4842,
        _4845,
        _4854,
        _4860,
        _4863,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundModalAnalysis")


class InterMountableComponentConnectionCompoundModalAnalysis(
    _4771.ConnectionCompoundModalAnalysis
):
    """InterMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
            parent: "InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4741.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4745.BeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(_4745.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4748.BevelDifferentialGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(
                _4748.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4753.BevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4758.ClutchConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ClutchConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4763.ConceptCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(
                _4763.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4766.ConceptGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4769.ConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.ConicalGearMeshCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4774.CouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4776.CVTBeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4784.CylindricalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4790.FaceGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(_4790.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4795.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(_4795.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4799.HypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(_4799.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4803.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(
                _4803.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4806.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(
                _4806.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4809.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(
                _4809.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4817.PartToPartShearCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(
                _4817.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4826.RingPinsToDiscConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(
                _4826.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4829.RollingRingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.RollingRingConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4836.SpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4839.SpringDamperConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4842.StraightBevelDiffGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(
                _4842.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4845.StraightBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4854.TorqueConverterConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(
                _4854.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4860.WormGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4860,
            )

            return self._parent._cast(_4860.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4863.ZerolBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4863,
            )

            return self._parent._cast(_4863.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4650.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

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
    ) -> "List[_4650.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundModalAnalysis(self)
