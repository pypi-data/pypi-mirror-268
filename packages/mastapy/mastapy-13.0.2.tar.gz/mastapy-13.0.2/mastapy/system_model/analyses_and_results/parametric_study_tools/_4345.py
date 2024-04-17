"""CVTParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CVTParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4420,
        _4304,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTParametricStudyTool",)


Self = TypeVar("Self", bound="CVTParametricStudyTool")


class CVTParametricStudyTool(_4314.BeltDriveParametricStudyTool):
    """CVTParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTParametricStudyTool")

    class _Cast_CVTParametricStudyTool:
        """Special nested class for casting CVTParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
            parent: "CVTParametricStudyTool",
        ):
            self._parent = parent

        @property
        def belt_drive_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_4314.BeltDriveParametricStudyTool":
            return self._parent._cast(_4314.BeltDriveParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_4420.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_4304.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "CVTParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTParametricStudyTool._Cast_CVTParametricStudyTool":
        return self._Cast_CVTParametricStudyTool(self)
