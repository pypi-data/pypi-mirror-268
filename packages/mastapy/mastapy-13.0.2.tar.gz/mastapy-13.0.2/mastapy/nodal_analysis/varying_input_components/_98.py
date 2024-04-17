"""ForceInputComponent"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.varying_input_components import _96
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_INPUT_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "ForceInputComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForceInputComponent",)


Self = TypeVar("Self", bound="ForceInputComponent")


class ForceInputComponent(_96.AbstractVaryingInputComponent):
    """ForceInputComponent

    This is a mastapy class.
    """

    TYPE = _FORCE_INPUT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForceInputComponent")

    class _Cast_ForceInputComponent:
        """Special nested class for casting ForceInputComponent to subclasses."""

        def __init__(
            self: "ForceInputComponent._Cast_ForceInputComponent",
            parent: "ForceInputComponent",
        ):
            self._parent = parent

        @property
        def abstract_varying_input_component(
            self: "ForceInputComponent._Cast_ForceInputComponent",
        ) -> "_96.AbstractVaryingInputComponent":
            return self._parent._cast(_96.AbstractVaryingInputComponent)

        @property
        def force_input_component(
            self: "ForceInputComponent._Cast_ForceInputComponent",
        ) -> "ForceInputComponent":
            return self._parent

        def __getattr__(
            self: "ForceInputComponent._Cast_ForceInputComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForceInputComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Force

        if temp is None:
            return 0.0

        return temp

    @force.setter
    @enforce_parameter_types
    def force(self: Self, value: "float"):
        self.wrapped.Force = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ForceInputComponent._Cast_ForceInputComponent":
        return self._Cast_ForceInputComponent(self)
