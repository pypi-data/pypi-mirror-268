"""AbstractShaftModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.system_deflections import _2695
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4626,
        _4687,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysis")


class AbstractShaftModalAnalysis(_4582.AbstractShaftOrHousingModalAnalysis):
    """AbstractShaftModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftModalAnalysis")

    class _Cast_AbstractShaftModalAnalysis:
        """Special nested class for casting AbstractShaftModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            parent: "AbstractShaftModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4582.AbstractShaftOrHousingModalAnalysis":
            return self._parent._cast(_4582.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4626.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.CycloidalDiscModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4687.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.ShaftModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "AbstractShaftModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2442.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2695.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

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
    ) -> "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis":
        return self._Cast_AbstractShaftModalAnalysis(self)
