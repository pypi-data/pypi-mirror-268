"""CrossedAxisCylindricalGearPairLineContact"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical import _1007
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR_LINE_CONTACT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CrossedAxisCylindricalGearPairLineContact",
)


__docformat__ = "restructuredtext en"
__all__ = ("CrossedAxisCylindricalGearPairLineContact",)


Self = TypeVar("Self", bound="CrossedAxisCylindricalGearPairLineContact")


class CrossedAxisCylindricalGearPairLineContact(_1007.CrossedAxisCylindricalGearPair):
    """CrossedAxisCylindricalGearPairLineContact

    This is a mastapy class.
    """

    TYPE = _CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR_LINE_CONTACT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CrossedAxisCylindricalGearPairLineContact"
    )

    class _Cast_CrossedAxisCylindricalGearPairLineContact:
        """Special nested class for casting CrossedAxisCylindricalGearPairLineContact to subclasses."""

        def __init__(
            self: "CrossedAxisCylindricalGearPairLineContact._Cast_CrossedAxisCylindricalGearPairLineContact",
            parent: "CrossedAxisCylindricalGearPairLineContact",
        ):
            self._parent = parent

        @property
        def crossed_axis_cylindrical_gear_pair(
            self: "CrossedAxisCylindricalGearPairLineContact._Cast_CrossedAxisCylindricalGearPairLineContact",
        ) -> "_1007.CrossedAxisCylindricalGearPair":
            return self._parent._cast(_1007.CrossedAxisCylindricalGearPair)

        @property
        def crossed_axis_cylindrical_gear_pair_line_contact(
            self: "CrossedAxisCylindricalGearPairLineContact._Cast_CrossedAxisCylindricalGearPairLineContact",
        ) -> "CrossedAxisCylindricalGearPairLineContact":
            return self._parent

        def __getattr__(
            self: "CrossedAxisCylindricalGearPairLineContact._Cast_CrossedAxisCylindricalGearPairLineContact",
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
        self: Self, instance_to_wrap: "CrossedAxisCylindricalGearPairLineContact.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CrossedAxisCylindricalGearPairLineContact._Cast_CrossedAxisCylindricalGearPairLineContact":
        return self._Cast_CrossedAxisCylindricalGearPairLineContact(self)
