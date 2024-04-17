"""ConnectorParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConnectorParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4312,
        _4390,
        _4417,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorParametricStudyTool",)


Self = TypeVar("Self", bound="ConnectorParametricStudyTool")


class ConnectorParametricStudyTool(_4389.MountableComponentParametricStudyTool):
    """ConnectorParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorParametricStudyTool")

    class _Cast_ConnectorParametricStudyTool:
        """Special nested class for casting ConnectorParametricStudyTool to subclasses."""

        def __init__(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
            parent: "ConnectorParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_4312.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BearingParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_4390.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.OilSealParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "_4417.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.ShaftHubConnectionParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "ConnectorParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool":
        return self._Cast_ConnectorParametricStudyTool(self)
