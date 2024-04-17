"""RollingRingAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "RollingRingAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2805
    from mastapy.system_model.analyses_and_results.modal_analyses import _4580, _4670
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyModalAnalysis")


class RollingRingAssemblyModalAnalysis(_4690.SpecialisedAssemblyModalAnalysis):
    """RollingRingAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyModalAnalysis")

    class _Cast_RollingRingAssemblyModalAnalysis:
        """Special nested class for casting RollingRingAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
            parent: "RollingRingAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_4690.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4690.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_4580.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
        ) -> "RollingRingAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingAssemblyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6954.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2805.RollingRingAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection

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
    ) -> "RollingRingAssemblyModalAnalysis._Cast_RollingRingAssemblyModalAnalysis":
        return self._Cast_RollingRingAssemblyModalAnalysis(self)
