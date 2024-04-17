"""SpiralBevelGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1187
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.SpiralBevel", "SpiralBevelGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _975, _973, _976
    from mastapy.gears.gear_designs.agma_gleason_conical import _1200
    from mastapy.gears.gear_designs.conical import _1161
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshDesign",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshDesign")


class SpiralBevelGearMeshDesign(_1187.BevelGearMeshDesign):
    """SpiralBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshDesign")

    class _Cast_SpiralBevelGearMeshDesign:
        """Special nested class for casting SpiralBevelGearMeshDesign to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
            parent: "SpiralBevelGearMeshDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
        ) -> "_1187.BevelGearMeshDesign":
            return self._parent._cast(_1187.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
        ) -> "_1200.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1200

            return self._parent._cast(_1200.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign",
        ) -> "SpiralBevelGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def wheel_inner_blade_angle_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_blade_angle_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def spiral_bevel_gear_set(self: Self) -> "_975.SpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def spiral_bevel_meshed_gears(
        self: Self,
    ) -> "List[_976.SpiralBevelMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.spiral_bevel.SpiralBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign":
        return self._Cast_SpiralBevelGearMeshDesign(self)
