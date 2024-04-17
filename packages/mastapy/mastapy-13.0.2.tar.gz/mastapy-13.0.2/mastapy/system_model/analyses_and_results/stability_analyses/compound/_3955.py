"""CylindricalPlanetGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3822
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3963,
        _3982,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundStabilityAnalysis")


class CylindricalPlanetGearCompoundStabilityAnalysis(
    _3952.CylindricalGearCompoundStabilityAnalysis
):
    """CylindricalPlanetGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundStabilityAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundStabilityAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
            parent: "CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_3952.CylindricalGearCompoundStabilityAnalysis":
            return self._parent._cast(_3952.CylindricalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_3963.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "CylindricalPlanetGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3822.CylindricalPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalPlanetGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3822.CylindricalPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalPlanetGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundStabilityAnalysis(self)
