"""VirtualCylindricalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears", "VirtualCylindricalGear"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _387, _388, _389, _393


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGear",)


Self = TypeVar("Self", bound="VirtualCylindricalGear")


class VirtualCylindricalGear(_392.VirtualCylindricalGearBasic):
    """VirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualCylindricalGear")

    class _Cast_VirtualCylindricalGear:
        """Special nested class for casting VirtualCylindricalGear to subclasses."""

        def __init__(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
            parent: "VirtualCylindricalGear",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_basic(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
        ) -> "_392.VirtualCylindricalGearBasic":
            return self._parent._cast(_392.VirtualCylindricalGearBasic)

        @property
        def klingelnberg_hypoid_virtual_cylindrical_gear(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
        ) -> "_387.KlingelnbergHypoidVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _387

            return self._parent._cast(_387.KlingelnbergHypoidVirtualCylindricalGear)

        @property
        def klingelnberg_spiral_bevel_virtual_cylindrical_gear(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
        ) -> "_388.KlingelnbergSpiralBevelVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _388

            return self._parent._cast(
                _388.KlingelnbergSpiralBevelVirtualCylindricalGear
            )

        @property
        def klingelnberg_virtual_cylindrical_gear(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
        ) -> "_389.KlingelnbergVirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _389

            return self._parent._cast(_389.KlingelnbergVirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_iso10300_method_b1(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
        ) -> "_393.VirtualCylindricalGearISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _393

            return self._parent._cast(_393.VirtualCylindricalGearISO10300MethodB1)

        @property
        def virtual_cylindrical_gear(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear",
        ) -> "VirtualCylindricalGear":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGear._Cast_VirtualCylindricalGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualCylindricalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_normal_for_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_transverse_for_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_of_addendum_normal_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioOfAddendumNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_of_addendum_transverse_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioOfAddendumTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectivePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def path_of_addendum_contact_normal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PathOfAddendumContactNormal

        if temp is None:
            return 0.0

        return temp

    @property
    def path_of_addendum_contact_transverse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PathOfAddendumContactTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "VirtualCylindricalGear._Cast_VirtualCylindricalGear":
        return self._Cast_VirtualCylindricalGear(self)
