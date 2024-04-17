"""HypoidGearSetCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4457,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "HypoidGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4375
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4513,
        _4514,
        _4485,
        _4511,
        _4549,
        _4451,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundParametricStudyTool")


class HypoidGearSetCompoundParametricStudyTool(
    _4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool
):
    """HypoidGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetCompoundParametricStudyTool"
    )

    class _Cast_HypoidGearSetCompoundParametricStudyTool:
        """Special nested class for casting HypoidGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
            parent: "HypoidGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            return self._parent._cast(
                _4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_4485.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_4511.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_4549.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_4451.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
        ) -> "HypoidGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "HypoidGearSetCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2542.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6916.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

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
    ) -> "List[_4375.HypoidGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearSetParametricStudyTool]

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
    def hypoid_gears_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4513.HypoidGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4514.HypoidGearMeshCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearMeshCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4375.HypoidGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearSetParametricStudyTool]

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
    ) -> "HypoidGearSetCompoundParametricStudyTool._Cast_HypoidGearSetCompoundParametricStudyTool":
        return self._Cast_HypoidGearSetCompoundParametricStudyTool(self)
