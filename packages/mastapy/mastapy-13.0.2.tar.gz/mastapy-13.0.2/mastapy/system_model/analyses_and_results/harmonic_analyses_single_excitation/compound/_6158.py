"""BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6163,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6027,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6161,
        _6162,
        _6151,
        _6179,
        _6205,
        _6224,
        _6172,
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation"
)


class BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation(
    _6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
):
    """BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6205.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6027.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6027.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
        return (
            self._Cast_BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation(
                self
            )
        )
