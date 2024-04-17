"""HypoidGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "HypoidGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.system_deflections import _2772
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4374,
        _4373,
        _4338,
        _4371,
        _4420,
        _4304,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="HypoidGearSetParametricStudyTool")


class HypoidGearSetParametricStudyTool(
    _4310.AGMAGleasonConicalGearSetParametricStudyTool
):
    """HypoidGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetParametricStudyTool")

    class _Cast_HypoidGearSetParametricStudyTool:
        """Special nested class for casting HypoidGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
            parent: "HypoidGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4310.AGMAGleasonConicalGearSetParametricStudyTool":
            return self._parent._cast(
                _4310.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4338.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4371.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(_4371.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4420.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4304.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "HypoidGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6916.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2772.HypoidGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4374.HypoidGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4373.HypoidGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool":
        return self._Cast_HypoidGearSetParametricStudyTool(self)
