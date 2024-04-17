"""CouplingConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4516,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CouplingConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4473,
        _4478,
        _4532,
        _4554,
        _4569,
        _4486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundParametricStudyTool")


class CouplingConnectionCompoundParametricStudyTool(
    _4516.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """CouplingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundParametricStudyTool"
    )

    class _Cast_CouplingConnectionCompoundParametricStudyTool:
        """Special nested class for casting CouplingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
            parent: "CouplingConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4516.InterMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4516.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4486.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4473.ClutchConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ClutchConnectionCompoundParametricStudyTool)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4478.ConceptCouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(
                _4478.ConceptCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4532.PartToPartShearCouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(
                _4532.PartToPartShearCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4554.SpringDamperConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.SpringDamperConnectionCompoundParametricStudyTool
            )

        @property
        def torque_converter_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "_4569.TorqueConverterConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4569,
            )

            return self._parent._cast(
                _4569.TorqueConverterConnectionCompoundParametricStudyTool
            )

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
        ) -> "CouplingConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "CouplingConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4341.CouplingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4341.CouplingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool":
        return self._Cast_CouplingConnectionCompoundParametricStudyTool(self)
