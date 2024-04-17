"""FaceGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _1000, _1001, _998, _993, _995
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetDesign",)


Self = TypeVar("Self", bound="FaceGearSetDesign")


class FaceGearSetDesign(_954.GearSetDesign):
    """FaceGearSetDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetDesign")

    class _Cast_FaceGearSetDesign:
        """Special nested class for casting FaceGearSetDesign to subclasses."""

        def __init__(
            self: "FaceGearSetDesign._Cast_FaceGearSetDesign",
            parent: "FaceGearSetDesign",
        ):
            self._parent = parent

        @property
        def gear_set_design(
            self: "FaceGearSetDesign._Cast_FaceGearSetDesign",
        ) -> "_954.GearSetDesign":
            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "FaceGearSetDesign._Cast_FaceGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def face_gear_set_design(
            self: "FaceGearSetDesign._Cast_FaceGearSetDesign",
        ) -> "FaceGearSetDesign":
            return self._parent

        def __getattr__(self: "FaceGearSetDesign._Cast_FaceGearSetDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    @enforce_parameter_types
    def module(self: Self, value: "float"):
        self.wrapped.Module = float(value) if value is not None else 0.0

    @property
    def nominal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NominalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @nominal_pressure_angle.setter
    @enforce_parameter_types
    def nominal_pressure_angle(self: Self, value: "float"):
        self.wrapped.NominalPressureAngle = float(value) if value is not None else 0.0

    @property
    def normal_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @shaft_angle.setter
    @enforce_parameter_types
    def shaft_angle(self: Self, value: "float"):
        self.wrapped.ShaftAngle = float(value) if value is not None else 0.0

    @property
    def working_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cylindrical_gear_set_micro_geometry(
        self: Self,
    ) -> "_1000.FaceGearSetMicroGeometry":
        """mastapy.gears.gear_designs.face.FaceGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gear(self: Self) -> "_1001.FaceGearWheelDesign":
        """mastapy.gears.gear_designs.face.FaceGearWheelDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion(self: Self) -> "_998.FaceGearPinionDesign":
        """mastapy.gears.gear_designs.face.FaceGearPinionDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Pinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_993.FaceGearDesign]":
        """List[mastapy.gears.gear_designs.face.FaceGearDesign]

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
    def face_gears(self: Self) -> "List[_993.FaceGearDesign]":
        """List[mastapy.gears.gear_designs.face.FaceGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes(self: Self) -> "List[_995.FaceGearMeshDesign]":
        """List[mastapy.gears.gear_designs.face.FaceGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSetDesign._Cast_FaceGearSetDesign":
        return self._Cast_FaceGearSetDesign(self)
