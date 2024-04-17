"""CVTPulleyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CVTPulleyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4342,
        _4389,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyParametricStudyTool",)


Self = TypeVar("Self", bound="CVTPulleyParametricStudyTool")


class CVTPulleyParametricStudyTool(_4410.PulleyParametricStudyTool):
    """CVTPulleyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyParametricStudyTool")

    class _Cast_CVTPulleyParametricStudyTool:
        """Special nested class for casting CVTPulleyParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
            parent: "CVTPulleyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def pulley_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4410.PulleyParametricStudyTool":
            return self._parent._cast(_4410.PulleyParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4342.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
        ) -> "CVTPulleyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2595.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyParametricStudyTool._Cast_CVTPulleyParametricStudyTool":
        return self._Cast_CVTPulleyParametricStudyTool(self)
