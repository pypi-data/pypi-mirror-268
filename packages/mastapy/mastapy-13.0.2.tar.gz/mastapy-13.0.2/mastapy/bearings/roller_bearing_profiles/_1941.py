"""RollerBearingJohnsGoharProfile"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.roller_bearing_profiles import _1943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_JOHNS_GOHAR_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingJohnsGoharProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingJohnsGoharProfile",)


Self = TypeVar("Self", bound="RollerBearingJohnsGoharProfile")


class RollerBearingJohnsGoharProfile(_1943.RollerBearingProfile):
    """RollerBearingJohnsGoharProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_JOHNS_GOHAR_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingJohnsGoharProfile")

    class _Cast_RollerBearingJohnsGoharProfile:
        """Special nested class for casting RollerBearingJohnsGoharProfile to subclasses."""

        def __init__(
            self: "RollerBearingJohnsGoharProfile._Cast_RollerBearingJohnsGoharProfile",
            parent: "RollerBearingJohnsGoharProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_profile(
            self: "RollerBearingJohnsGoharProfile._Cast_RollerBearingJohnsGoharProfile",
        ) -> "_1943.RollerBearingProfile":
            return self._parent._cast(_1943.RollerBearingProfile)

        @property
        def roller_bearing_johns_gohar_profile(
            self: "RollerBearingJohnsGoharProfile._Cast_RollerBearingJohnsGoharProfile",
        ) -> "RollerBearingJohnsGoharProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingJohnsGoharProfile._Cast_RollerBearingJohnsGoharProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingJohnsGoharProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_load(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DesignLoad

        if temp is None:
            return 0.0

        return temp

    @design_load.setter
    @enforce_parameter_types
    def design_load(self: Self, value: "float"):
        self.wrapped.DesignLoad = float(value) if value is not None else 0.0

    @property
    def end_drop(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EndDrop

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @end_drop.setter
    @enforce_parameter_types
    def end_drop(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EndDrop = value

    @property
    def length_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LengthFactor

        if temp is None:
            return 0.0

        return temp

    @length_factor.setter
    @enforce_parameter_types
    def length_factor(self: Self, value: "float"):
        self.wrapped.LengthFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "RollerBearingJohnsGoharProfile._Cast_RollerBearingJohnsGoharProfile":
        return self._Cast_RollerBearingJohnsGoharProfile(self)
