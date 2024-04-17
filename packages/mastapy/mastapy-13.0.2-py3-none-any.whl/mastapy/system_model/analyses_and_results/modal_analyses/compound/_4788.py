"""ExternalCADModelCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4761
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ExternalCADModelCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.modal_analyses import _4636
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4815
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundModalAnalysis")


class ExternalCADModelCompoundModalAnalysis(_4761.ComponentCompoundModalAnalysis):
    """ExternalCADModelCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCompoundModalAnalysis"
    )

    class _Cast_ExternalCADModelCompoundModalAnalysis:
        """Special nested class for casting ExternalCADModelCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
            parent: "ExternalCADModelCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
        ) -> "ExternalCADModelCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_4636.ExternalCADModelModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis]

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
    ) -> "List[_4636.ExternalCADModelModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis]

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
    ) -> "ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis":
        return self._Cast_ExternalCADModelCompoundModalAnalysis(self)
