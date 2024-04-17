"""OverridableTolerance"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "OverridableTolerance",
)


__docformat__ = "restructuredtext en"
__all__ = ("OverridableTolerance",)


Self = TypeVar("Self", bound="OverridableTolerance")


class OverridableTolerance(_0.APIBase):
    """OverridableTolerance

    This is a mastapy class.
    """

    TYPE = _OVERRIDABLE_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OverridableTolerance")

    class _Cast_OverridableTolerance:
        """Special nested class for casting OverridableTolerance to subclasses."""

        def __init__(
            self: "OverridableTolerance._Cast_OverridableTolerance",
            parent: "OverridableTolerance",
        ):
            self._parent = parent

        @property
        def overridable_tolerance(
            self: "OverridableTolerance._Cast_OverridableTolerance",
        ) -> "OverridableTolerance":
            return self._parent

        def __getattr__(
            self: "OverridableTolerance._Cast_OverridableTolerance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OverridableTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def standard_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StandardValue

        if temp is None:
            return 0.0

        return temp

    @property
    def value(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @value.setter
    @enforce_parameter_types
    def value(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Value = value

    @property
    def cast_to(self: Self) -> "OverridableTolerance._Cast_OverridableTolerance":
        return self._Cast_OverridableTolerance(self)
