"""MaxStripLoadStressObject"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAX_STRIP_LOAD_STRESS_OBJECT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "MaxStripLoadStressObject"
)


__docformat__ = "restructuredtext en"
__all__ = ("MaxStripLoadStressObject",)


Self = TypeVar("Self", bound="MaxStripLoadStressObject")


class MaxStripLoadStressObject(_0.APIBase):
    """MaxStripLoadStressObject

    This is a mastapy class.
    """

    TYPE = _MAX_STRIP_LOAD_STRESS_OBJECT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaxStripLoadStressObject")

    class _Cast_MaxStripLoadStressObject:
        """Special nested class for casting MaxStripLoadStressObject to subclasses."""

        def __init__(
            self: "MaxStripLoadStressObject._Cast_MaxStripLoadStressObject",
            parent: "MaxStripLoadStressObject",
        ):
            self._parent = parent

        @property
        def max_strip_load_stress_object(
            self: "MaxStripLoadStressObject._Cast_MaxStripLoadStressObject",
        ) -> "MaxStripLoadStressObject":
            return self._parent

        def __getattr__(
            self: "MaxStripLoadStressObject._Cast_MaxStripLoadStressObject", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaxStripLoadStressObject.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_strip_load(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumStripLoad

        if temp is None:
            return 0.0

        return temp

    @maximum_strip_load.setter
    @enforce_parameter_types
    def maximum_strip_load(self: Self, value: "float"):
        self.wrapped.MaximumStripLoad = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "MaxStripLoadStressObject._Cast_MaxStripLoadStressObject":
        return self._Cast_MaxStripLoadStressObject(self)
