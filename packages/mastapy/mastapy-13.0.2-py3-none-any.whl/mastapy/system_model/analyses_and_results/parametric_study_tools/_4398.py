"""ParametricStudyToolResultsForReporting"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_TOOL_RESULTS_FOR_REPORTING = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyToolResultsForReporting",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyToolResultsForReporting",)


Self = TypeVar("Self", bound="ParametricStudyToolResultsForReporting")


class ParametricStudyToolResultsForReporting(_0.APIBase):
    """ParametricStudyToolResultsForReporting

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_TOOL_RESULTS_FOR_REPORTING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParametricStudyToolResultsForReporting"
    )

    class _Cast_ParametricStudyToolResultsForReporting:
        """Special nested class for casting ParametricStudyToolResultsForReporting to subclasses."""

        def __init__(
            self: "ParametricStudyToolResultsForReporting._Cast_ParametricStudyToolResultsForReporting",
            parent: "ParametricStudyToolResultsForReporting",
        ):
            self._parent = parent

        @property
        def parametric_study_tool_results_for_reporting(
            self: "ParametricStudyToolResultsForReporting._Cast_ParametricStudyToolResultsForReporting",
        ) -> "ParametricStudyToolResultsForReporting":
            return self._parent

        def __getattr__(
            self: "ParametricStudyToolResultsForReporting._Cast_ParametricStudyToolResultsForReporting",
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
        self: Self, instance_to_wrap: "ParametricStudyToolResultsForReporting.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParametricStudyToolResultsForReporting._Cast_ParametricStudyToolResultsForReporting":
        return self._Cast_ParametricStudyToolResultsForReporting(self)
