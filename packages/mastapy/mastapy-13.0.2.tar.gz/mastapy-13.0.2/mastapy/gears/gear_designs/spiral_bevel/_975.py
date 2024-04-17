"""SpiralBevelGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.gear_designs.bevel import _1188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.SpiralBevel", "SpiralBevelGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _973, _974
    from mastapy.gears.gear_designs.agma_gleason_conical import _1201
    from mastapy.gears.gear_designs.conical import _1162
    from mastapy.gears.gear_designs import _954, _952


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetDesign",)


Self = TypeVar("Self", bound="SpiralBevelGearSetDesign")


class SpiralBevelGearSetDesign(_1188.BevelGearSetDesign):
    """SpiralBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetDesign")

    class _Cast_SpiralBevelGearSetDesign:
        """Special nested class for casting SpiralBevelGearSetDesign to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
            parent: "SpiralBevelGearSetDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_design(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
        ) -> "_1188.BevelGearSetDesign":
            return self._parent._cast(_1188.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
        ) -> "_1201.AGMAGleasonConicalGearSetDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1201

            return self._parent._cast(_1201.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
        ) -> "_1162.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1162

            return self._parent._cast(_1162.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
        ) -> "_954.GearSetDesign":
            from mastapy.gears.gear_designs import _954

            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def spiral_bevel_gear_set_design(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign",
        ) -> "SpiralBevelGearSetDesign":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def gears(self: Self) -> "List[_973.SpiralBevelGearDesign]":
        """List[mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears(self: Self) -> "List[_973.SpiralBevelGearDesign]":
        """List[mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes(self: Self) -> "List[_974.SpiralBevelGearMeshDesign]":
        """List[mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign":
        return self._Cast_SpiralBevelGearSetDesign(self)
