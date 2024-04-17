"""AxialShaverRedressing"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _767,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_SHAVER_REDRESSING = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "AxialShaverRedressing",
)


__docformat__ = "restructuredtext en"
__all__ = ("AxialShaverRedressing",)


Self = TypeVar("Self", bound="AxialShaverRedressing")


class AxialShaverRedressing(_767.ShaverRedressing["_754.ConventionalShavingDynamics"]):
    """AxialShaverRedressing

    This is a mastapy class.
    """

    TYPE = _AXIAL_SHAVER_REDRESSING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxialShaverRedressing")

    class _Cast_AxialShaverRedressing:
        """Special nested class for casting AxialShaverRedressing to subclasses."""

        def __init__(
            self: "AxialShaverRedressing._Cast_AxialShaverRedressing",
            parent: "AxialShaverRedressing",
        ):
            self._parent = parent

        @property
        def shaver_redressing(
            self: "AxialShaverRedressing._Cast_AxialShaverRedressing",
        ) -> "_767.ShaverRedressing":
            return self._parent._cast(_767.ShaverRedressing)

        @property
        def axial_shaver_redressing(
            self: "AxialShaverRedressing._Cast_AxialShaverRedressing",
        ) -> "AxialShaverRedressing":
            return self._parent

        def __getattr__(
            self: "AxialShaverRedressing._Cast_AxialShaverRedressing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AxialShaverRedressing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AxialShaverRedressing._Cast_AxialShaverRedressing":
        return self._Cast_AxialShaverRedressing(self)
