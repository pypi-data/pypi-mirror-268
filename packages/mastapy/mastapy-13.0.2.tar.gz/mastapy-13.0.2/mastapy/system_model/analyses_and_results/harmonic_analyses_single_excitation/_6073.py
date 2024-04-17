"""FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6116,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.static_loads import _6897
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6016,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation")


class FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation(
    _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation",
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
        self: Self,
        instance_to_wrap: "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6897.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation(self)
