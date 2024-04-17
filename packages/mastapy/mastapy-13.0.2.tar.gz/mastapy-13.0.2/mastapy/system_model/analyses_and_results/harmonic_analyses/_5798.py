"""PartToPartShearCouplingHalfHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.system_deflections import _2795
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfHarmonicAnalysis")


class PartToPartShearCouplingHalfHarmonicAnalysis(_5726.CouplingHalfHarmonicAnalysis):
    """PartToPartShearCouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfHarmonicAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfHarmonicAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
            parent: "PartToPartShearCouplingHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_5726.CouplingHalfHarmonicAnalysis":
            return self._parent._cast(_5726.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
        ) -> "PartToPartShearCouplingHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "_2795.PartToPartShearCouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection

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
    ) -> "PartToPartShearCouplingHalfHarmonicAnalysis._Cast_PartToPartShearCouplingHalfHarmonicAnalysis":
        return self._Cast_PartToPartShearCouplingHalfHarmonicAnalysis(self)
