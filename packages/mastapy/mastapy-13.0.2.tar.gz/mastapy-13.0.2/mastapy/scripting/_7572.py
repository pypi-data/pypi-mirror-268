"""SMTBitmap"""

from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy import _7561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SMT_BITMAP = python_net_import("SMT.MastaAPIUtility.Scripting", "SMTBitmap")


__docformat__ = "restructuredtext en"
__all__ = ("SMTBitmap",)


Self = TypeVar("Self", bound="SMTBitmap")


class SMTBitmap(_7561.MarshalByRefObjectPermanent):
    """SMTBitmap

    This is a mastapy class.
    """

    TYPE = _SMT_BITMAP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SMTBitmap")

    class _Cast_SMTBitmap:
        """Special nested class for casting SMTBitmap to subclasses."""

        def __init__(self: "SMTBitmap._Cast_SMTBitmap", parent: "SMTBitmap"):
            self._parent = parent

        @property
        def smt_bitmap(self: "SMTBitmap._Cast_SMTBitmap") -> "SMTBitmap":
            return self._parent

        def __getattr__(self: "SMTBitmap._Cast_SMTBitmap", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SMTBitmap.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def to_image(self: Self) -> "Image":
        """Image"""
        return conversion.pn_to_mp_image(self.wrapped.ToImage())

    def to_bytes(self: Self) -> "bytes":
        """bytes"""
        return conversion.pn_to_mp_bytes(self.wrapped.ToBytes())

    @property
    def cast_to(self: Self) -> "SMTBitmap._Cast_SMTBitmap":
        return self._Cast_SMTBitmap(self)
