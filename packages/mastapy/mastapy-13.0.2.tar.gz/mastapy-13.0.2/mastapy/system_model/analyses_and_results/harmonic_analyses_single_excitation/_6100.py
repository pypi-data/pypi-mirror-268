"""PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6055,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6116,
        _6016,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation"
)


class PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation(
    _6055.CouplingHarmonicAnalysisOfSingleExcitation
):
    """PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
            parent: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6055.CouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6055.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6940.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

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
    ) -> "PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation(
            self
        )
