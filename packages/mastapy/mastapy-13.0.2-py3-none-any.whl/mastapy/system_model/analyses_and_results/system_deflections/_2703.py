"""BearingDynamicPostAnalysisResultWrapper"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_POST_ANALYSIS_RESULT_WRAPPER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BearingDynamicPostAnalysisResultWrapper",
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingDynamicPostAnalysisResultWrapper",)


Self = TypeVar("Self", bound="BearingDynamicPostAnalysisResultWrapper")


class BearingDynamicPostAnalysisResultWrapper(_0.APIBase):
    """BearingDynamicPostAnalysisResultWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_POST_ANALYSIS_RESULT_WRAPPER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingDynamicPostAnalysisResultWrapper"
    )

    class _Cast_BearingDynamicPostAnalysisResultWrapper:
        """Special nested class for casting BearingDynamicPostAnalysisResultWrapper to subclasses."""

        def __init__(
            self: "BearingDynamicPostAnalysisResultWrapper._Cast_BearingDynamicPostAnalysisResultWrapper",
            parent: "BearingDynamicPostAnalysisResultWrapper",
        ):
            self._parent = parent

        @property
        def bearing_dynamic_post_analysis_result_wrapper(
            self: "BearingDynamicPostAnalysisResultWrapper._Cast_BearingDynamicPostAnalysisResultWrapper",
        ) -> "BearingDynamicPostAnalysisResultWrapper":
            return self._parent

        def __getattr__(
            self: "BearingDynamicPostAnalysisResultWrapper._Cast_BearingDynamicPostAnalysisResultWrapper",
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
        self: Self, instance_to_wrap: "BearingDynamicPostAnalysisResultWrapper.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def plot(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Plot

        if temp is None:
            return False

        return temp

    @plot.setter
    @enforce_parameter_types
    def plot(self: Self, value: "bool"):
        self.wrapped.Plot = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "BearingDynamicPostAnalysisResultWrapper._Cast_BearingDynamicPostAnalysisResultWrapper":
        return self._Cast_BearingDynamicPostAnalysisResultWrapper(self)
