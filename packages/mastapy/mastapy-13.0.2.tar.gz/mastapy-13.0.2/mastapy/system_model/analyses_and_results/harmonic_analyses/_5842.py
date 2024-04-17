"""TorqueConverterTurbineHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "TorqueConverterTurbineHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.system_deflections import _2839
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineHarmonicAnalysis")


class TorqueConverterTurbineHarmonicAnalysis(_5726.CouplingHalfHarmonicAnalysis):
    """TorqueConverterTurbineHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineHarmonicAnalysis"
    )

    class _Cast_TorqueConverterTurbineHarmonicAnalysis:
        """Special nested class for casting TorqueConverterTurbineHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
            parent: "TorqueConverterTurbineHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_5726.CouplingHalfHarmonicAnalysis":
            return self._parent._cast(_5726.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "TorqueConverterTurbineHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2618.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6984.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "_2839.TorqueConverterTurbineSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection

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
    ) -> "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis":
        return self._Cast_TorqueConverterTurbineHarmonicAnalysis(self)
