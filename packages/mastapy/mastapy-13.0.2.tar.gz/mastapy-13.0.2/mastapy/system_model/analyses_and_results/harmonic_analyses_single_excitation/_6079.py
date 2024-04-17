"""HypoidGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6020,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "HypoidGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6914
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6048,
        _6074,
        _6095,
        _6041,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="HypoidGearHarmonicAnalysisOfSingleExcitation")


class HypoidGearHarmonicAnalysisOfSingleExcitation(
    _6020.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
):
    """HypoidGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_HypoidGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting HypoidGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
            parent: "HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6020.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6020.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6048.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(_6074.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "HypoidGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "HypoidGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6914.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

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
    ) -> "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation(self)
