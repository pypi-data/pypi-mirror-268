"""AngleInputComponent"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.varying_input_components import _96
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_INPUT_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "AngleInputComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngleInputComponent",)


Self = TypeVar("Self", bound="AngleInputComponent")


class AngleInputComponent(_96.AbstractVaryingInputComponent):
    """AngleInputComponent

    This is a mastapy class.
    """

    TYPE = _ANGLE_INPUT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngleInputComponent")

    class _Cast_AngleInputComponent:
        """Special nested class for casting AngleInputComponent to subclasses."""

        def __init__(
            self: "AngleInputComponent._Cast_AngleInputComponent",
            parent: "AngleInputComponent",
        ):
            self._parent = parent

        @property
        def abstract_varying_input_component(
            self: "AngleInputComponent._Cast_AngleInputComponent",
        ) -> "_96.AbstractVaryingInputComponent":
            return self._parent._cast(_96.AbstractVaryingInputComponent)

        @property
        def angle_input_component(
            self: "AngleInputComponent._Cast_AngleInputComponent",
        ) -> "AngleInputComponent":
            return self._parent

        def __getattr__(
            self: "AngleInputComponent._Cast_AngleInputComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngleInputComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "float"):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "AngleInputComponent._Cast_AngleInputComponent":
        return self._Cast_AngleInputComponent(self)
