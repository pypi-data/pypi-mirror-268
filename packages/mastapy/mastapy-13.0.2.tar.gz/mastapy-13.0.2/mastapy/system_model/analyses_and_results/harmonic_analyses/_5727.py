"""CouplingHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.system_deflections import _2739
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5710,
        _5716,
        _5799,
        _5825,
        _5840,
        _5686,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHarmonicAnalysis")


class CouplingHarmonicAnalysis(_5818.SpecialisedAssemblyHarmonicAnalysis):
    """CouplingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHarmonicAnalysis")

    class _Cast_CouplingHarmonicAnalysis:
        """Special nested class for casting CouplingHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
            parent: "CouplingHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5710.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5716.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.ConceptCouplingHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5799.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5825.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.SpringDamperHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5840.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.TorqueConverterHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "CouplingHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2739.CouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection

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
    ) -> "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis":
        return self._Cast_CouplingHarmonicAnalysis(self)
