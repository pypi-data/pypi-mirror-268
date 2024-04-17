"""AnalysisSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS = python_net_import("SMT.MastaAPI.NodalAnalysis", "AnalysisSettings")


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisSettings",)


Self = TypeVar("Self", bound="AnalysisSettings")


class AnalysisSettings(_0.APIBase):
    """AnalysisSettings

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisSettings")

    class _Cast_AnalysisSettings:
        """Special nested class for casting AnalysisSettings to subclasses."""

        def __init__(
            self: "AnalysisSettings._Cast_AnalysisSettings", parent: "AnalysisSettings"
        ):
            self._parent = parent

        @property
        def analysis_settings(
            self: "AnalysisSettings._Cast_AnalysisSettings",
        ) -> "AnalysisSettings":
            return self._parent

        def __getattr__(self: "AnalysisSettings._Cast_AnalysisSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AnalysisSettings._Cast_AnalysisSettings":
        return self._Cast_AnalysisSettings(self)
