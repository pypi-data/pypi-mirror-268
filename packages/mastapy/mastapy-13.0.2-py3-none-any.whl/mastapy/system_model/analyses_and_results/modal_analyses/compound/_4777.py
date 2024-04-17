"""CVTCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4746
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CVTCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4622
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4834,
        _4736,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundModalAnalysis")


class CVTCompoundModalAnalysis(_4746.BeltDriveCompoundModalAnalysis):
    """CVTCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundModalAnalysis")

    class _Cast_CVTCompoundModalAnalysis:
        """Special nested class for casting CVTCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
            parent: "CVTCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4746.BeltDriveCompoundModalAnalysis":
            return self._parent._cast(_4746.BeltDriveCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "CVTCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4622.CVTModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_4622.CVTModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis]

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
    ) -> "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis":
        return self._Cast_CVTCompoundModalAnalysis(self)
