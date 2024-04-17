"""PartToPartShearCouplingConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4489,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4516,
        _4486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionCompoundParametricStudyTool"
)


class PartToPartShearCouplingConnectionCompoundParametricStudyTool(
    _4489.CouplingConnectionCompoundParametricStudyTool
):
    """PartToPartShearCouplingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
            parent: "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "_4489.CouplingConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4489.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "_4516.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "_4486.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
        ) -> "PartToPartShearCouplingConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4402.PartToPartShearCouplingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingConnectionParametricStudyTool]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4402.PartToPartShearCouplingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingConnectionParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionCompoundParametricStudyTool._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool":
        return self._Cast_PartToPartShearCouplingConnectionCompoundParametricStudyTool(
            self
        )
