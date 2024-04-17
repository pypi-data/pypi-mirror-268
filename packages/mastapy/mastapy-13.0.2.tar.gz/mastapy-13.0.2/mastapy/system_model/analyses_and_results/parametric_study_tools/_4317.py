"""BevelDifferentialGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelDifferentialGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6833
    from mastapy.system_model.analyses_and_results.system_deflections import _2710
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4316,
        _4315,
        _4310,
        _4338,
        _4371,
        _4420,
        _4304,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetParametricStudyTool")


class BevelDifferentialGearSetParametricStudyTool(
    _4322.BevelGearSetParametricStudyTool
):
    """BevelDifferentialGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetParametricStudyTool"
    )

    class _Cast_BevelDifferentialGearSetParametricStudyTool:
        """Special nested class for casting BevelDifferentialGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
            parent: "BevelDifferentialGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4322.BevelGearSetParametricStudyTool":
            return self._parent._cast(_4322.BevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4310.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(
                _4310.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4338.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4371.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(_4371.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4420.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4304.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "BevelDifferentialGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2523.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6833.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

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
    ) -> "List[_2710.BevelDifferentialGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection]

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
    def bevel_differential_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4316.BevelDifferentialGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4315.BevelDifferentialGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool":
        return self._Cast_BevelDifferentialGearSetParametricStudyTool(self)
