"""PlungeShaverRedressing"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _767,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_REDRESSING = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShaverRedressing",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverRedressing",)


Self = TypeVar("Self", bound="PlungeShaverRedressing")


class PlungeShaverRedressing(_767.ShaverRedressing["_758.PlungeShaverDynamics"]):
    """PlungeShaverRedressing

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_REDRESSING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverRedressing")

    class _Cast_PlungeShaverRedressing:
        """Special nested class for casting PlungeShaverRedressing to subclasses."""

        def __init__(
            self: "PlungeShaverRedressing._Cast_PlungeShaverRedressing",
            parent: "PlungeShaverRedressing",
        ):
            self._parent = parent

        @property
        def shaver_redressing(
            self: "PlungeShaverRedressing._Cast_PlungeShaverRedressing",
        ) -> "_767.ShaverRedressing":
            return self._parent._cast(_767.ShaverRedressing)

        @property
        def plunge_shaver_redressing(
            self: "PlungeShaverRedressing._Cast_PlungeShaverRedressing",
        ) -> "PlungeShaverRedressing":
            return self._parent

        def __getattr__(
            self: "PlungeShaverRedressing._Cast_PlungeShaverRedressing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverRedressing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PlungeShaverRedressing._Cast_PlungeShaverRedressing":
        return self._Cast_PlungeShaverRedressing(self)
