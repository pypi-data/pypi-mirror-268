"""ExternalCADModelParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ExternalCADModelParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.static_loads import _6892
    from mastapy.system_model.analyses_and_results.system_deflections import _2760
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelParametricStudyTool",)


Self = TypeVar("Self", bound="ExternalCADModelParametricStudyTool")


class ExternalCADModelParametricStudyTool(_4329.ComponentParametricStudyTool):
    """ExternalCADModelParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelParametricStudyTool")

    class _Cast_ExternalCADModelParametricStudyTool:
        """Special nested class for casting ExternalCADModelParametricStudyTool to subclasses."""

        def __init__(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
            parent: "ExternalCADModelParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_parametric_study_tool(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_parametric_study_tool(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
        ) -> "ExternalCADModelParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool",
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
        self: Self, instance_to_wrap: "ExternalCADModelParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6892.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2760.ExternalCADModelSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ExternalCADModelParametricStudyTool._Cast_ExternalCADModelParametricStudyTool"
    ):
        return self._Cast_ExternalCADModelParametricStudyTool(self)
