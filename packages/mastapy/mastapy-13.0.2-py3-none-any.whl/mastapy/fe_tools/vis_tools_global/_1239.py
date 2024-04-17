"""ElementFace"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FACE = python_net_import("SMT.MastaAPI.FETools.VisToolsGlobal", "ElementFace")


__docformat__ = "restructuredtext en"
__all__ = ("ElementFace",)


Self = TypeVar("Self", bound="ElementFace")


class ElementFace(_0.APIBase):
    """ElementFace

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementFace")

    class _Cast_ElementFace:
        """Special nested class for casting ElementFace to subclasses."""

        def __init__(self: "ElementFace._Cast_ElementFace", parent: "ElementFace"):
            self._parent = parent

        @property
        def element_face(self: "ElementFace._Cast_ElementFace") -> "ElementFace":
            return self._parent

        def __getattr__(self: "ElementFace._Cast_ElementFace", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementFace.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElementFace._Cast_ElementFace":
        return self._Cast_ElementFace(self)
