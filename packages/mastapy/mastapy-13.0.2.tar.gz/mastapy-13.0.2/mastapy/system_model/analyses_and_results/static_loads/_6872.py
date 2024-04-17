"""CylindricalGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, overridable_enum_runtime, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _513
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.static_loads import _6901
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.gears.materials import _601
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6873,
        _6920,
        _6858,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshLoadCase",)


Self = TypeVar("Self", bound="CylindricalGearMeshLoadCase")


class CylindricalGearMeshLoadCase(_6901.GearMeshLoadCase):
    """CylindricalGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshLoadCase")

    class _Cast_CylindricalGearMeshLoadCase:
        """Special nested class for casting CylindricalGearMeshLoadCase to subclasses."""

        def __init__(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
            parent: "CylindricalGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_case(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "_6901.GearMeshLoadCase":
            return self._parent._cast(_6901.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
        ) -> "CylindricalGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @application_factor.setter
    @enforce_parameter_types
    def application_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ApplicationFactor = value

    @property
    def change_in_centre_distance_due_to_housing_thermal_effects(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInCentreDistanceDueToHousingThermalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def do_profile_modifications_compensate_for_the_deflections_at_actual_load(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.DoProfileModificationsCompensateForTheDeflectionsAtActualLoad
        )

        if temp is None:
            return False

        return temp

    @do_profile_modifications_compensate_for_the_deflections_at_actual_load.setter
    @enforce_parameter_types
    def do_profile_modifications_compensate_for_the_deflections_at_actual_load(
        self: Self, value: "bool"
    ):
        self.wrapped.DoProfileModificationsCompensateForTheDeflectionsAtActualLoad = (
            bool(value) if value is not None else False
        )

    @property
    def dynamic_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_factor.setter
    @enforce_parameter_types
    def dynamic_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicFactor = value

    @property
    def face_load_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FaceLoadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @face_load_factor_bending.setter
    @enforce_parameter_types
    def face_load_factor_bending(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FaceLoadFactorBending = value

    @property
    def face_load_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FaceLoadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @face_load_factor_contact.setter
    @enforce_parameter_types
    def face_load_factor_contact(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FaceLoadFactorContact = value

    @property
    def helical_gear_micro_geometry_option(
        self: Self,
    ) -> "overridable.Overridable_HelicalGearMicroGeometryOption":
        """Overridable[mastapy.gears.rating.cylindrical.iso6336.HelicalGearMicroGeometryOption]"""
        temp = self.wrapped.HelicalGearMicroGeometryOption

        if temp is None:
            return None

        value = overridable.Overridable_HelicalGearMicroGeometryOption.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @helical_gear_micro_geometry_option.setter
    @enforce_parameter_types
    def helical_gear_micro_geometry_option(
        self: Self,
        value: "Union[_513.HelicalGearMicroGeometryOption, Tuple[_513.HelicalGearMicroGeometryOption, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_HelicalGearMicroGeometryOption.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_HelicalGearMicroGeometryOption.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.HelicalGearMicroGeometryOption = value

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_database(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsDatabase.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_database.setter
    @enforce_parameter_types
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_database(
        self: Self, value: "str"
    ):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def maximum_number_of_times_out_of_contact_before_being_considered_converged(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = (
            self.wrapped.MaximumNumberOfTimesOutOfContactBeforeBeingConsideredConverged
        )

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_number_of_times_out_of_contact_before_being_considered_converged.setter
    @enforce_parameter_types
    def maximum_number_of_times_out_of_contact_before_being_considered_converged(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumNumberOfTimesOutOfContactBeforeBeingConsideredConverged = (
            value
        )

    @property
    def misalignment(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Misalignment

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @misalignment.setter
    @enforce_parameter_types
    def misalignment(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Misalignment = value

    @property
    def misalignment_due_to_manufacturing_tolerances(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MisalignmentDueToManufacturingTolerances

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @misalignment_due_to_manufacturing_tolerances.setter
    @enforce_parameter_types
    def misalignment_due_to_manufacturing_tolerances(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MisalignmentDueToManufacturingTolerances = value

    @property
    def override_misalignment_in_system_deflection_and_ltca(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideMisalignmentInSystemDeflectionAndLTCA

        if temp is None:
            return False

        return temp

    @override_misalignment_in_system_deflection_and_ltca.setter
    @enforce_parameter_types
    def override_misalignment_in_system_deflection_and_ltca(self: Self, value: "bool"):
        self.wrapped.OverrideMisalignmentInSystemDeflectionAndLTCA = (
            bool(value) if value is not None else False
        )

    @property
    def permissible_specific_lubricant_film_thickness(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PermissibleSpecificLubricantFilmThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @permissible_specific_lubricant_film_thickness.setter
    @enforce_parameter_types
    def permissible_specific_lubricant_film_thickness(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PermissibleSpecificLubricantFilmThickness = value

    @property
    def transverse_load_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @transverse_load_factor_bending.setter
    @enforce_parameter_types
    def transverse_load_factor_bending(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TransverseLoadFactorBending = value

    @property
    def transverse_load_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TransverseLoadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @transverse_load_factor_contact.setter
    @enforce_parameter_types
    def transverse_load_factor_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TransverseLoadFactorContact = value

    @property
    def use_design_iso14179_part_1_coefficient_of_friction_constants_and_exponents(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseDesignISO14179Part1CoefficientOfFrictionConstantsAndExponents
        )

        if temp is None:
            return False

        return temp

    @use_design_iso14179_part_1_coefficient_of_friction_constants_and_exponents.setter
    @enforce_parameter_types
    def use_design_iso14179_part_1_coefficient_of_friction_constants_and_exponents(
        self: Self, value: "bool"
    ):
        self.wrapped.UseDesignISO14179Part1CoefficientOfFrictionConstantsAndExponents = (
            bool(value) if value is not None else False
        )

    @property
    def user_specified_coefficient_of_friction(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UserSpecifiedCoefficientOfFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @user_specified_coefficient_of_friction.setter
    @enforce_parameter_types
    def user_specified_coefficient_of_friction(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UserSpecifiedCoefficientOfFriction = value

    @property
    def connection_design(self: Self) -> "_2316.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents(
        self: Self,
    ) -> "_601.ISOTR1417912001CoefficientOfFrictionConstants":
        """mastapy.gears.materials.ISOTR1417912001CoefficientOfFrictionConstants

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6873.CylindricalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshLoadCase._Cast_CylindricalGearMeshLoadCase":
        return self._Cast_CylindricalGearMeshLoadCase(self)
