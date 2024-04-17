"""ClutchHalfModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ClutchHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6842
    from mastapy.system_model.analyses_and_results.system_deflections import _2720
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4666,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfModalAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfModalAnalysis")


class ClutchHalfModalAnalysis(_4619.CouplingHalfModalAnalysis):
    """ClutchHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfModalAnalysis")

    class _Cast_ClutchHalfModalAnalysis:
        """Special nested class for casting ClutchHalfModalAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
            parent: "ClutchHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4619.CouplingHalfModalAnalysis":
            return self._parent._cast(_4619.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "ClutchHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6842.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2720.ClutchHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis":
        return self._Cast_ClutchHalfModalAnalysis(self)
