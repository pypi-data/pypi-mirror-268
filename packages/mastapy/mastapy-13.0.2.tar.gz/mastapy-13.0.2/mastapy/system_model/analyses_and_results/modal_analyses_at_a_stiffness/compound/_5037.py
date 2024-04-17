"""CVTCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5006,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CVTCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4906,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5094,
        _4996,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTCompoundModalAnalysisAtAStiffness")


class CVTCompoundModalAnalysisAtAStiffness(
    _5006.BeltDriveCompoundModalAnalysisAtAStiffness
):
    """CVTCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundModalAnalysisAtAStiffness")

    class _Cast_CVTCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CVTCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
            parent: "CVTCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_5006.BeltDriveCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5006.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
        ) -> "CVTCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CVTCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4906.CVTModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTModalAnalysisAtAStiffness]

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
    ) -> "List[_4906.CVTModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTModalAnalysisAtAStiffness]

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
    ) -> "CVTCompoundModalAnalysisAtAStiffness._Cast_CVTCompoundModalAnalysisAtAStiffness":
        return self._Cast_CVTCompoundModalAnalysisAtAStiffness(self)
