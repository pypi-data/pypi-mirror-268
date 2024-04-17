"""CylindricalGearCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4913,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5046,
        _5073,
        _5021,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalGearCompoundModalAnalysisAtAStiffness")


class CylindricalGearCompoundModalAnalysisAtAStiffness(
    _5054.GearCompoundModalAnalysisAtAStiffness
):
    """CylindricalGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CylindricalGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
            parent: "CylindricalGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5054.GearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5054.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5073.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(_5021.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5046.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(
                _5046.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
        ) -> "CylindricalGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CylindricalGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

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
    ) -> "List[_4913.CylindricalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalGearModalAnalysisAtAStiffness]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.CylindricalGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4913.CylindricalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalGearModalAnalysisAtAStiffness]

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
    ) -> "CylindricalGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_CylindricalGearCompoundModalAnalysisAtAStiffness(self)
