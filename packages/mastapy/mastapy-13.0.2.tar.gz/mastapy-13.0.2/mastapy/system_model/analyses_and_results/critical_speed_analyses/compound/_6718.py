"""ConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6686,
        _6688,
        _6692,
        _6695,
        _6700,
        _6705,
        _6707,
        _6710,
        _6713,
        _6716,
        _6721,
        _6723,
        _6727,
        _6729,
        _6731,
        _6737,
        _6742,
        _6746,
        _6748,
        _6750,
        _6753,
        _6756,
        _6764,
        _6766,
        _6773,
        _6776,
        _6780,
        _6783,
        _6786,
        _6789,
        _6792,
        _6801,
        _6807,
        _6810,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundCriticalSpeedAnalysis")


class ConnectionCompoundCriticalSpeedAnalysis(_7547.ConnectionCompoundAnalysis):
    """ConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
            parent: "ConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6686.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6688.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6692.BeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(_6692.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6695.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6695,
            )

            return self._parent._cast(
                _6695.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6700.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6705.ClutchConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6707.CoaxialConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(
                _6710.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6713.ConceptGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(
                _6713.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6716.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(
                _6716.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6721.CouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(
                _6721.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6723.CVTBeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6723,
            )

            return self._parent._cast(
                _6723.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6727.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6729.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(
                _6729.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6731.CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(
                _6731.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6737.FaceGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6742.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(_6742.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6746.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(_6746.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6750.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(
                _6750.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6753.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(
                _6753.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6756.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(
                _6756.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6764.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(
                _6764.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6766.PlanetaryConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.PlanetaryConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6773.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6776.RollingRingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6780.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6783.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6786.SpringDamperConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6789.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6792.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6792,
            )

            return self._parent._cast(
                _6792.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6801.TorqueConverterConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(
                _6801.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6807.WormGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6807,
            )

            return self._parent._cast(_6807.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6810.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6810,
            )

            return self._parent._cast(
                _6810.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
        ) -> "ConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6586.ConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6586.ConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConnectionCriticalSpeedAnalysis]

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
    ) -> "ConnectionCompoundCriticalSpeedAnalysis._Cast_ConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_ConnectionCompoundCriticalSpeedAnalysis(self)
