"""ComponentCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6226,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ComponentCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6041,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6148,
        _6149,
        _6151,
        _6155,
        _6158,
        _6161,
        _6162,
        _6163,
        _6166,
        _6170,
        _6175,
        _6176,
        _6179,
        _6183,
        _6186,
        _6189,
        _6192,
        _6194,
        _6197,
        _6198,
        _6199,
        _6200,
        _6203,
        _6205,
        _6208,
        _6209,
        _6213,
        _6216,
        _6219,
        _6222,
        _6223,
        _6224,
        _6225,
        _6229,
        _6232,
        _6233,
        _6234,
        _6235,
        _6236,
        _6239,
        _6242,
        _6243,
        _6246,
        _6251,
        _6252,
        _6255,
        _6258,
        _6259,
        _6261,
        _6262,
        _6263,
        _6266,
        _6267,
        _6268,
        _6269,
        _6270,
        _6273,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ComponentCompoundHarmonicAnalysisOfSingleExcitation")


class ComponentCompoundHarmonicAnalysisOfSingleExcitation(
    _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
):
    """ComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6155.BearingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BearingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6166.BoltCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.BoltCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6189,
            )

            return self._parent._cast(
                _6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6198.DatumCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.DatumCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6205.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6208,
            )

            return self._parent._cast(
                _6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6235,
            )

            return self._parent._cast(
                _6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6259,
            )

            return self._parent._cast(
                _6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6268,
            )

            return self._parent._cast(
                _6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6269,
            )

            return self._parent._cast(
                _6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6270,
            )

            return self._parent._cast(
                _6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6273,
            )

            return self._parent._cast(
                _6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6041.ComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6041.ComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation(self)
