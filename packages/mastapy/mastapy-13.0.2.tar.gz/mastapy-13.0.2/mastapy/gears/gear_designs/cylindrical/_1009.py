"""CrossedAxisCylindricalGearPairPointContact"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical import _1007
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR_POINT_CONTACT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CrossedAxisCylindricalGearPairPointContact",
)


__docformat__ = "restructuredtext en"
__all__ = ("CrossedAxisCylindricalGearPairPointContact",)


Self = TypeVar("Self", bound="CrossedAxisCylindricalGearPairPointContact")


class CrossedAxisCylindricalGearPairPointContact(_1007.CrossedAxisCylindricalGearPair):
    """CrossedAxisCylindricalGearPairPointContact

    This is a mastapy class.
    """

    TYPE = _CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR_POINT_CONTACT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CrossedAxisCylindricalGearPairPointContact"
    )

    class _Cast_CrossedAxisCylindricalGearPairPointContact:
        """Special nested class for casting CrossedAxisCylindricalGearPairPointContact to subclasses."""

        def __init__(
            self: "CrossedAxisCylindricalGearPairPointContact._Cast_CrossedAxisCylindricalGearPairPointContact",
            parent: "CrossedAxisCylindricalGearPairPointContact",
        ):
            self._parent = parent

        @property
        def crossed_axis_cylindrical_gear_pair(
            self: "CrossedAxisCylindricalGearPairPointContact._Cast_CrossedAxisCylindricalGearPairPointContact",
        ) -> "_1007.CrossedAxisCylindricalGearPair":
            return self._parent._cast(_1007.CrossedAxisCylindricalGearPair)

        @property
        def crossed_axis_cylindrical_gear_pair_point_contact(
            self: "CrossedAxisCylindricalGearPairPointContact._Cast_CrossedAxisCylindricalGearPairPointContact",
        ) -> "CrossedAxisCylindricalGearPairPointContact":
            return self._parent

        def __getattr__(
            self: "CrossedAxisCylindricalGearPairPointContact._Cast_CrossedAxisCylindricalGearPairPointContact",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CrossedAxisCylindricalGearPairPointContact.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CrossedAxisCylindricalGearPairPointContact._Cast_CrossedAxisCylindricalGearPairPointContact":
        return self._Cast_CrossedAxisCylindricalGearPairPointContact(self)
