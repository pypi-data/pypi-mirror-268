"""CylindricalGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3965
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CylindricalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.stability_analyses import _3820
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3952,
        _3953,
        _3989,
        _4003,
        _3905,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetCompoundStabilityAnalysis")


class CylindricalGearSetCompoundStabilityAnalysis(
    _3965.GearSetCompoundStabilityAnalysis
):
    """CylindricalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_CylindricalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting CylindricalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
            parent: "CylindricalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_stability_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_3965.GearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3965.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "_3989.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
        ) -> "CylindricalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3820.CylindricalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalGearSetStabilityAnalysis]

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
    def cylindrical_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_3952.CylindricalGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.CylindricalGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_3953.CylindricalGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.CylindricalGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3820.CylindricalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalGearSetStabilityAnalysis]

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
    ) -> "CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis":
        return self._Cast_CylindricalGearSetCompoundStabilityAnalysis(self)
