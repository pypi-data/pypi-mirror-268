"""InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5542,
        _5546,
        _5549,
        _5554,
        _5559,
        _5564,
        _5567,
        _5570,
        _5575,
        _5577,
        _5585,
        _5591,
        _5596,
        _5600,
        _5604,
        _5607,
        _5610,
        _5618,
        _5627,
        _5630,
        _5637,
        _5640,
        _5643,
        _5646,
        _5655,
        _5661,
        _5664,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
)


class InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5572.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5572.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5542.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5546.BeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5549.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(
                _5549.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(
                _5554.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.ClutchConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5564.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(
                _5564.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.ConceptGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.CouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5577.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5585.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(
                _5585.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5591.FaceGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(
                _5591.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(_5596.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5600.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5604.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(
                _5604.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5607.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5618.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(
                _5618.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.RollingRingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5637.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5640.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5646.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5655.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5655,
            )

            return self._parent._cast(
                _5655.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5661.WormGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5661,
            )

            return self._parent._cast(
                _5661.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5664.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5664,
            )

            return self._parent._cast(
                _5664.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
