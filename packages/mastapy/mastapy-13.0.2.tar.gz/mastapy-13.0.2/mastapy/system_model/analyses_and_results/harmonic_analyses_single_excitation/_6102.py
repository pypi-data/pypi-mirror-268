"""PlanetaryGearSetHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6065,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6076,
        _6116,
        _6016,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PlanetaryGearSetHarmonicAnalysisOfSingleExcitation")


class PlanetaryGearSetHarmonicAnalysisOfSingleExcitation(
    _6065.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6065.CylindricalGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6065.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(_6076.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2549.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation(self)
