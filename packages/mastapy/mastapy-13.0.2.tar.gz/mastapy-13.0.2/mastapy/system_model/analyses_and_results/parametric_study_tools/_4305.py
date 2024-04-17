"""AbstractShaftOrHousingParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractShaftOrHousingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4306,
        _4349,
        _4367,
        _4418,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingParametricStudyTool")


class AbstractShaftOrHousingParametricStudyTool(_4329.ComponentParametricStudyTool):
    """AbstractShaftOrHousingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingParametricStudyTool"
    )

    class _Cast_AbstractShaftOrHousingParametricStudyTool:
        """Special nested class for casting AbstractShaftOrHousingParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
            parent: "AbstractShaftOrHousingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4306.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.AbstractShaftParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4349.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4349,
            )

            return self._parent._cast(_4349.CycloidalDiscParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4367.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(_4367.FEPartParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4418.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.ShaftParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "AbstractShaftOrHousingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2443.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool":
        return self._Cast_AbstractShaftOrHousingParametricStudyTool(self)
