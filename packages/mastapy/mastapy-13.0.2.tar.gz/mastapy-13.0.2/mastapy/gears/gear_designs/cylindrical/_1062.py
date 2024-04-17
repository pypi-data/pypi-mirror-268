"""LinearBacklashSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_BACKLASH_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "LinearBacklashSpecification"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1044


__docformat__ = "restructuredtext en"
__all__ = ("LinearBacklashSpecification",)


Self = TypeVar("Self", bound="LinearBacklashSpecification")


class LinearBacklashSpecification(_0.APIBase):
    """LinearBacklashSpecification

    This is a mastapy class.
    """

    TYPE = _LINEAR_BACKLASH_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearBacklashSpecification")

    class _Cast_LinearBacklashSpecification:
        """Special nested class for casting LinearBacklashSpecification to subclasses."""

        def __init__(
            self: "LinearBacklashSpecification._Cast_LinearBacklashSpecification",
            parent: "LinearBacklashSpecification",
        ):
            self._parent = parent

        @property
        def linear_backlash_specification(
            self: "LinearBacklashSpecification._Cast_LinearBacklashSpecification",
        ) -> "LinearBacklashSpecification":
            return self._parent

        def __getattr__(
            self: "LinearBacklashSpecification._Cast_LinearBacklashSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearBacklashSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankName

        if temp is None:
            return ""

        return temp

    @property
    def circumferential_backlash_pitch_circle(
        self: Self,
    ) -> "_1044.CylindricalMeshLinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshLinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircumferentialBacklashPitchCircle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def circumferential_backlash_reference_circle(
        self: Self,
    ) -> "_1044.CylindricalMeshLinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshLinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircumferentialBacklashReferenceCircle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def normal_backlash(
        self: Self,
    ) -> "_1044.CylindricalMeshLinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshLinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalBacklash

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def radial_backlash(
        self: Self,
    ) -> "_1044.CylindricalMeshLinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshLinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialBacklash

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_backlash(
        self: Self,
    ) -> "List[_1044.CylindricalMeshLinearBacklashSpecification]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalMeshLinearBacklashSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearBacklash

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LinearBacklashSpecification._Cast_LinearBacklashSpecification":
        return self._Cast_LinearBacklashSpecification(self)
