"""CylindricalGearFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.system_model.part_model.gears import _2533, _2532
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.import_from_cad import _2511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "CylindricalGearFromCAD"
)

if TYPE_CHECKING:
    from mastapy.geometry.two_d import _315
    from mastapy.system_model.part_model.import_from_cad import (
        _2506,
        _2507,
        _2508,
        _2509,
        _2502,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFromCAD",)


Self = TypeVar("Self", bound="CylindricalGearFromCAD")


class CylindricalGearFromCAD(_2511.MountableComponentFromCAD):
    """CylindricalGearFromCAD

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFromCAD")

    class _Cast_CylindricalGearFromCAD:
        """Special nested class for casting CylindricalGearFromCAD to subclasses."""

        def __init__(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
            parent: "CylindricalGearFromCAD",
        ):
            self._parent = parent

        @property
        def mountable_component_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def cylindrical_gear_in_planetary_set_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "_2506.CylindricalGearInPlanetarySetFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2506

            return self._parent._cast(_2506.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "_2507.CylindricalPlanetGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2507

            return self._parent._cast(_2507.CylindricalPlanetGearFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "_2508.CylindricalRingGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2508

            return self._parent._cast(_2508.CylindricalRingGearFromCAD)

        @property
        def cylindrical_sun_gear_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "_2509.CylindricalSunGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2509

            return self._parent._cast(_2509.CylindricalSunGearFromCAD)

        @property
        def cylindrical_gear_from_cad(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD",
        ) -> "CylindricalGearFromCAD":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_drawing_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CADDrawingDiameter

        if temp is None:
            return 0.0

        return temp

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
    def existing_gear_set(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGearSet":
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.CylindricalGearSet]"""
        temp = self.wrapped.ExistingGearSet

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGearSet",
        )(temp)

    @existing_gear_set.setter
    @enforce_parameter_types
    def existing_gear_set(self: Self, value: "_2533.CylindricalGearSet"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ExistingGearSet = value

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def gear_set_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.GearSetName

        if temp is None:
            return ""

        return temp

    @gear_set_name.setter
    @enforce_parameter_types
    def gear_set_name(self: Self, value: "str"):
        self.wrapped.GearSetName = str(value) if value is not None else ""

    @property
    def helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    @enforce_parameter_types
    def helix_angle(self: Self, value: "float"):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def internal_external(self: Self) -> "_315.InternalExternalType":
        """mastapy.geometry.two_d.InternalExternalType"""
        temp = self.wrapped.InternalExternal

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Geometry.TwoD.InternalExternalType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.geometry.two_d._315", "InternalExternalType"
        )(value)

    @internal_external.setter
    @enforce_parameter_types
    def internal_external(self: Self, value: "_315.InternalExternalType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Geometry.TwoD.InternalExternalType"
        )
        self.wrapped.InternalExternal = value

    @property
    def meshing_gear(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGear":
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.CylindricalGear]"""
        temp = self.wrapped.MeshingGear

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGear",
        )(temp)

    @meshing_gear.setter
    @enforce_parameter_types
    def meshing_gear(self: Self, value: "_2532.CylindricalGear"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGear.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGear.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.MeshingGear = value

    @property
    def normal_module(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @normal_module.setter
    @enforce_parameter_types
    def normal_module(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NormalModule = value

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
    def number_of_teeth(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfTeeth = value

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
    def tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "CylindricalGearFromCAD._Cast_CylindricalGearFromCAD":
        return self._Cast_CylindricalGearFromCAD(self)
