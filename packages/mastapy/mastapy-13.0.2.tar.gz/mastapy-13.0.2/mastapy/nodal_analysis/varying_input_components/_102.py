"""VelocityInputComponent"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.varying_input_components import _96
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VELOCITY_INPUT_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "VelocityInputComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("VelocityInputComponent",)


Self = TypeVar("Self", bound="VelocityInputComponent")


class VelocityInputComponent(_96.AbstractVaryingInputComponent):
    """VelocityInputComponent

    This is a mastapy class.
    """

    TYPE = _VELOCITY_INPUT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VelocityInputComponent")

    class _Cast_VelocityInputComponent:
        """Special nested class for casting VelocityInputComponent to subclasses."""

        def __init__(
            self: "VelocityInputComponent._Cast_VelocityInputComponent",
            parent: "VelocityInputComponent",
        ):
            self._parent = parent

        @property
        def abstract_varying_input_component(
            self: "VelocityInputComponent._Cast_VelocityInputComponent",
        ) -> "_96.AbstractVaryingInputComponent":
            return self._parent._cast(_96.AbstractVaryingInputComponent)

        @property
        def velocity_input_component(
            self: "VelocityInputComponent._Cast_VelocityInputComponent",
        ) -> "VelocityInputComponent":
            return self._parent

        def __getattr__(
            self: "VelocityInputComponent._Cast_VelocityInputComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VelocityInputComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Velocity

        if temp is None:
            return 0.0

        return temp

    @velocity.setter
    @enforce_parameter_types
    def velocity(self: Self, value: "float"):
        self.wrapped.Velocity = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "VelocityInputComponent._Cast_VelocityInputComponent":
        return self._Cast_VelocityInputComponent(self)
