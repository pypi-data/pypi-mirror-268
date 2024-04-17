"""SynchroniserSleeveModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4707
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SynchroniserSleeveModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.static_loads import _6979
    from mastapy.system_model.analyses_and_results.system_deflections import _2831
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4619,
        _4666,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveModalAnalysis")


class SynchroniserSleeveModalAnalysis(_4707.SynchroniserPartModalAnalysis):
    """SynchroniserSleeveModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveModalAnalysis")

    class _Cast_SynchroniserSleeveModalAnalysis:
        """Special nested class for casting SynchroniserSleeveModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
            parent: "SynchroniserSleeveModalAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_4707.SynchroniserPartModalAnalysis":
            return self._parent._cast(_4707.SynchroniserPartModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_4619.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "SynchroniserSleeveModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSleeveModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6979.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2831.SynchroniserSleeveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection

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
    ) -> "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis":
        return self._Cast_SynchroniserSleeveModalAnalysis(self)
