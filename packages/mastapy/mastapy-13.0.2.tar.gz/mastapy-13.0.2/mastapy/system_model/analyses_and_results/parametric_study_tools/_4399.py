"""ParametricStudyToolStepResult"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_TOOL_STEP_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyToolStepResult",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyToolStepResult",)


Self = TypeVar("Self", bound="ParametricStudyToolStepResult")


class ParametricStudyToolStepResult(_0.APIBase):
    """ParametricStudyToolStepResult

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_TOOL_STEP_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyToolStepResult")

    class _Cast_ParametricStudyToolStepResult:
        """Special nested class for casting ParametricStudyToolStepResult to subclasses."""

        def __init__(
            self: "ParametricStudyToolStepResult._Cast_ParametricStudyToolStepResult",
            parent: "ParametricStudyToolStepResult",
        ):
            self._parent = parent

        @property
        def parametric_study_tool_step_result(
            self: "ParametricStudyToolStepResult._Cast_ParametricStudyToolStepResult",
        ) -> "ParametricStudyToolStepResult":
            return self._parent

        def __getattr__(
            self: "ParametricStudyToolStepResult._Cast_ParametricStudyToolStepResult",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyToolStepResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def failure_message(self: Self) -> "str":
        """str"""
        temp = self.wrapped.FailureMessage

        if temp is None:
            return ""

        return temp

    @failure_message.setter
    @enforce_parameter_types
    def failure_message(self: Self, value: "str"):
        self.wrapped.FailureMessage = str(value) if value is not None else ""

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def successful(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp

    @successful.setter
    @enforce_parameter_types
    def successful(self: Self, value: "bool"):
        self.wrapped.Successful = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "ParametricStudyToolStepResult._Cast_ParametricStudyToolStepResult":
        return self._Cast_ParametricStudyToolStepResult(self)
