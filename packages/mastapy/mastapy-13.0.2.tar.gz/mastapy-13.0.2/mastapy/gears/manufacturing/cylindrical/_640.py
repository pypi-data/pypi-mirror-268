"""ProfileModificationSegment"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical import _639
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_MODIFICATION_SEGMENT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "ProfileModificationSegment"
)


__docformat__ = "restructuredtext en"
__all__ = ("ProfileModificationSegment",)


Self = TypeVar("Self", bound="ProfileModificationSegment")


class ProfileModificationSegment(_639.ModificationSegment):
    """ProfileModificationSegment

    This is a mastapy class.
    """

    TYPE = _PROFILE_MODIFICATION_SEGMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileModificationSegment")

    class _Cast_ProfileModificationSegment:
        """Special nested class for casting ProfileModificationSegment to subclasses."""

        def __init__(
            self: "ProfileModificationSegment._Cast_ProfileModificationSegment",
            parent: "ProfileModificationSegment",
        ):
            self._parent = parent

        @property
        def modification_segment(
            self: "ProfileModificationSegment._Cast_ProfileModificationSegment",
        ) -> "_639.ModificationSegment":
            return self._parent._cast(_639.ModificationSegment)

        @property
        def profile_modification_segment(
            self: "ProfileModificationSegment._Cast_ProfileModificationSegment",
        ) -> "ProfileModificationSegment":
            return self._parent

        def __getattr__(
            self: "ProfileModificationSegment._Cast_ProfileModificationSegment",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileModificationSegment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "float"):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

    @property
    def roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollAngle

        if temp is None:
            return 0.0

        return temp

    @roll_angle.setter
    @enforce_parameter_types
    def roll_angle(self: Self, value: "float"):
        self.wrapped.RollAngle = float(value) if value is not None else 0.0

    @property
    def roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollDistance

        if temp is None:
            return 0.0

        return temp

    @roll_distance.setter
    @enforce_parameter_types
    def roll_distance(self: Self, value: "float"):
        self.wrapped.RollDistance = float(value) if value is not None else 0.0

    @property
    def use_iso217712007_slope_sign_convention(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseISO217712007SlopeSignConvention

        if temp is None:
            return False

        return temp

    @use_iso217712007_slope_sign_convention.setter
    @enforce_parameter_types
    def use_iso217712007_slope_sign_convention(self: Self, value: "bool"):
        self.wrapped.UseISO217712007SlopeSignConvention = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileModificationSegment._Cast_ProfileModificationSegment":
        return self._Cast_ProfileModificationSegment(self)
