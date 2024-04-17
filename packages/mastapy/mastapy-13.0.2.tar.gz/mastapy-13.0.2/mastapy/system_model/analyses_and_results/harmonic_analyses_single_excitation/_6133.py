"""SynchroniserPartHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SynchroniserPartHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2613
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6131,
        _6134,
        _6095,
        _6041,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SynchroniserPartHarmonicAnalysisOfSingleExcitation")


class SynchroniserPartHarmonicAnalysisOfSingleExcitation(
    _6054.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """SynchroniserPartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserPartHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
            parent: "SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6054.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SynchroniserPartHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2613.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation(self)
