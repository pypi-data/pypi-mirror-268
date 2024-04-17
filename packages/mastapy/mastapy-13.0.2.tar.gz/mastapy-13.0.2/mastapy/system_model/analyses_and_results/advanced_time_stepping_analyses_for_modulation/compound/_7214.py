"""InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7184,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7085,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7154,
        _7158,
        _7161,
        _7166,
        _7171,
        _7176,
        _7179,
        _7182,
        _7187,
        _7189,
        _7197,
        _7203,
        _7208,
        _7212,
        _7216,
        _7219,
        _7222,
        _7230,
        _7239,
        _7242,
        _7249,
        _7252,
        _7255,
        _7258,
        _7267,
        _7273,
        _7276,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7154.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7154,
            )

            return self._parent._cast(
                _7154.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7158.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7171.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7176.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7176,
            )

            return self._parent._cast(
                _7176.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7179.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7187.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7187,
            )

            return self._parent._cast(
                _7187.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7189.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7197.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7203.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7212.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7216.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7219.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7230.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7230,
            )

            return self._parent._cast(
                _7230.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7239.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7242.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7249.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7249,
            )

            return self._parent._cast(
                _7249.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7252.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7255.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7258.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7267.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7267,
            )

            return self._parent._cast(
                _7267.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7273.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7273,
            )

            return self._parent._cast(
                _7273.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7276.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7276,
            )

            return self._parent._cast(
                _7276.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
