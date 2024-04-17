"""GearMeshCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6212,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6075,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6152,
        _6159,
        _6164,
        _6177,
        _6180,
        _6195,
        _6201,
        _6210,
        _6214,
        _6217,
        _6220,
        _6247,
        _6253,
        _6256,
        _6271,
        _6274,
        _6182,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearMeshCompoundHarmonicAnalysisOfSingleExcitation")


class GearMeshCompoundHarmonicAnalysisOfSingleExcitation(
    _6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """GearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6152.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6152,
            )

            return self._parent._cast(
                _6152.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6159.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6159,
            )

            return self._parent._cast(
                _6159.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6164.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6177.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6180.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6180,
            )

            return self._parent._cast(
                _6180.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6195.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6201.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6210.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6210,
            )

            return self._parent._cast(
                _6210.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6214.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6217.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6247.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6247,
            )

            return self._parent._cast(
                _6247.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6253.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6253,
            )

            return self._parent._cast(
                _6253.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6256.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6256,
            )

            return self._parent._cast(
                _6256.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6271.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6271,
            )

            return self._parent._cast(
                _6271.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6274.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6274,
            )

            return self._parent._cast(
                _6274.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6075.GearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6075.GearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation(self)
