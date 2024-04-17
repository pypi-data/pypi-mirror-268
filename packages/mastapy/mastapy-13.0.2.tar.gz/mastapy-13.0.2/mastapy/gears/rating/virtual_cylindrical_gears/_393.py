"""VirtualCylindricalGearISO10300MethodB1"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B1 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "VirtualCylindricalGearISO10300MethodB1",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _392


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGearISO10300MethodB1",)


Self = TypeVar("Self", bound="VirtualCylindricalGearISO10300MethodB1")


class VirtualCylindricalGearISO10300MethodB1(_391.VirtualCylindricalGear):
    """VirtualCylindricalGearISO10300MethodB1

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B1
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualCylindricalGearISO10300MethodB1"
    )

    class _Cast_VirtualCylindricalGearISO10300MethodB1:
        """Special nested class for casting VirtualCylindricalGearISO10300MethodB1 to subclasses."""

        def __init__(
            self: "VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1",
            parent: "VirtualCylindricalGearISO10300MethodB1",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear(
            self: "VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1",
        ) -> "_391.VirtualCylindricalGear":
            return self._parent._cast(_391.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(
            self: "VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1",
        ) -> "_392.VirtualCylindricalGearBasic":
            from mastapy.gears.rating.virtual_cylindrical_gears import _392

            return self._parent._cast(_392.VirtualCylindricalGearBasic)

        @property
        def virtual_cylindrical_gear_iso10300_method_b1(
            self: "VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1",
        ) -> "VirtualCylindricalGearISO10300MethodB1":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1",
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
        self: Self, instance_to_wrap: "VirtualCylindricalGearISO10300MethodB1.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter_of_virtual_cylindrical_gear_in_normal_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameterOfVirtualCylindricalGearInNormalSection

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
    def reference_diameter_in_normal_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameterInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter_of_virtual_cylindrical_gear_in_normal_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameterOfVirtualCylindricalGearInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseModule

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
    def virtual_spur_gear_number_of_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualSpurGearNumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1":
        return self._Cast_VirtualCylindricalGearISO10300MethodB1(self)
