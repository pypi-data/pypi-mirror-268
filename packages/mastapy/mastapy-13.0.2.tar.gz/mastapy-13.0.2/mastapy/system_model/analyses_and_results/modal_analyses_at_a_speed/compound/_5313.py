"""GearCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5332,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "GearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5184,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5259,
        _5266,
        _5269,
        _5270,
        _5271,
        _5284,
        _5287,
        _5302,
        _5305,
        _5308,
        _5317,
        _5321,
        _5324,
        _5327,
        _5354,
        _5360,
        _5363,
        _5366,
        _5367,
        _5378,
        _5381,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearCompoundModalAnalysisAtASpeed")


class GearCompoundModalAnalysisAtASpeed(
    _5332.MountableComponentCompoundModalAnalysisAtASpeed
):
    """GearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundModalAnalysisAtASpeed")

    class _Cast_GearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting GearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
            parent: "GearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(
                _5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5269.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5270.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5271.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5284.ConceptGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5287.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(_5287.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5302.CylindricalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(
                _5302.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5305.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(
                _5305.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5308.FaceGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(_5308.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5317.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(_5317.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5321.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5324.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5327.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5354.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5360.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5363.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5366.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5367.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5378.WormGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(_5378.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "_5381.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5381,
            )

            return self._parent._cast(_5381.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
        ) -> "GearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "GearCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5184.GearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GearModalAnalysisAtASpeed]

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
    ) -> "List[_5184.GearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GearModalAnalysisAtASpeed]

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
    ) -> "GearCompoundModalAnalysisAtASpeed._Cast_GearCompoundModalAnalysisAtASpeed":
        return self._Cast_GearCompoundModalAnalysisAtASpeed(self)
