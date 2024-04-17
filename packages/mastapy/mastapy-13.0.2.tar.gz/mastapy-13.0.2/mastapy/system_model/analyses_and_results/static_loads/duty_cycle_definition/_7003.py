"""LoadCaseNameOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_CASE_NAME_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "LoadCaseNameOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadCaseNameOptions",)


Self = TypeVar("Self", bound="LoadCaseNameOptions")


class LoadCaseNameOptions(_1854.ColumnInputOptions):
    """LoadCaseNameOptions

    This is a mastapy class.
    """

    TYPE = _LOAD_CASE_NAME_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadCaseNameOptions")

    class _Cast_LoadCaseNameOptions:
        """Special nested class for casting LoadCaseNameOptions to subclasses."""

        def __init__(
            self: "LoadCaseNameOptions._Cast_LoadCaseNameOptions",
            parent: "LoadCaseNameOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "LoadCaseNameOptions._Cast_LoadCaseNameOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def load_case_name_options(
            self: "LoadCaseNameOptions._Cast_LoadCaseNameOptions",
        ) -> "LoadCaseNameOptions":
            return self._parent

        def __getattr__(
            self: "LoadCaseNameOptions._Cast_LoadCaseNameOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadCaseNameOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LoadCaseNameOptions._Cast_LoadCaseNameOptions":
        return self._Cast_LoadCaseNameOptions(self)
