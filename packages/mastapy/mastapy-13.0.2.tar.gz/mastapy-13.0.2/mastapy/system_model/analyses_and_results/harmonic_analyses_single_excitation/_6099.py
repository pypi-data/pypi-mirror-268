"""PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6095,
        _6041,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation"
)


class PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6054.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6054.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation(
            self
        )
