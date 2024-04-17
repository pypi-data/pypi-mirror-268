"""LoadedDeepGrooveBallBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DEEP_GROOVE_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedDeepGrooveBallBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2019, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDeepGrooveBallBearingRow",)


Self = TypeVar("Self", bound="LoadedDeepGrooveBallBearingRow")


class LoadedDeepGrooveBallBearingRow(_2010.LoadedBallBearingRow):
    """LoadedDeepGrooveBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_DEEP_GROOVE_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedDeepGrooveBallBearingRow")

    class _Cast_LoadedDeepGrooveBallBearingRow:
        """Special nested class for casting LoadedDeepGrooveBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedDeepGrooveBallBearingRow._Cast_LoadedDeepGrooveBallBearingRow",
            parent: "LoadedDeepGrooveBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(
            self: "LoadedDeepGrooveBallBearingRow._Cast_LoadedDeepGrooveBallBearingRow",
        ) -> "_2010.LoadedBallBearingRow":
            return self._parent._cast(_2010.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedDeepGrooveBallBearingRow._Cast_LoadedDeepGrooveBallBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(
            self: "LoadedDeepGrooveBallBearingRow._Cast_LoadedDeepGrooveBallBearingRow",
        ) -> "LoadedDeepGrooveBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedDeepGrooveBallBearingRow._Cast_LoadedDeepGrooveBallBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedDeepGrooveBallBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2019.LoadedDeepGrooveBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedDeepGrooveBallBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedDeepGrooveBallBearingRow._Cast_LoadedDeepGrooveBallBearingRow":
        return self._Cast_LoadedDeepGrooveBallBearingRow(self)
