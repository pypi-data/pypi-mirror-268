"""StraightBevelDiffGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.gears.gear_designs.bevel import _1188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff", "StraightBevelDiffGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _969, _970
    from mastapy.gears.gear_designs.agma_gleason_conical import _1201
    from mastapy.gears.gear_designs.conical import _1162
    from mastapy.gears.gear_designs import _954, _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetDesign",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetDesign")


class StraightBevelDiffGearSetDesign(_1188.BevelGearSetDesign):
    """StraightBevelDiffGearSetDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSetDesign")

    class _Cast_StraightBevelDiffGearSetDesign:
        """Special nested class for casting StraightBevelDiffGearSetDesign to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
            parent: "StraightBevelDiffGearSetDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_design(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
        ) -> "_1188.BevelGearSetDesign":
            return self._parent._cast(_1188.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
        ) -> "_1201.AGMAGleasonConicalGearSetDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1201

            return self._parent._cast(_1201.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
        ) -> "_1162.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1162

            return self._parent._cast(_1162.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
        ) -> "_954.GearSetDesign":
            from mastapy.gears.gear_designs import _954

            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
        ) -> "StraightBevelDiffGearSetDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def derating_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeratingFactor

        if temp is None:
            return 0.0

        return temp

    @derating_factor.setter
    @enforce_parameter_types
    def derating_factor(self: Self, value: "float"):
        self.wrapped.DeratingFactor = float(value) if value is not None else 0.0

    @property
    def gears(self: Self) -> "List[_969.StraightBevelDiffGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearDesign]

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
    def straight_bevel_diff_meshes(
        self: Self,
    ) -> "List[_970.StraightBevelDiffGearMeshDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetDesign._Cast_StraightBevelDiffGearSetDesign":
        return self._Cast_StraightBevelDiffGearSetDesign(self)
