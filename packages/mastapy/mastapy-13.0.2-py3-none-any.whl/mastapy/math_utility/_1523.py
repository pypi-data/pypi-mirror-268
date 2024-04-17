"""HarmonicValue"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_VALUE = python_net_import("SMT.MastaAPI.MathUtility", "HarmonicValue")


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicValue",)


Self = TypeVar("Self", bound="HarmonicValue")


class HarmonicValue(_0.APIBase):
    """HarmonicValue

    This is a mastapy class.
    """

    TYPE = _HARMONIC_VALUE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicValue")

    class _Cast_HarmonicValue:
        """Special nested class for casting HarmonicValue to subclasses."""

        def __init__(
            self: "HarmonicValue._Cast_HarmonicValue", parent: "HarmonicValue"
        ):
            self._parent = parent

        @property
        def harmonic_value(
            self: "HarmonicValue._Cast_HarmonicValue",
        ) -> "HarmonicValue":
            return self._parent

        def __getattr__(self: "HarmonicValue._Cast_HarmonicValue", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicValue.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def amplitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Amplitude

        if temp is None:
            return 0.0

        return temp

    @property
    def harmonic_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicIndex

        if temp is None:
            return 0

        return temp

    @property
    def phase(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Phase

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "HarmonicValue._Cast_HarmonicValue":
        return self._Cast_HarmonicValue(self)
