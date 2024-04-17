"""CycloidalAssemblyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5353,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2575
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5168,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5255,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CycloidalAssemblyCompoundModalAnalysisAtASpeed")


class CycloidalAssemblyCompoundModalAnalysisAtASpeed(
    _5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
):
    """CycloidalAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
            parent: "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5255.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CycloidalAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2575.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2575.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5168.CycloidalAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5168.CycloidalAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalAssemblyModalAnalysisAtASpeed]

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
    ) -> "CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed(self)
