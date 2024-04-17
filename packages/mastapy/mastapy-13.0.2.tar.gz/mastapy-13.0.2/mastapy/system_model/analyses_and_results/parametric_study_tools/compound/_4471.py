"""BoltedJointCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4549,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BoltedJointCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6839
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4323
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4451,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BoltedJointCompoundParametricStudyTool")


class BoltedJointCompoundParametricStudyTool(
    _4549.SpecialisedAssemblyCompoundParametricStudyTool
):
    """BoltedJointCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltedJointCompoundParametricStudyTool"
    )

    class _Cast_BoltedJointCompoundParametricStudyTool:
        """Special nested class for casting BoltedJointCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
            parent: "BoltedJointCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "_4549.SpecialisedAssemblyCompoundParametricStudyTool":
            return self._parent._cast(
                _4549.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "_4451.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
        ) -> "BoltedJointCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "BoltedJointCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2450.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6839.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

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
    ) -> "List[_4323.BoltedJointParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BoltedJointParametricStudyTool]

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
    ) -> "List[_4323.BoltedJointParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BoltedJointParametricStudyTool]

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
    ) -> "BoltedJointCompoundParametricStudyTool._Cast_BoltedJointCompoundParametricStudyTool":
        return self._Cast_BoltedJointCompoundParametricStudyTool(self)
