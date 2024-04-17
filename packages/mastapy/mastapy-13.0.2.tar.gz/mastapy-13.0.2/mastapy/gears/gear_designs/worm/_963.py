"""WormGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Worm", "WormGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _354
    from mastapy.gears.gear_designs.worm import _961, _962
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetDesign",)


Self = TypeVar("Self", bound="WormGearSetDesign")


class WormGearSetDesign(_954.GearSetDesign):
    """WormGearSetDesign

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetDesign")

    class _Cast_WormGearSetDesign:
        """Special nested class for casting WormGearSetDesign to subclasses."""

        def __init__(
            self: "WormGearSetDesign._Cast_WormGearSetDesign",
            parent: "WormGearSetDesign",
        ):
            self._parent = parent

        @property
        def gear_set_design(
            self: "WormGearSetDesign._Cast_WormGearSetDesign",
        ) -> "_954.GearSetDesign":
            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "WormGearSetDesign._Cast_WormGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def worm_gear_set_design(
            self: "WormGearSetDesign._Cast_WormGearSetDesign",
        ) -> "WormGearSetDesign":
            return self._parent

        def __getattr__(self: "WormGearSetDesign._Cast_WormGearSetDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialModule

        if temp is None:
            return 0.0

        return temp

    @axial_module.setter
    @enforce_parameter_types
    def axial_module(self: Self, value: "float"):
        self.wrapped.AxialModule = float(value) if value is not None else 0.0

    @property
    def axial_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialPressureAngle

        if temp is None:
            return 0.0

        return temp

    @axial_pressure_angle.setter
    @enforce_parameter_types
    def axial_pressure_angle(self: Self, value: "float"):
        self.wrapped.AxialPressureAngle = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_pressure_angle(self: Self, value: "float"):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def worm_type(self: Self) -> "_354.WormType":
        """mastapy.gears.WormType"""
        temp = self.wrapped.WormType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.WormType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._354", "WormType")(value)

    @worm_type.setter
    @enforce_parameter_types
    def worm_type(self: Self, value: "_354.WormType"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.WormType")
        self.wrapped.WormType = value

    @property
    def gears(self: Self) -> "List[_961.WormGearDesign]":
        """List[mastapy.gears.gear_designs.worm.WormGearDesign]

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
    def worm_gears(self: Self) -> "List[_961.WormGearDesign]":
        """List[mastapy.gears.gear_designs.worm.WormGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes(self: Self) -> "List[_962.WormGearMeshDesign]":
        """List[mastapy.gears.gear_designs.worm.WormGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "WormGearSetDesign._Cast_WormGearSetDesign":
        return self._Cast_WormGearSetDesign(self)
