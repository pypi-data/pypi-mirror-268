"""WormGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Worm", "WormGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _964, _960, _963, _961
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshDesign",)


Self = TypeVar("Self", bound="WormGearMeshDesign")


class WormGearMeshDesign(_953.GearMeshDesign):
    """WormGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshDesign")

    class _Cast_WormGearMeshDesign:
        """Special nested class for casting WormGearMeshDesign to subclasses."""

        def __init__(
            self: "WormGearMeshDesign._Cast_WormGearMeshDesign",
            parent: "WormGearMeshDesign",
        ):
            self._parent = parent

        @property
        def gear_mesh_design(
            self: "WormGearMeshDesign._Cast_WormGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "WormGearMeshDesign._Cast_WormGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def worm_gear_mesh_design(
            self: "WormGearMeshDesign._Cast_WormGearMeshDesign",
        ) -> "WormGearMeshDesign":
            return self._parent

        def __getattr__(self: "WormGearMeshDesign._Cast_WormGearMeshDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    @enforce_parameter_types
    def centre_distance(self: Self, value: "float"):
        self.wrapped.CentreDistance = float(value) if value is not None else 0.0

    @property
    def coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_friction.setter
    @enforce_parameter_types
    def coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.CoefficientOfFriction = float(value) if value is not None else 0.0

    @property
    def meshing_friction_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeshingFrictionAngle

        if temp is None:
            return 0.0

        return temp

    @meshing_friction_angle.setter
    @enforce_parameter_types
    def meshing_friction_angle(self: Self, value: "float"):
        self.wrapped.MeshingFrictionAngle = float(value) if value is not None else 0.0

    @property
    def shaft_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def standard_centre_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StandardCentreDistance

        if temp is None:
            return 0.0

        return temp

    @standard_centre_distance.setter
    @enforce_parameter_types
    def standard_centre_distance(self: Self, value: "float"):
        self.wrapped.StandardCentreDistance = float(value) if value is not None else 0.0

    @property
    def wheel_addendum_modification_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelAddendumModificationFactor

        if temp is None:
            return 0.0

        return temp

    @wheel_addendum_modification_factor.setter
    @enforce_parameter_types
    def wheel_addendum_modification_factor(self: Self, value: "float"):
        self.wrapped.WheelAddendumModificationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel(self: Self) -> "_964.WormWheelDesign":
        """mastapy.gears.gear_designs.worm.WormWheelDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Wheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm(self: Self) -> "_960.WormDesign":
        """mastapy.gears.gear_designs.worm.WormDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Worm

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_set(self: Self) -> "_963.WormGearSetDesign":
        """mastapy.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "WormGearMeshDesign._Cast_WormGearMeshDesign":
        return self._Cast_WormGearMeshDesign(self)
