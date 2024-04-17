"""WormGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Worm", "WormGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.gears.gear_designs.worm import _960, _964
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("WormGearDesign",)


Self = TypeVar("Self", bound="WormGearDesign")


class WormGearDesign(_951.GearDesign):
    """WormGearDesign

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearDesign")

    class _Cast_WormGearDesign:
        """Special nested class for casting WormGearDesign to subclasses."""

        def __init__(
            self: "WormGearDesign._Cast_WormGearDesign", parent: "WormGearDesign"
        ):
            self._parent = parent

        @property
        def gear_design(
            self: "WormGearDesign._Cast_WormGearDesign",
        ) -> "_951.GearDesign":
            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "WormGearDesign._Cast_WormGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def worm_design(
            self: "WormGearDesign._Cast_WormGearDesign",
        ) -> "_960.WormDesign":
            from mastapy.gears.gear_designs.worm import _960

            return self._parent._cast(_960.WormDesign)

        @property
        def worm_wheel_design(
            self: "WormGearDesign._Cast_WormGearDesign",
        ) -> "_964.WormWheelDesign":
            from mastapy.gears.gear_designs.worm import _964

            return self._parent._cast(_964.WormWheelDesign)

        @property
        def worm_gear_design(
            self: "WormGearDesign._Cast_WormGearDesign",
        ) -> "WormGearDesign":
            return self._parent

        def __getattr__(self: "WormGearDesign._Cast_WormGearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self: Self) -> "_336.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._336", "Hand")(value)

    @hand.setter
    @enforce_parameter_types
    def hand(self: Self, value: "_336.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "WormGearDesign._Cast_WormGearDesign":
        return self._Cast_WormGearDesign(self)
