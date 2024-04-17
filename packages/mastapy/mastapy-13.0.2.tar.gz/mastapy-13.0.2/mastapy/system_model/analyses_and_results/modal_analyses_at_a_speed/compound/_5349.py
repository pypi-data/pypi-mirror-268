"""RootAssemblyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5262,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5220,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5255,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RootAssemblyCompoundModalAnalysisAtASpeed")


class RootAssemblyCompoundModalAnalysisAtASpeed(
    _5262.AssemblyCompoundModalAnalysisAtASpeed
):
    """RootAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_RootAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting RootAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
            parent: "RootAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5262.AssemblyCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5262.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5255.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "RootAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5220.RootAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RootAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5220.RootAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RootAssemblyModalAnalysisAtASpeed]

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
    ) -> "RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_RootAssemblyCompoundModalAnalysisAtASpeed(self)
