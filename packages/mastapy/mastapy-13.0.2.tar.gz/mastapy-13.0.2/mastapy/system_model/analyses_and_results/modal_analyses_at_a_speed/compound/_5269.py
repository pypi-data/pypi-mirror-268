"""BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5266,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5139,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5271,
        _5259,
        _5287,
        _5313,
        _5332,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed")


class BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed(
    _5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed
):
    """BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
            parent: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5271.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5287.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(_5287.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5313.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(_5313.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5139.BevelDifferentialPlanetGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelDifferentialPlanetGearModalAnalysisAtASpeed]

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
    ) -> "List[_5139.BevelDifferentialPlanetGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelDifferentialPlanetGearModalAnalysisAtASpeed]

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
    ) -> "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed(self)
