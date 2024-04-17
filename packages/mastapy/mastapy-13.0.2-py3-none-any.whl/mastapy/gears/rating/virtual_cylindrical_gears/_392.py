"""VirtualCylindricalGearBasic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_BASIC = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears", "VirtualCylindricalGearBasic"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import (
        _381,
        _384,
        _387,
        _388,
        _389,
        _391,
        _393,
        _394,
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGearBasic",)


Self = TypeVar("Self", bound="VirtualCylindricalGearBasic")


class VirtualCylindricalGearBasic(_0.APIBase):
    """VirtualCylindricalGearBasic

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_BASIC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualCylindricalGearBasic")

    class _Cast_VirtualCylindricalGearBasic:
        """Special nested class for casting VirtualCylindricalGearBasic to subclasses."""

        def __init__(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
            parent: "VirtualCylindricalGearBasic",
        ):
            self._parent = parent

        @property
        def bevel_virtual_cylindrical_gear_iso10300_method_b2(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_381.BevelVirtualCylindricalGearISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _381

            return self._parent._cast(_381.BevelVirtualCylindricalGearISO10300MethodB2)

        @property
        def hypoid_virtual_cylindrical_gear_iso10300_method_b2(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_384.HypoidVirtualCylindricalGearISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _384

            return self._parent._cast(_384.HypoidVirtualCylindricalGearISO10300MethodB2)

        @property
        def klingelnberg_hypoid_virtual_cylindrical_gear(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_387.KlingelnbergHypoidVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _387

            return self._parent._cast(_387.KlingelnbergHypoidVirtualCylindricalGear)

        @property
        def klingelnberg_spiral_bevel_virtual_cylindrical_gear(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_388.KlingelnbergSpiralBevelVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _388

            return self._parent._cast(
                _388.KlingelnbergSpiralBevelVirtualCylindricalGear
            )

        @property
        def klingelnberg_virtual_cylindrical_gear(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_389.KlingelnbergVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _389

            return self._parent._cast(_389.KlingelnbergVirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_391.VirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _391

            return self._parent._cast(_391.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_iso10300_method_b1(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_393.VirtualCylindricalGearISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _393

            return self._parent._cast(_393.VirtualCylindricalGearISO10300MethodB1)

        @property
        def virtual_cylindrical_gear_iso10300_method_b2(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "_394.VirtualCylindricalGearISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _394

            return self._parent._cast(_394.VirtualCylindricalGearISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_basic(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
        ) -> "VirtualCylindricalGearBasic":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualCylindricalGearBasic.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle_at_base_circle_of_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleAtBaseCircleOfVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_of_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleOfVirtualCylindricalGears

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
    def normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_radius_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipRadiusOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic":
        return self._Cast_VirtualCylindricalGearBasic(self)
