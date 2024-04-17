"""StraightBevelGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1187
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _967, _965, _968
    from mastapy.gears.gear_designs.agma_gleason_conical import _1200
    from mastapy.gears.gear_designs.conical import _1161
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshDesign",)


Self = TypeVar("Self", bound="StraightBevelGearMeshDesign")


class StraightBevelGearMeshDesign(_1187.BevelGearMeshDesign):
    """StraightBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearMeshDesign")

    class _Cast_StraightBevelGearMeshDesign:
        """Special nested class for casting StraightBevelGearMeshDesign to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
            parent: "StraightBevelGearMeshDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_1187.BevelGearMeshDesign":
            return self._parent._cast(_1187.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_1200.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1200

            return self._parent._cast(_1200.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "StraightBevelGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self: Self) -> "_967.StraightBevelGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def straight_bevel_meshed_gears(
        self: Self,
    ) -> "List[_968.StraightBevelMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel.StraightBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign":
        return self._Cast_StraightBevelGearMeshDesign(self)
