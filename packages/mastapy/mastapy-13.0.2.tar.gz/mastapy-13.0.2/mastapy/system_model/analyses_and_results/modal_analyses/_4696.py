"""SpringDamperModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpringDamperModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.system_deflections import _2820
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4690,
        _4580,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperModalAnalysis",)


Self = TypeVar("Self", bound="SpringDamperModalAnalysis")


class SpringDamperModalAnalysis(_4620.CouplingModalAnalysis):
    """SpringDamperModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperModalAnalysis")

    class _Cast_SpringDamperModalAnalysis:
        """Special nested class for casting SpringDamperModalAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
            parent: "SpringDamperModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_4620.CouplingModalAnalysis":
            return self._parent._cast(_4620.CouplingModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_4690.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_4580.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis",
        ) -> "SpringDamperModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6967.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2820.SpringDamperSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection

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
    ) -> "SpringDamperModalAnalysis._Cast_SpringDamperModalAnalysis":
        return self._Cast_SpringDamperModalAnalysis(self)
