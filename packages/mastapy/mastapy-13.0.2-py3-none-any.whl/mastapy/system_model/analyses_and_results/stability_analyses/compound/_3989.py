"""PlanetaryGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PlanetaryGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3857
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3965,
        _4003,
        _3905,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundStabilityAnalysis")


class PlanetaryGearSetCompoundStabilityAnalysis(
    _3954.CylindricalGearSetCompoundStabilityAnalysis
):
    """PlanetaryGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundStabilityAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
            parent: "PlanetaryGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3954.CylindricalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3954.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3965.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "PlanetaryGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3857.PlanetaryGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3857.PlanetaryGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis":
        return self._Cast_PlanetaryGearSetCompoundStabilityAnalysis(self)
