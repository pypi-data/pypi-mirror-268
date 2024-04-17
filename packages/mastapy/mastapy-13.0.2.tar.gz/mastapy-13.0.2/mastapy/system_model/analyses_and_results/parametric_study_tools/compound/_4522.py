"""KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4519,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6926
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4520,
        _4521,
        _4485,
        _4511,
        _4549,
        _4451,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool(
    _4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            return self._parent._cast(
                _4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_4485.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_4511.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_4549.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_4451.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4382.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundParametricStudyTool
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_parametric_study_tool(
        self: Self,
    ) -> (
        "List[_4521.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool]"
    ):
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundParametricStudyTool
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4382.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool(
                self
            )
        )
