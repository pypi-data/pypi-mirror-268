"""StraightBevelGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.gear_designs.bevel import _1188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _965, _966
    from mastapy.gears.gear_designs.agma_gleason_conical import _1201
    from mastapy.gears.gear_designs.conical import _1162
    from mastapy.gears.gear_designs import _954, _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetDesign",)


Self = TypeVar("Self", bound="StraightBevelGearSetDesign")


class StraightBevelGearSetDesign(_1188.BevelGearSetDesign):
    """StraightBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearSetDesign")

    class _Cast_StraightBevelGearSetDesign:
        """Special nested class for casting StraightBevelGearSetDesign to subclasses."""

        def __init__(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
            parent: "StraightBevelGearSetDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_design(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
        ) -> "_1188.BevelGearSetDesign":
            return self._parent._cast(_1188.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
        ) -> "_1201.AGMAGleasonConicalGearSetDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1201

            return self._parent._cast(_1201.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
        ) -> "_1162.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1162

            return self._parent._cast(_1162.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
        ) -> "_954.GearSetDesign":
            from mastapy.gears.gear_designs import _954

            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_gear_set_design(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
        ) -> "StraightBevelGearSetDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self: Self) -> "List[_965.StraightBevelGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel.StraightBevelGearDesign]

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
    def straight_bevel_gears(self: Self) -> "List[_965.StraightBevelGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel.StraightBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes(self: Self) -> "List[_966.StraightBevelGearMeshDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel.StraightBevelGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign":
        return self._Cast_StraightBevelGearSetDesign(self)
