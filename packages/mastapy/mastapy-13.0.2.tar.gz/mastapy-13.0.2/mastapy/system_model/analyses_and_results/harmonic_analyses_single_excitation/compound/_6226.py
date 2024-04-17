"""PartCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "PartCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6097,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6147,
        _6148,
        _6149,
        _6151,
        _6153,
        _6154,
        _6155,
        _6157,
        _6158,
        _6160,
        _6161,
        _6162,
        _6163,
        _6165,
        _6166,
        _6167,
        _6168,
        _6170,
        _6172,
        _6173,
        _6175,
        _6176,
        _6178,
        _6179,
        _6181,
        _6183,
        _6184,
        _6186,
        _6188,
        _6189,
        _6190,
        _6192,
        _6194,
        _6196,
        _6197,
        _6198,
        _6199,
        _6200,
        _6202,
        _6203,
        _6204,
        _6205,
        _6207,
        _6208,
        _6209,
        _6211,
        _6213,
        _6215,
        _6216,
        _6218,
        _6219,
        _6221,
        _6222,
        _6223,
        _6224,
        _6225,
        _6227,
        _6229,
        _6231,
        _6232,
        _6233,
        _6234,
        _6235,
        _6236,
        _6238,
        _6239,
        _6241,
        _6242,
        _6243,
        _6245,
        _6246,
        _6248,
        _6249,
        _6251,
        _6252,
        _6254,
        _6255,
        _6257,
        _6258,
        _6259,
        _6260,
        _6261,
        _6262,
        _6263,
        _6264,
        _6266,
        _6267,
        _6268,
        _6269,
        _6270,
        _6272,
        _6273,
        _6275,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PartCompoundHarmonicAnalysisOfSingleExcitation")


class PartCompoundHarmonicAnalysisOfSingleExcitation(_7554.PartCompoundAnalysis):
    """PartCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PartCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "PartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6147,
            )

            return self._parent._cast(
                _6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6153.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6154,
            )

            return self._parent._cast(
                _6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6155.BearingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BearingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6157.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6157,
            )

            return self._parent._cast(
                _6157.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6160.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6165.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6166.BoltCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.BoltCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6167.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6167,
            )

            return self._parent._cast(
                _6167.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6168.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6168,
            )

            return self._parent._cast(
                _6168.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6173.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6178.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6181.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6181,
            )

            return self._parent._cast(
                _6181.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6184.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6188.CVTCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6188,
            )

            return self._parent._cast(
                _6188.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6189,
            )

            return self._parent._cast(
                _6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6190.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6196.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6198.DatumCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.DatumCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6202.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6202,
            )

            return self._parent._cast(
                _6202.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6204.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6205.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6207.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6207,
            )

            return self._parent._cast(
                _6207.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6208,
            )

            return self._parent._cast(
                _6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6211.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6211,
            )

            return self._parent._cast(
                _6211.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6215.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6221.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6221,
            )

            return self._parent._cast(
                _6221.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6227.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6231.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6231,
            )

            return self._parent._cast(
                _6231.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6235,
            )

            return self._parent._cast(
                _6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6238.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6238,
            )

            return self._parent._cast(
                _6238.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6241.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6241,
            )

            return self._parent._cast(
                _6241.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6245.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6248.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6249.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6254.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6257.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6259,
            )

            return self._parent._cast(
                _6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6260.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6264.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6264,
            )

            return self._parent._cast(
                _6264.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6268,
            )

            return self._parent._cast(
                _6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6269,
            )

            return self._parent._cast(
                _6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6270,
            )

            return self._parent._cast(
                _6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6272.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6272,
            )

            return self._parent._cast(
                _6272.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6273,
            )

            return self._parent._cast(
                _6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6275.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6275,
            )

            return self._parent._cast(
                _6275.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "PartCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PartCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6097.PartHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PartHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6097.PartHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PartHarmonicAnalysisOfSingleExcitation]

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
    ) -> "PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation(self)
