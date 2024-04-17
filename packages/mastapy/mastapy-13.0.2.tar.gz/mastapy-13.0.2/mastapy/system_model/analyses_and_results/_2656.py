"""AnalysisCaseVariable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE_VARIABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "AnalysisCaseVariable"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4400


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisCaseVariable",)


Self = TypeVar("Self", bound="AnalysisCaseVariable")


class AnalysisCaseVariable(_0.APIBase):
    """AnalysisCaseVariable

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE_VARIABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisCaseVariable")

    class _Cast_AnalysisCaseVariable:
        """Special nested class for casting AnalysisCaseVariable to subclasses."""

        def __init__(
            self: "AnalysisCaseVariable._Cast_AnalysisCaseVariable",
            parent: "AnalysisCaseVariable",
        ):
            self._parent = parent

        @property
        def parametric_study_variable(
            self: "AnalysisCaseVariable._Cast_AnalysisCaseVariable",
        ) -> "_4400.ParametricStudyVariable":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.ParametricStudyVariable)

        @property
        def analysis_case_variable(
            self: "AnalysisCaseVariable._Cast_AnalysisCaseVariable",
        ) -> "AnalysisCaseVariable":
            return self._parent

        def __getattr__(
            self: "AnalysisCaseVariable._Cast_AnalysisCaseVariable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisCaseVariable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def entity_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntityName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "AnalysisCaseVariable._Cast_AnalysisCaseVariable":
        return self._Cast_AnalysisCaseVariable(self)
