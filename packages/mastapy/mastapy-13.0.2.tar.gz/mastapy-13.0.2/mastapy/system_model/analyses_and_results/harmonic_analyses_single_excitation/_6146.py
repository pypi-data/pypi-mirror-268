"""ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6034,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2561
    from mastapy.system_model.analyses_and_results.static_loads import _6996
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6144,
        _6145,
        _6022,
        _6050,
        _6076,
        _6116,
        _6016,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation")


class ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation(
    _6034.BevelGearSetHarmonicAnalysisOfSingleExcitation
):
    """ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6034.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(_6076.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2561.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6996.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6144.ZerolBevelGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ZerolBevelGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6145.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation(self)
