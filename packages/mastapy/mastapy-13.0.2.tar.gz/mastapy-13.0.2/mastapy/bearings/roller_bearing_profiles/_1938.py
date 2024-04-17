"""RollerBearingCrownedProfile"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.roller_bearing_profiles import _1943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_CROWNED_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingCrownedProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingCrownedProfile",)


Self = TypeVar("Self", bound="RollerBearingCrownedProfile")


class RollerBearingCrownedProfile(_1943.RollerBearingProfile):
    """RollerBearingCrownedProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_CROWNED_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingCrownedProfile")

    class _Cast_RollerBearingCrownedProfile:
        """Special nested class for casting RollerBearingCrownedProfile to subclasses."""

        def __init__(
            self: "RollerBearingCrownedProfile._Cast_RollerBearingCrownedProfile",
            parent: "RollerBearingCrownedProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_profile(
            self: "RollerBearingCrownedProfile._Cast_RollerBearingCrownedProfile",
        ) -> "_1943.RollerBearingProfile":
            return self._parent._cast(_1943.RollerBearingProfile)

        @property
        def roller_bearing_crowned_profile(
            self: "RollerBearingCrownedProfile._Cast_RollerBearingCrownedProfile",
        ) -> "RollerBearingCrownedProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingCrownedProfile._Cast_RollerBearingCrownedProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingCrownedProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crown_end_drop(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CrownEndDrop

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @crown_end_drop.setter
    @enforce_parameter_types
    def crown_end_drop(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CrownEndDrop = value

    @property
    def crown_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CrownRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @crown_radius.setter
    @enforce_parameter_types
    def crown_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CrownRadius = value

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def parallel_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ParallelLength

        if temp is None:
            return 0.0

        return temp

    @parallel_length.setter
    @enforce_parameter_types
    def parallel_length(self: Self, value: "float"):
        self.wrapped.ParallelLength = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "RollerBearingCrownedProfile._Cast_RollerBearingCrownedProfile":
        return self._Cast_RollerBearingCrownedProfile(self)
