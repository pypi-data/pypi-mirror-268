"""MeasuredAndFactorViewModel"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASURED_AND_FACTOR_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "MeasuredAndFactorViewModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("MeasuredAndFactorViewModel",)


Self = TypeVar("Self", bound="MeasuredAndFactorViewModel")


class MeasuredAndFactorViewModel(_0.APIBase):
    """MeasuredAndFactorViewModel

    This is a mastapy class.
    """

    TYPE = _MEASURED_AND_FACTOR_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasuredAndFactorViewModel")

    class _Cast_MeasuredAndFactorViewModel:
        """Special nested class for casting MeasuredAndFactorViewModel to subclasses."""

        def __init__(
            self: "MeasuredAndFactorViewModel._Cast_MeasuredAndFactorViewModel",
            parent: "MeasuredAndFactorViewModel",
        ):
            self._parent = parent

        @property
        def measured_and_factor_view_model(
            self: "MeasuredAndFactorViewModel._Cast_MeasuredAndFactorViewModel",
        ) -> "MeasuredAndFactorViewModel":
            return self._parent

        def __getattr__(
            self: "MeasuredAndFactorViewModel._Cast_MeasuredAndFactorViewModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasuredAndFactorViewModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def per_normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PerNormalModule

        if temp is None:
            return 0.0

        return temp

    @per_normal_module.setter
    @enforce_parameter_types
    def per_normal_module(self: Self, value: "float"):
        self.wrapped.PerNormalModule = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "MeasuredAndFactorViewModel._Cast_MeasuredAndFactorViewModel":
        return self._Cast_MeasuredAndFactorViewModel(self)
