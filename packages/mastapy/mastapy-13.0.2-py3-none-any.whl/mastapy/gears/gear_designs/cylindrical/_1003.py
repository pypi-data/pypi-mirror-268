"""BacklashSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1073
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BACKLASH_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "BacklashSpecification"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1062, _1041


__docformat__ = "restructuredtext en"
__all__ = ("BacklashSpecification",)


Self = TypeVar("Self", bound="BacklashSpecification")


class BacklashSpecification(_1073.RelativeValuesSpecification["BacklashSpecification"]):
    """BacklashSpecification

    This is a mastapy class.
    """

    TYPE = _BACKLASH_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BacklashSpecification")

    class _Cast_BacklashSpecification:
        """Special nested class for casting BacklashSpecification to subclasses."""

        def __init__(
            self: "BacklashSpecification._Cast_BacklashSpecification",
            parent: "BacklashSpecification",
        ):
            self._parent = parent

        @property
        def relative_values_specification(
            self: "BacklashSpecification._Cast_BacklashSpecification",
        ) -> "_1073.RelativeValuesSpecification":
            pass

            return self._parent._cast(_1073.RelativeValuesSpecification)

        @property
        def backlash_specification(
            self: "BacklashSpecification._Cast_BacklashSpecification",
        ) -> "BacklashSpecification":
            return self._parent

        def __getattr__(
            self: "BacklashSpecification._Cast_BacklashSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BacklashSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank(self: Self) -> "_1062.LinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.LinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1062.LinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.LinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def angular_backlash(self: Self) -> "List[_1041.CylindricalMeshAngularBacklash]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalMeshAngularBacklash]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularBacklash

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flanks(self: Self) -> "List[_1062.LinearBacklashSpecification]":
        """List[mastapy.gears.gear_designs.cylindrical.LinearBacklashSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def both_flanks(self: Self) -> "_1062.LinearBacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.LinearBacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BacklashSpecification._Cast_BacklashSpecification":
        return self._Cast_BacklashSpecification(self)
