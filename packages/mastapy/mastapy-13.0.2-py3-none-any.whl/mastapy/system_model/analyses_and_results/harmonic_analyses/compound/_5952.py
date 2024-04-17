"""InterMountableComponentConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5892,
        _5896,
        _5899,
        _5904,
        _5909,
        _5914,
        _5917,
        _5920,
        _5925,
        _5927,
        _5935,
        _5941,
        _5946,
        _5950,
        _5954,
        _5957,
        _5960,
        _5968,
        _5977,
        _5980,
        _5987,
        _5990,
        _5993,
        _5996,
        _6005,
        _6011,
        _6014,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundHarmonicAnalysis"
)


class InterMountableComponentConnectionCompoundHarmonicAnalysis(
    _5922.ConnectionCompoundHarmonicAnalysis
):
    """InterMountableComponentConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
            parent: "InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5922.ConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5922.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5892.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(
                _5892.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5896.BeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5899.BevelDifferentialGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(
                _5899.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5904.BevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5909.ClutchConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5914.ConceptCouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(
                _5914.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5917.ConceptGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5920.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(_5920.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5925.CouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5927.CVTBeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(_5927.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5935.CylindricalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5941.FaceGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5946.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(_5946.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5950.HypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(_5950.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5954.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(
                _5954.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5957.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(
                _5957.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5960.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(
                _5960.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5968.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(
                _5968.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5977.RingPinsToDiscConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(
                _5977.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5980.RollingRingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(
                _5980.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5987.SpiralBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(_5987.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5990.SpringDamperConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(
                _5990.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5993.StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(
                _5993.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5996.StraightBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(
                _5996.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_6005.TorqueConverterConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6005,
            )

            return self._parent._cast(
                _6005.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_6011.WormGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6011,
            )

            return self._parent._cast(_6011.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_6014.ZerolBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6014,
            )

            return self._parent._cast(_6014.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "InterMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5782.InterMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis]

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
    ) -> "List[_5782.InterMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis(
            self
        )
