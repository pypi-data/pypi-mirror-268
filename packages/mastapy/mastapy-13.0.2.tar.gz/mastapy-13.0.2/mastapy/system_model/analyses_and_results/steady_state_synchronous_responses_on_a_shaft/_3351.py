"""SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3253,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3258,
        _3263,
        _3265,
        _3270,
        _3272,
        _3276,
        _3281,
        _3283,
        _3286,
        _3292,
        _3295,
        _3296,
        _3301,
        _3307,
        _3310,
        _3312,
        _3316,
        _3320,
        _3323,
        _3326,
        _3335,
        _3337,
        _3344,
        _3353,
        _3357,
        _3360,
        _3363,
        _3370,
        _3373,
        _3378,
        _3381,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"
)


class SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
    _3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
):
    """SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3258.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3263.BeltDriveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(
                _3263.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3265.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.BoltedJointSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3276.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3281.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3283.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3292.CouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3295.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(_3295.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3296.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3316.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3320.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3323.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3335.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3337.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3337,
            )

            return self._parent._cast(
                _3337.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3344.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3353.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3357.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3360.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3360,
            )

            return self._parent._cast(
                _3360.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3363.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3370.SynchroniserSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3373.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3378.WormGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3378,
            )

            return self._parent._cast(
                _3378.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3381.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3381,
            )

            return self._parent._cast(
                _3381.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2483.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
            self
        )
