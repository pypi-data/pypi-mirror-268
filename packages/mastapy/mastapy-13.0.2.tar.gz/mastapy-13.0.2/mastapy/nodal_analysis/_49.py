"""AnalysisSettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "AnalysisSettingsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisSettingsDatabase",)


Self = TypeVar("Self", bound="AnalysisSettingsDatabase")


class AnalysisSettingsDatabase(_1835.NamedDatabase["_50.AnalysisSettingsItem"]):
    """AnalysisSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisSettingsDatabase")

    class _Cast_AnalysisSettingsDatabase:
        """Special nested class for casting AnalysisSettingsDatabase to subclasses."""

        def __init__(
            self: "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase",
            parent: "AnalysisSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def analysis_settings_database(
            self: "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase",
        ) -> "AnalysisSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisSettingsDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase":
        return self._Cast_AnalysisSettingsDatabase(self)
