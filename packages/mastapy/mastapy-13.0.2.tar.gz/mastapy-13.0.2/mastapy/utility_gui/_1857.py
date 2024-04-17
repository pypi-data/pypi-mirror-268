"""DataLoggerWithCharts"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.math_utility.convergence import _1582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_LOGGER_WITH_CHARTS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "DataLoggerWithCharts"
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1856


__docformat__ = "restructuredtext en"
__all__ = ("DataLoggerWithCharts",)


Self = TypeVar("Self", bound="DataLoggerWithCharts")


class DataLoggerWithCharts(_1582.DataLogger):
    """DataLoggerWithCharts

    This is a mastapy class.
    """

    TYPE = _DATA_LOGGER_WITH_CHARTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataLoggerWithCharts")

    class _Cast_DataLoggerWithCharts:
        """Special nested class for casting DataLoggerWithCharts to subclasses."""

        def __init__(
            self: "DataLoggerWithCharts._Cast_DataLoggerWithCharts",
            parent: "DataLoggerWithCharts",
        ):
            self._parent = parent

        @property
        def data_logger(
            self: "DataLoggerWithCharts._Cast_DataLoggerWithCharts",
        ) -> "_1582.DataLogger":
            return self._parent._cast(_1582.DataLogger)

        @property
        def data_logger_with_charts(
            self: "DataLoggerWithCharts._Cast_DataLoggerWithCharts",
        ) -> "DataLoggerWithCharts":
            return self._parent

        def __getattr__(
            self: "DataLoggerWithCharts._Cast_DataLoggerWithCharts", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataLoggerWithCharts.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def logged_items(self: Self) -> "List[_1856.DataLoggerItem]":
        """List[mastapy.utility_gui.DataLoggerItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoggedItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "DataLoggerWithCharts._Cast_DataLoggerWithCharts":
        return self._Cast_DataLoggerWithCharts(self)
