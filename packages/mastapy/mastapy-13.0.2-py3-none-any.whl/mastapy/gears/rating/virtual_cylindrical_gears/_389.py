"""KlingelnbergVirtualCylindricalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "KlingelnbergVirtualCylindricalGear",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _387, _388, _392


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergVirtualCylindricalGear",)


Self = TypeVar("Self", bound="KlingelnbergVirtualCylindricalGear")


class KlingelnbergVirtualCylindricalGear(_391.VirtualCylindricalGear):
    """KlingelnbergVirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergVirtualCylindricalGear")

    class _Cast_KlingelnbergVirtualCylindricalGear:
        """Special nested class for casting KlingelnbergVirtualCylindricalGear to subclasses."""

        def __init__(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
            parent: "KlingelnbergVirtualCylindricalGear",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
        ) -> "_391.VirtualCylindricalGear":
            return self._parent._cast(_391.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
        ) -> "_392.VirtualCylindricalGearBasic":
            from mastapy.gears.rating.virtual_cylindrical_gears import _392

            return self._parent._cast(_392.VirtualCylindricalGearBasic)

        @property
        def klingelnberg_hypoid_virtual_cylindrical_gear(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
        ) -> "_387.KlingelnbergHypoidVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _387

            return self._parent._cast(_387.KlingelnbergHypoidVirtualCylindricalGear)

        @property
        def klingelnberg_spiral_bevel_virtual_cylindrical_gear(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
        ) -> "_388.KlingelnbergSpiralBevelVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _388

            return self._parent._cast(
                _388.KlingelnbergSpiralBevelVirtualCylindricalGear
            )

        @property
        def klingelnberg_virtual_cylindrical_gear(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
        ) -> "KlingelnbergVirtualCylindricalGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear",
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
        self: Self, instance_to_wrap: "KlingelnbergVirtualCylindricalGear.TYPE"
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
    def face_contact_ratio_transverse_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def outside_diameter_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutsideDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_number_of_teeth_normal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualNumberOfTeethNormal

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_number_of_teeth_transverse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualNumberOfTeethTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear":
        return self._Cast_KlingelnbergVirtualCylindricalGear(self)
