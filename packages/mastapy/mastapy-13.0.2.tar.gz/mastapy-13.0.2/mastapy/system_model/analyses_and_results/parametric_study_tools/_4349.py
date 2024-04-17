"""CycloidalDiscParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CycloidalDiscParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.system_deflections import _2746
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4305,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscParametricStudyTool",)


Self = TypeVar("Self", bound="CycloidalDiscParametricStudyTool")


class CycloidalDiscParametricStudyTool(_4306.AbstractShaftParametricStudyTool):
    """CycloidalDiscParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscParametricStudyTool")

    class _Cast_CycloidalDiscParametricStudyTool:
        """Special nested class for casting CycloidalDiscParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
            parent: "CycloidalDiscParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_4306.AbstractShaftParametricStudyTool":
            return self._parent._cast(_4306.AbstractShaftParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_4305.AbstractShaftOrHousingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "CycloidalDiscParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6868.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "List[_2746.CycloidalDiscSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection]

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
    ) -> "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool":
        return self._Cast_CycloidalDiscParametricStudyTool(self)
