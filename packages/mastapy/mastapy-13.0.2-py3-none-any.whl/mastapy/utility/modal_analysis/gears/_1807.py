"""HarmonicOrderForTE"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ORDER_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "HarmonicOrderForTE"
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicOrderForTE",)


Self = TypeVar("Self", bound="HarmonicOrderForTE")


class HarmonicOrderForTE(_1809.OrderForTE):
    """HarmonicOrderForTE

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ORDER_FOR_TE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicOrderForTE")

    class _Cast_HarmonicOrderForTE:
        """Special nested class for casting HarmonicOrderForTE to subclasses."""

        def __init__(
            self: "HarmonicOrderForTE._Cast_HarmonicOrderForTE",
            parent: "HarmonicOrderForTE",
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "HarmonicOrderForTE._Cast_HarmonicOrderForTE",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def harmonic_order_for_te(
            self: "HarmonicOrderForTE._Cast_HarmonicOrderForTE",
        ) -> "HarmonicOrderForTE":
            return self._parent

        def __getattr__(self: "HarmonicOrderForTE._Cast_HarmonicOrderForTE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicOrderForTE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Harmonic

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: Self) -> "HarmonicOrderForTE._Cast_HarmonicOrderForTE":
        return self._Cast_HarmonicOrderForTE(self)
