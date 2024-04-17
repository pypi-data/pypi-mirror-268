"""ComponentCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5075,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ComponentCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4890,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4997,
        _4998,
        _5000,
        _5004,
        _5007,
        _5010,
        _5011,
        _5012,
        _5015,
        _5019,
        _5024,
        _5025,
        _5028,
        _5032,
        _5035,
        _5038,
        _5041,
        _5043,
        _5046,
        _5047,
        _5048,
        _5049,
        _5052,
        _5054,
        _5057,
        _5058,
        _5062,
        _5065,
        _5068,
        _5071,
        _5072,
        _5073,
        _5074,
        _5078,
        _5081,
        _5082,
        _5083,
        _5084,
        _5085,
        _5088,
        _5091,
        _5092,
        _5095,
        _5100,
        _5101,
        _5104,
        _5107,
        _5108,
        _5110,
        _5111,
        _5112,
        _5115,
        _5116,
        _5117,
        _5118,
        _5119,
        _5122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ComponentCompoundModalAnalysisAtAStiffness")


class ComponentCompoundModalAnalysisAtAStiffness(
    _5075.PartCompoundModalAnalysisAtAStiffness
):
    """ComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ComponentCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ComponentCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
            parent: "ComponentCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_4997.AbstractShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_4998.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(
                _4998.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5000.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5004.BearingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(_5004.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5007.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(
                _5007.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5010.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5011.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(
                _5011.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5012.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.BoltCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(_5015.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5019.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(_5019.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(
                _5025.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5028.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5028,
            )

            return self._parent._cast(
                _5028.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5032.ConnectorCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5035.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5038.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(_5038.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5041.CycloidalDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5046.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(
                _5046.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def datum_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.DatumCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5048.ExternalCADModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(
                _5048.ExternalCADModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5049.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5049,
            )

            return self._parent._cast(_5049.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5052.FEPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(_5052.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5054.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(_5054.GearCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5057.GuideDxfModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.GuideDxfModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5058.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(_5058.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5062.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5065.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5068.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(
                _5068.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(_5071.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5072.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5073.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5074.OilSealCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(_5074.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5078.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5081.PlanetCarrierCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5082.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(_5082.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5083.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(_5083.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5084.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(_5084.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5085.RingPinsCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(_5085.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5091.ShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(_5091.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5092.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5095.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5100.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5101.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5104.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5107.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5108.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5110.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5111.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5115.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5116.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5117.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5117,
            )

            return self._parent._cast(
                _5117.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5118.VirtualComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5118,
            )

            return self._parent._cast(
                _5118.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5119.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5119,
            )

            return self._parent._cast(_5119.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5122.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5122,
            )

            return self._parent._cast(
                _5122.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
        ) -> "ComponentCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ComponentCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4890.ComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ComponentModalAnalysisAtAStiffness]

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
    ) -> "List[_4890.ComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ComponentModalAnalysisAtAStiffness]

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
    ) -> "ComponentCompoundModalAnalysisAtAStiffness._Cast_ComponentCompoundModalAnalysisAtAStiffness":
        return self._Cast_ComponentCompoundModalAnalysisAtAStiffness(self)
