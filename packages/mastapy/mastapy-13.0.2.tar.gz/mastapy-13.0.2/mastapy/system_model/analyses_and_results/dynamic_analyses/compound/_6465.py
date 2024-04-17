"""CylindricalGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6476
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CylindricalGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6463,
        _6464,
        _6500,
        _6514,
        _6416,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetCompoundDynamicAnalysis")


class CylindricalGearSetCompoundDynamicAnalysis(_6476.GearSetCompoundDynamicAnalysis):
    """CylindricalGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetCompoundDynamicAnalysis"
    )

    class _Cast_CylindricalGearSetCompoundDynamicAnalysis:
        """Special nested class for casting CylindricalGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
            parent: "CylindricalGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_dynamic_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_6476.GearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6476.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_6514.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_6416.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "_6500.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
        ) -> "CylindricalGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearSetCompoundDynamicAnalysis.TYPE"
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
    ) -> "List[_6334.CylindricalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearSetDynamicAnalysis]

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
    def cylindrical_gears_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6463.CylindricalGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6464.CylindricalGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6334.CylindricalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearSetDynamicAnalysis]

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
    ) -> "CylindricalGearSetCompoundDynamicAnalysis._Cast_CylindricalGearSetCompoundDynamicAnalysis":
        return self._Cast_CylindricalGearSetCompoundDynamicAnalysis(self)
