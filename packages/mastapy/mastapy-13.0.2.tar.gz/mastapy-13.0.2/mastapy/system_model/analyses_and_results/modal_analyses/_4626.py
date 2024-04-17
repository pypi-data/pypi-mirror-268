"""CycloidalDiscModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4581
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CycloidalDiscModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.system_deflections import _2746
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4582,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscModalAnalysis")


class CycloidalDiscModalAnalysis(_4581.AbstractShaftModalAnalysis):
    """CycloidalDiscModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscModalAnalysis")

    class _Cast_CycloidalDiscModalAnalysis:
        """Special nested class for casting CycloidalDiscModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
            parent: "CycloidalDiscModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4581.AbstractShaftModalAnalysis":
            return self._parent._cast(_4581.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4582.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "CycloidalDiscModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6868.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2746.CycloidalDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis":
        return self._Cast_CycloidalDiscModalAnalysis(self)
