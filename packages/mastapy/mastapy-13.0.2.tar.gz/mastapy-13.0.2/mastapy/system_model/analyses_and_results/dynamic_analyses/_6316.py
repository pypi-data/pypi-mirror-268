"""ConceptGearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConceptGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.static_loads import _6852
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6314,
        _6315,
        _6385,
        _6285,
        _6366,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetDynamicAnalysis")


class ConceptGearSetDynamicAnalysis(_6347.GearSetDynamicAnalysis):
    """ConceptGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetDynamicAnalysis")

    class _Cast_ConceptGearSetDynamicAnalysis:
        """Special nested class for casting ConceptGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
            parent: "ConceptGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_dynamic_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_6347.GearSetDynamicAnalysis":
            return self._parent._cast(_6347.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_6285.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
        ) -> "ConceptGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2529.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6852.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6314.ConceptGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6315.ConceptGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetDynamicAnalysis._Cast_ConceptGearSetDynamicAnalysis":
        return self._Cast_ConceptGearSetDynamicAnalysis(self)
