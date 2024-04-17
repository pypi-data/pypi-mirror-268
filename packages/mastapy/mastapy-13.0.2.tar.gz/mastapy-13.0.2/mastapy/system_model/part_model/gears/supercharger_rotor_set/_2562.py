"""BoostPressureInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOOST_PRESSURE_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "BoostPressureInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("BoostPressureInputOptions",)


Self = TypeVar("Self", bound="BoostPressureInputOptions")


class BoostPressureInputOptions(_1854.ColumnInputOptions):
    """BoostPressureInputOptions

    This is a mastapy class.
    """

    TYPE = _BOOST_PRESSURE_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoostPressureInputOptions")

    class _Cast_BoostPressureInputOptions:
        """Special nested class for casting BoostPressureInputOptions to subclasses."""

        def __init__(
            self: "BoostPressureInputOptions._Cast_BoostPressureInputOptions",
            parent: "BoostPressureInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "BoostPressureInputOptions._Cast_BoostPressureInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def boost_pressure_input_options(
            self: "BoostPressureInputOptions._Cast_BoostPressureInputOptions",
        ) -> "BoostPressureInputOptions":
            return self._parent

        def __getattr__(
            self: "BoostPressureInputOptions._Cast_BoostPressureInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoostPressureInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BoostPressureInputOptions._Cast_BoostPressureInputOptions":
        return self._Cast_BoostPressureInputOptions(self)
