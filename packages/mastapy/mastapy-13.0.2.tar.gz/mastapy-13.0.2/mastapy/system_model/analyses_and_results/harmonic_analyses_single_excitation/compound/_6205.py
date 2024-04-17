"""GearCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6224,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "GearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6074,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6151,
        _6158,
        _6161,
        _6162,
        _6163,
        _6176,
        _6179,
        _6194,
        _6197,
        _6200,
        _6209,
        _6213,
        _6216,
        _6219,
        _6246,
        _6252,
        _6255,
        _6258,
        _6259,
        _6270,
        _6273,
        _6172,
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearCompoundHarmonicAnalysisOfSingleExcitation")


class GearCompoundHarmonicAnalysisOfSingleExcitation(
    _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """GearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6259,
            )

            return self._parent._cast(
                _6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6270,
            )

            return self._parent._cast(
                _6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6273,
            )

            return self._parent._cast(
                _6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "GearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "GearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6074.GearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6074.GearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation(self)
