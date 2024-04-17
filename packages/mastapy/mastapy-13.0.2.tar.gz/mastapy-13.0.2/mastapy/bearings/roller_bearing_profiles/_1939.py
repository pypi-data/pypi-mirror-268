"""RollerBearingDinLundbergProfile"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility import _1517
from mastapy.bearings.roller_bearing_profiles import _1943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_DIN_LUNDBERG_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingDinLundbergProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingDinLundbergProfile",)


Self = TypeVar("Self", bound="RollerBearingDinLundbergProfile")


class RollerBearingDinLundbergProfile(_1943.RollerBearingProfile):
    """RollerBearingDinLundbergProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_DIN_LUNDBERG_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingDinLundbergProfile")

    class _Cast_RollerBearingDinLundbergProfile:
        """Special nested class for casting RollerBearingDinLundbergProfile to subclasses."""

        def __init__(
            self: "RollerBearingDinLundbergProfile._Cast_RollerBearingDinLundbergProfile",
            parent: "RollerBearingDinLundbergProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_profile(
            self: "RollerBearingDinLundbergProfile._Cast_RollerBearingDinLundbergProfile",
        ) -> "_1943.RollerBearingProfile":
            return self._parent._cast(_1943.RollerBearingProfile)

        @property
        def roller_bearing_din_lundberg_profile(
            self: "RollerBearingDinLundbergProfile._Cast_RollerBearingDinLundbergProfile",
        ) -> "RollerBearingDinLundbergProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingDinLundbergProfile._Cast_RollerBearingDinLundbergProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingDinLundbergProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_offset(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_offset.setter
    @enforce_parameter_types
    def axial_offset(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialOffset = value

    @property
    def effective_length(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EffectiveLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @effective_length.setter
    @enforce_parameter_types
    def effective_length(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EffectiveLength = value

    @property
    def extrapolation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions":
        """EnumWithSelectedValue[mastapy.math_utility.ExtrapolationOptions]"""
        temp = self.wrapped.ExtrapolationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @extrapolation_method.setter
    @enforce_parameter_types
    def extrapolation_method(self: Self, value: "_1517.ExtrapolationOptions"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExtrapolationMethod = value

    @property
    def cast_to(
        self: Self,
    ) -> "RollerBearingDinLundbergProfile._Cast_RollerBearingDinLundbergProfile":
        return self._Cast_RollerBearingDinLundbergProfile(self)
