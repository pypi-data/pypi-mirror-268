"""PlanetaryGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6465
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PlanetaryGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6476,
        _6514,
        _6416,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundDynamicAnalysis")


class PlanetaryGearSetCompoundDynamicAnalysis(
    _6465.CylindricalGearSetCompoundDynamicAnalysis
):
    """PlanetaryGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundDynamicAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundDynamicAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
            parent: "PlanetaryGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6465.CylindricalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6465.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6476.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(_6476.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6514.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6416.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "PlanetaryGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6371.PlanetaryGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis]

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
    ) -> "List[_6371.PlanetaryGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis]

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
    ) -> "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis":
        return self._Cast_PlanetaryGearSetCompoundDynamicAnalysis(self)
