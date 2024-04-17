"""PlanetaryGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5304,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5210,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5315,
        _5353,
        _5255,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundModalAnalysisAtASpeed")


class PlanetaryGearSetCompoundModalAnalysisAtASpeed(
    _5304.CylindricalGearSetCompoundModalAnalysisAtASpeed
):
    """PlanetaryGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PlanetaryGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
            parent: "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5304.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5304.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5315.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(_5315.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5255.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "PlanetaryGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5210.PlanetaryGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PlanetaryGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5210.PlanetaryGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PlanetaryGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed(self)
