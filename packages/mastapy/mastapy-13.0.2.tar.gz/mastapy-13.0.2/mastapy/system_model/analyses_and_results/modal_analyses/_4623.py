"""CVTPulleyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4679
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CVTPulleyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.system_deflections import _2741
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4619,
        _4666,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyModalAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyModalAnalysis")


class CVTPulleyModalAnalysis(_4679.PulleyModalAnalysis):
    """CVTPulleyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyModalAnalysis")

    class _Cast_CVTPulleyModalAnalysis:
        """Special nested class for casting CVTPulleyModalAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
            parent: "CVTPulleyModalAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4679.PulleyModalAnalysis":
            return self._parent._cast(_4679.PulleyModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4619.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "CVTPulleyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2595.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2741.CVTPulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis":
        return self._Cast_CVTPulleyModalAnalysis(self)
