"""NonDimensionalInputComponent"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.varying_input_components import _96
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_DIMENSIONAL_INPUT_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "NonDimensionalInputComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("NonDimensionalInputComponent",)


Self = TypeVar("Self", bound="NonDimensionalInputComponent")


class NonDimensionalInputComponent(_96.AbstractVaryingInputComponent):
    """NonDimensionalInputComponent

    This is a mastapy class.
    """

    TYPE = _NON_DIMENSIONAL_INPUT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonDimensionalInputComponent")

    class _Cast_NonDimensionalInputComponent:
        """Special nested class for casting NonDimensionalInputComponent to subclasses."""

        def __init__(
            self: "NonDimensionalInputComponent._Cast_NonDimensionalInputComponent",
            parent: "NonDimensionalInputComponent",
        ):
            self._parent = parent

        @property
        def abstract_varying_input_component(
            self: "NonDimensionalInputComponent._Cast_NonDimensionalInputComponent",
        ) -> "_96.AbstractVaryingInputComponent":
            return self._parent._cast(_96.AbstractVaryingInputComponent)

        @property
        def non_dimensional_input_component(
            self: "NonDimensionalInputComponent._Cast_NonDimensionalInputComponent",
        ) -> "NonDimensionalInputComponent":
            return self._parent

        def __getattr__(
            self: "NonDimensionalInputComponent._Cast_NonDimensionalInputComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonDimensionalInputComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def non_dimensional_quantity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NonDimensionalQuantity

        if temp is None:
            return 0.0

        return temp

    @non_dimensional_quantity.setter
    @enforce_parameter_types
    def non_dimensional_quantity(self: Self, value: "float"):
        self.wrapped.NonDimensionalQuantity = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "NonDimensionalInputComponent._Cast_NonDimensionalInputComponent":
        return self._Cast_NonDimensionalInputComponent(self)
