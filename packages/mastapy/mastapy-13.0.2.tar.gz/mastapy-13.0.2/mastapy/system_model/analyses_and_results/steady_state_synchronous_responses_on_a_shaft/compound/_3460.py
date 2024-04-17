"""MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3408,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3330,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3387,
        _3391,
        _3394,
        _3397,
        _3398,
        _3399,
        _3406,
        _3411,
        _3412,
        _3415,
        _3419,
        _3422,
        _3425,
        _3430,
        _3433,
        _3436,
        _3441,
        _3445,
        _3449,
        _3452,
        _3455,
        _3458,
        _3459,
        _3461,
        _3465,
        _3468,
        _3469,
        _3470,
        _3471,
        _3472,
        _3475,
        _3479,
        _3482,
        _3487,
        _3488,
        _3491,
        _3494,
        _3495,
        _3497,
        _3498,
        _3499,
        _3502,
        _3503,
        _3504,
        _3505,
        _3506,
        _3509,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"
)


class MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft(
    _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3387.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3391.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3391,
            )

            return self._parent._cast(
                _3391.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3394,
            )

            return self._parent._cast(
                _3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3397.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3398.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3406.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3411.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3415.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3415,
            )

            return self._parent._cast(
                _3415.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3419.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3422,
            )

            return self._parent._cast(
                _3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3425.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3425,
            )

            return self._parent._cast(
                _3425.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3433.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3436.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3445.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3449.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3452.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3458.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3459.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3461.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3465.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3465,
            )

            return self._parent._cast(
                _3465.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3468.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3468,
            )

            return self._parent._cast(
                _3468.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3469.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3470.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3471.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3472.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3479.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3482.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3487.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3488.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3491.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3495.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3495,
            )

            return self._parent._cast(
                _3495.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3497.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3498.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3498,
            )

            return self._parent._cast(
                _3498.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3499.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3503.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3504.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3504,
            )

            return self._parent._cast(
                _3504.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3505.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3506.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3506,
            )

            return self._parent._cast(
                _3506.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3509.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3509,
            )

            return self._parent._cast(
                _3509.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3330.MountableComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.MountableComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3330.MountableComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.MountableComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
