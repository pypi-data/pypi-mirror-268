"""CylindricalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy.gears import _325
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import overridable_enum_runtime, conversion, constructor
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model.gears import _2539
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1032
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2570
    from mastapy.system_model.part_model.gears import _2532, _2549
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSet",)


Self = TypeVar("Self", bound="CylindricalGearSet")


class CylindricalGearSet(_2539.GearSet):
    """CylindricalGearSet

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSet")

    class _Cast_CylindricalGearSet:
        """Special nested class for casting CylindricalGearSet to subclasses."""

        def __init__(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
            parent: "CylindricalGearSet",
        ):
            self._parent = parent

        @property
        def gear_set(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
        ) -> "_2539.GearSet":
            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "CylindricalGearSet._Cast_CylindricalGearSet") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def planetary_gear_set(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
        ) -> "_2549.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.PlanetaryGearSet)

        @property
        def cylindrical_gear_set(
            self: "CylindricalGearSet._Cast_CylindricalGearSet",
        ) -> "CylindricalGearSet":
            return self._parent

        def __getattr__(self: "CylindricalGearSet._Cast_CylindricalGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_requirement(
        self: Self,
    ) -> "overridable.Overridable_ContactRatioRequirements":
        """Overridable[mastapy.gears.ContactRatioRequirements]"""
        temp = self.wrapped.AxialContactRatioRequirement

        if temp is None:
            return None

        value = overridable.Overridable_ContactRatioRequirements.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @axial_contact_ratio_requirement.setter
    @enforce_parameter_types
    def axial_contact_ratio_requirement(
        self: Self,
        value: "Union[_325.ContactRatioRequirements, Tuple[_325.ContactRatioRequirements, bool]]",
    ):
        wrapper_type = overridable.Overridable_ContactRatioRequirements.wrapper_type()
        enclosed_type = overridable.Overridable_ContactRatioRequirements.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def is_supercharger_rotor_set(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsSuperchargerRotorSet

        if temp is None:
            return False

        return temp

    @is_supercharger_rotor_set.setter
    @enforce_parameter_types
    def is_supercharger_rotor_set(self: Self, value: "bool"):
        self.wrapped.IsSuperchargerRotorSet = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_acceptable_axial_contact_ratio(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_acceptable_axial_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_axial_contact_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumAcceptableAxialContactRatio = value

    @property
    def maximum_acceptable_transverse_contact_ratio(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_transverse_contact_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumAcceptableTransverseContactRatio = value

    @property
    def maximum_face_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumFaceWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_face_width.setter
    @enforce_parameter_types
    def maximum_face_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumFaceWidth = value

    @property
    def maximum_helix_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_helix_angle.setter
    @enforce_parameter_types
    def maximum_helix_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumHelixAngle = value

    @property
    def maximum_normal_module(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_normal_module.setter
    @enforce_parameter_types
    def maximum_normal_module(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumNormalModule = value

    @property
    def maximum_normal_pressure_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_normal_pressure_angle.setter
    @enforce_parameter_types
    def maximum_normal_pressure_angle(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumNormalPressureAngle = value

    @property
    def minimum_acceptable_axial_contact_ratio(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_acceptable_axial_contact_ratio.setter
    @enforce_parameter_types
    def minimum_acceptable_axial_contact_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumAcceptableAxialContactRatio = value

    @property
    def minimum_acceptable_transverse_contact_ratio(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def minimum_acceptable_transverse_contact_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumAcceptableTransverseContactRatio = value

    @property
    def minimum_face_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumFaceWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_face_width.setter
    @enforce_parameter_types
    def minimum_face_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumFaceWidth = value

    @property
    def minimum_helix_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_helix_angle.setter
    @enforce_parameter_types
    def minimum_helix_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumHelixAngle = value

    @property
    def minimum_normal_module(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_normal_module.setter
    @enforce_parameter_types
    def minimum_normal_module(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumNormalModule = value

    @property
    def minimum_normal_pressure_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_normal_pressure_angle.setter
    @enforce_parameter_types
    def minimum_normal_pressure_angle(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumNormalPressureAngle = value

    @property
    def opposite_hand(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OppositeHand

        if temp is None:
            return False

        return temp

    @opposite_hand.setter
    @enforce_parameter_types
    def opposite_hand(self: Self, value: "bool"):
        self.wrapped.OppositeHand = bool(value) if value is not None else False

    @property
    def supercharger_rotor_set_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.SuperchargerRotorSetDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @supercharger_rotor_set_database.setter
    @enforce_parameter_types
    def supercharger_rotor_set_database(self: Self, value: "str"):
        self.wrapped.SuperchargerRotorSetDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def transverse_contact_ratio_requirement(
        self: Self,
    ) -> "overridable.Overridable_ContactRatioRequirements":
        """Overridable[mastapy.gears.ContactRatioRequirements]"""
        temp = self.wrapped.TransverseContactRatioRequirement

        if temp is None:
            return None

        value = overridable.Overridable_ContactRatioRequirements.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @transverse_contact_ratio_requirement.setter
    @enforce_parameter_types
    def transverse_contact_ratio_requirement(
        self: Self,
        value: "Union[_325.ContactRatioRequirements, Tuple[_325.ContactRatioRequirements, bool]]",
    ):
        wrapper_type = overridable.Overridable_ContactRatioRequirements.wrapper_type()
        enclosed_type = overridable.Overridable_ContactRatioRequirements.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def active_gear_set_design(self: Self) -> "_1032.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_design(self: Self) -> "_1032.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def supercharger_rotor_set(self: Self) -> "_2570.SuperchargerRotorSet":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.SuperchargerRotorSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerRotorSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears(self: Self) -> "List[_2532.CylindricalGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes(self: Self) -> "List[_2316.CylindricalGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set_designs(self: Self) -> "List[_1032.CylindricalGearSetDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_gear(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear"""
        method_result = self.wrapped.AddGear()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "CylindricalGearSet._Cast_CylindricalGearSet":
        return self._Cast_CylindricalGearSet(self)
