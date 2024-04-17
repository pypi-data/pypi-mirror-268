"""CustomReportKey"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_KEY = python_net_import("SMT.MastaAPI.Utility.Report", "CustomReportKey")


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportKey",)


Self = TypeVar("Self", bound="CustomReportKey")


class CustomReportKey(_1833.DatabaseKey):
    """CustomReportKey

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportKey")

    class _Cast_CustomReportKey:
        """Special nested class for casting CustomReportKey to subclasses."""

        def __init__(
            self: "CustomReportKey._Cast_CustomReportKey", parent: "CustomReportKey"
        ):
            self._parent = parent

        @property
        def database_key(
            self: "CustomReportKey._Cast_CustomReportKey",
        ) -> "_1833.DatabaseKey":
            return self._parent._cast(_1833.DatabaseKey)

        @property
        def custom_report_key(
            self: "CustomReportKey._Cast_CustomReportKey",
        ) -> "CustomReportKey":
            return self._parent

        def __getattr__(self: "CustomReportKey._Cast_CustomReportKey", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomReportKey._Cast_CustomReportKey":
        return self._Cast_CustomReportKey(self)
