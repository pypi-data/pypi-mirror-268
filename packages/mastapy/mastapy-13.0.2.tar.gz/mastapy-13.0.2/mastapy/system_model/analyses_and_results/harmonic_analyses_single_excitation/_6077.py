"""GuideDxfModelHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GuideDxfModelHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GuideDxfModelHarmonicAnalysisOfSingleExcitation")


class GuideDxfModelHarmonicAnalysisOfSingleExcitation(
    _6041.ComponentHarmonicAnalysisOfSingleExcitation
):
    """GuideDxfModelHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GuideDxfModelHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
            parent: "GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "GuideDxfModelHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "GuideDxfModelHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6905.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

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
    ) -> "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation(self)
