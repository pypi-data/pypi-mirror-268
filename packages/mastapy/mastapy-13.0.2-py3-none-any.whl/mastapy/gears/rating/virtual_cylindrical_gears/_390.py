"""KlingelnbergVirtualCylindricalGearSet"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "KlingelnbergVirtualCylindricalGearSet",
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergVirtualCylindricalGearSet",)


Self = TypeVar("Self", bound="KlingelnbergVirtualCylindricalGearSet")


class KlingelnbergVirtualCylindricalGearSet(
    _395.VirtualCylindricalGearSet["_389.KlingelnbergVirtualCylindricalGear"]
):
    """KlingelnbergVirtualCylindricalGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR_SET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergVirtualCylindricalGearSet"
    )

    class _Cast_KlingelnbergVirtualCylindricalGearSet:
        """Special nested class for casting KlingelnbergVirtualCylindricalGearSet to subclasses."""

        def __init__(
            self: "KlingelnbergVirtualCylindricalGearSet._Cast_KlingelnbergVirtualCylindricalGearSet",
            parent: "KlingelnbergVirtualCylindricalGearSet",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_set(
            self: "KlingelnbergVirtualCylindricalGearSet._Cast_KlingelnbergVirtualCylindricalGearSet",
        ) -> "_395.VirtualCylindricalGearSet":
            return self._parent._cast(_395.VirtualCylindricalGearSet)

        @property
        def klingelnberg_virtual_cylindrical_gear_set(
            self: "KlingelnbergVirtualCylindricalGearSet._Cast_KlingelnbergVirtualCylindricalGearSet",
        ) -> "KlingelnbergVirtualCylindricalGearSet":
            return self._parent

        def __getattr__(
            self: "KlingelnbergVirtualCylindricalGearSet._Cast_KlingelnbergVirtualCylindricalGearSet",
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
        self: Self, instance_to_wrap: "KlingelnbergVirtualCylindricalGearSet.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_path_of_contact_of_virtual_cylindrical_gear_in_transverse_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LengthOfPathOfContactOfVirtualCylindricalGearInTransverseSection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_ratio_transverse_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_transmission_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualTransmissionRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergVirtualCylindricalGearSet._Cast_KlingelnbergVirtualCylindricalGearSet":
        return self._Cast_KlingelnbergVirtualCylindricalGearSet(self)
