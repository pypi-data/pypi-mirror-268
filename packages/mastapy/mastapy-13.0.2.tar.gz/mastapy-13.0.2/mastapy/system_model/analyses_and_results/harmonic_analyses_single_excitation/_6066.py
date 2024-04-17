"""CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6063,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6074,
        _6095,
        _6041,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation")


class CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation(
    _6063.CylindricalGearHarmonicAnalysisOfSingleExcitation
):
    """CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
            parent: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6063.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6063.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(_6074.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation(self)
