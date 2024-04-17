"""PartSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3617,
        _3512,
        _3513,
        _3514,
        _3517,
        _3518,
        _3519,
        _3520,
        _3522,
        _3524,
        _3525,
        _3526,
        _3527,
        _3529,
        _3530,
        _3531,
        _3532,
        _3534,
        _3535,
        _3537,
        _3539,
        _3540,
        _3542,
        _3543,
        _3545,
        _3546,
        _3548,
        _3550,
        _3551,
        _3553,
        _3554,
        _3555,
        _3558,
        _3560,
        _3561,
        _3562,
        _3563,
        _3564,
        _3566,
        _3567,
        _3568,
        _3569,
        _3571,
        _3572,
        _3573,
        _3575,
        _3576,
        _3579,
        _3580,
        _3582,
        _3583,
        _3585,
        _3586,
        _3587,
        _3588,
        _3589,
        _3590,
        _3593,
        _3594,
        _3596,
        _3597,
        _3598,
        _3599,
        _3600,
        _3601,
        _3603,
        _3605,
        _3606,
        _3607,
        _3608,
        _3610,
        _3612,
        _3613,
        _3615,
        _3616,
        _3619,
        _3620,
        _3622,
        _3623,
        _3624,
        _3625,
        _3626,
        _3627,
        _3628,
        _3629,
        _3631,
        _3632,
        _3633,
        _3634,
        _3635,
        _3637,
        _3638,
        _3640,
        _3641,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PartSteadyStateSynchronousResponseAtASpeed")


class PartSteadyStateSynchronousResponseAtASpeed(_7556.PartStaticLoadAnalysisCase):
    """PartSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_PartSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
            parent: "PartSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3513.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3514.AbstractShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3518.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3519.AssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3520.BearingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3522.BeltDriveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(
                _3522.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3525.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3526.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3527.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3530.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.BoltedJointSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3532.BoltSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(_3532.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3534.ClutchHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3535.ClutchSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3542.ConceptGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.ConceptGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3546.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3548.ConnectorSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3548,
            )

            return self._parent._cast(
                _3548.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3551.CouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3553.CVTPulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3554.CVTSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(_3554.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3555.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3558.CycloidalDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3560.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3561.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3563.DatumSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(_3563.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3564.ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.FaceGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3567.FaceGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3568.FEPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3569.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3572.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(_3572.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3573.GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3576.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3579.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3580.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3582.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3586.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3587.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3588.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3590.OilSealSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3593.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3594.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3596.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3597.PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(
                _3597.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3598.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3599.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3600.PulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3601.RingPinsSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3603.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3605.RollingRingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.RootAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(
                _3606.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3607.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3608.ShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(_3608.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3613.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3615.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3616.SpringDamperSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3623.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3624.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3625.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3626.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3627.SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3628.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3629.SynchroniserSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3631.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3631,
            )

            return self._parent._cast(
                _3631.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3632.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(
                _3632.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3633.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3634.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3634,
            )

            return self._parent._cast(
                _3634.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3635.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3635,
            )

            return self._parent._cast(
                _3635.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3637.WormGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3637,
            )

            return self._parent._cast(
                _3637.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3638.WormGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3638,
            )

            return self._parent._cast(
                _3638.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3641.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3641,
            )

            return self._parent._cast(
                _3641.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "PartSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
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
        self: Self, instance_to_wrap: "PartSteadyStateSynchronousResponseAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "_3617.SteadyStateSynchronousResponseAtASpeed":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SteadyStateSynchronousResponseAtASpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartSteadyStateSynchronousResponseAtASpeed(self)
