"""BallBearingShoulderDefinition"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_BEARING_SHOULDER_DEFINITION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "BallBearingShoulderDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("BallBearingShoulderDefinition",)


Self = TypeVar("Self", bound="BallBearingShoulderDefinition")


class BallBearingShoulderDefinition(_0.APIBase):
    """BallBearingShoulderDefinition

    This is a mastapy class.
    """

    TYPE = _BALL_BEARING_SHOULDER_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BallBearingShoulderDefinition")

    class _Cast_BallBearingShoulderDefinition:
        """Special nested class for casting BallBearingShoulderDefinition to subclasses."""

        def __init__(
            self: "BallBearingShoulderDefinition._Cast_BallBearingShoulderDefinition",
            parent: "BallBearingShoulderDefinition",
        ):
            self._parent = parent

        @property
        def ball_bearing_shoulder_definition(
            self: "BallBearingShoulderDefinition._Cast_BallBearingShoulderDefinition",
        ) -> "BallBearingShoulderDefinition":
            return self._parent

        def __getattr__(
            self: "BallBearingShoulderDefinition._Cast_BallBearingShoulderDefinition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BallBearingShoulderDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chamfer(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Chamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @chamfer.setter
    @enforce_parameter_types
    def chamfer(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Chamfer = value

    @property
    def diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Diameter = value

    @property
    def height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Height

        if temp is None:
            return 0.0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: Self, value: "float"):
        self.wrapped.Height = float(value) if value is not None else 0.0

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
    def cast_to(
        self: Self,
    ) -> "BallBearingShoulderDefinition._Cast_BallBearingShoulderDefinition":
        return self._Cast_BallBearingShoulderDefinition(self)
