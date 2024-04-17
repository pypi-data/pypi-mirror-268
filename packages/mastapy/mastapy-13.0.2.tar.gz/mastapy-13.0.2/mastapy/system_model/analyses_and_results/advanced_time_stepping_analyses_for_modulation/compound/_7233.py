"""PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7198,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7104,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7209,
        _7247,
        _7149,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7209.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7104.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7104.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
