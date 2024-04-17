"""ComponentSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2992,
        _2993,
        _2997,
        _2999,
        _3004,
        _3005,
        _3006,
        _3009,
        _3011,
        _3013,
        _3018,
        _3022,
        _3025,
        _3027,
        _3029,
        _3032,
        _3037,
        _3040,
        _3041,
        _3042,
        _3044,
        _3047,
        _3048,
        _3052,
        _3053,
        _3056,
        _3060,
        _3063,
        _3066,
        _3067,
        _3068,
        _3069,
        _3070,
        _3073,
        _3077,
        _3078,
        _3079,
        _3080,
        _3081,
        _3085,
        _3087,
        _3088,
        _3093,
        _3095,
        _3102,
        _3105,
        _3106,
        _3107,
        _3108,
        _3109,
        _3110,
        _3113,
        _3115,
        _3116,
        _3117,
        _3120,
        _3123,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ComponentSteadyStateSynchronousResponse")


class ComponentSteadyStateSynchronousResponse(_3071.PartSteadyStateSynchronousResponse):
    """ComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentSteadyStateSynchronousResponse"
    )

    class _Cast_ComponentSteadyStateSynchronousResponse:
        """Special nested class for casting ComponentSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
            parent: "ComponentSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2992.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2993.AbstractShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(_2993.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2997.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(
                _2997.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def bearing_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2999.BearingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BearingSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3004.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3005.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3006.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3009.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(_3009.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3011.BoltSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(_3011.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3013.ClutchHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(_3013.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3018.ConceptCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3022.ConceptGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3025.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3027.ConnectorSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3027,
            )

            return self._parent._cast(_3027.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3029.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3032.CVTPulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3032,
            )

            return self._parent._cast(_3032.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3037.CycloidalDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3040.CylindricalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(
                _3040.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3041.CylindricalPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(
                _3041.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def datum_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3042.DatumSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3044.ExternalCADModelSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(
                _3044.ExternalCADModelSteadyStateSynchronousResponse
            )

        @property
        def face_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3047.FaceGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(_3047.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3048.FEPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(_3048.FEPartSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3052.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(_3052.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3053.GuideDxfModelSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(_3053.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3056.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(_3056.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3060.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(
                _3060.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3063.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3066.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3067.MassDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3068.MeasurementComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(
                _3068.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3070.OilSealSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.OilSealSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3073.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(
                _3073.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3077.PlanetCarrierSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3077,
            )

            return self._parent._cast(_3077.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3078.PointLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(_3078.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3079.PowerLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(_3079.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3080.PulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(_3080.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3081.RingPinsSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(_3081.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3085.RollingRingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(_3085.RollingRingSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3087.ShaftHubConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(
                _3087.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3088.ShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(_3088.ShaftSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3093.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3095.SpringDamperHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3102.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3105.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3106.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3107.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3108.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(
                _3108.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3109.SynchroniserPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(
                _3109.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3110.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(
                _3110.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3113.TorqueConverterPumpSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3113,
            )

            return self._parent._cast(
                _3113.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3115.TorqueConverterTurbineSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3116.UnbalancedMassSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3116,
            )

            return self._parent._cast(
                _3116.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3117.VirtualComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3117,
            )

            return self._parent._cast(
                _3117.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3120.WormGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3120,
            )

            return self._parent._cast(_3120.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3123.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "ComponentSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ComponentSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse":
        return self._Cast_ComponentSteadyStateSynchronousResponse(self)
