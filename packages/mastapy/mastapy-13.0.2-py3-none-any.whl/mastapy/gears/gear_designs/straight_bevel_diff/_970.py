"""StraightBevelDiffGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1187
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff",
    "StraightBevelDiffGearMeshDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _971, _969, _972
    from mastapy.gears.gear_designs.agma_gleason_conical import _1200
    from mastapy.gears.gear_designs.conical import _1161
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshDesign",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshDesign")


class StraightBevelDiffGearMeshDesign(_1187.BevelGearMeshDesign):
    """StraightBevelDiffGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearMeshDesign")

    class _Cast_StraightBevelDiffGearMeshDesign:
        """Special nested class for casting StraightBevelDiffGearMeshDesign to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
            parent: "StraightBevelDiffGearMeshDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
        ) -> "_1187.BevelGearMeshDesign":
            return self._parent._cast(_1187.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
        ) -> "_1200.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1200

            return self._parent._cast(_1200.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
        ) -> "StraightBevelDiffGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_performance_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionPerformanceTorque

        if temp is None:
            return 0.0

        return temp

    @pinion_performance_torque.setter
    @enforce_parameter_types
    def pinion_performance_torque(self: Self, value: "float"):
        self.wrapped.PinionPerformanceTorque = (
            float(value) if value is not None else 0.0
        )

    @property
    def straight_bevel_diff_gear_set(
        self: Self,
    ) -> "_971.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears(
        self: Self,
    ) -> "List[_969.StraightBevelDiffGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshed_gears(
        self: Self,
    ) -> "List[_972.StraightBevelDiffMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign":
        return self._Cast_StraightBevelDiffGearMeshDesign(self)
