"""CylindricalGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, overridable_enum_runtime
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials.efficiency import _297
from mastapy.system_model.analyses_and_results.static_loads import _6904
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.gears import _322
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6950,
        _6870,
        _6872,
        _6873,
        _6942,
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.gears.gear_designs.cylindrical import _1063
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetLoadCase",)


Self = TypeVar("Self", bound="CylindricalGearSetLoadCase")


class CylindricalGearSetLoadCase(_6904.GearSetLoadCase):
    """CylindricalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetLoadCase")

    class _Cast_CylindricalGearSetLoadCase:
        """Special nested class for casting CylindricalGearSetLoadCase to subclasses."""

        def __init__(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
            parent: "CylindricalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_6904.GearSetLoadCase":
            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "_6942.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.PlanetaryGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "CylindricalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boost_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BoostPressure

        if temp is None:
            return 0.0

        return temp

    @boost_pressure.setter
    @enforce_parameter_types
    def boost_pressure(self: Self, value: "float"):
        self.wrapped.BoostPressure = float(value) if value is not None else 0.0

    @property
    def coefficient_of_friction_calculation_method(
        self: Self,
    ) -> "_322.CoefficientOfFrictionCalculationMethod":
        """mastapy.gears.CoefficientOfFrictionCalculationMethod"""
        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._322", "CoefficientOfFrictionCalculationMethod"
        )(value)

    @coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def coefficient_of_friction_calculation_method(
        self: Self, value: "_322.CoefficientOfFrictionCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def dynamic_load_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_load_factor.setter
    @enforce_parameter_types
    def dynamic_load_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicLoadFactor = value

    @property
    def efficiency_rating_method(
        self: Self,
    ) -> "overridable.Overridable_EfficiencyRatingMethod":
        """Overridable[mastapy.materials.efficiency.EfficiencyRatingMethod]"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = overridable.Overridable_EfficiencyRatingMethod.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(
        self: Self,
        value: "Union[_297.EfficiencyRatingMethod, Tuple[_297.EfficiencyRatingMethod, bool]]",
    ):
        wrapper_type = overridable.Overridable_EfficiencyRatingMethod.wrapper_type()
        enclosed_type = overridable.Overridable_EfficiencyRatingMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def override_micro_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideMicroGeometry

        if temp is None:
            return False

        return temp

    @override_micro_geometry.setter
    @enforce_parameter_types
    def override_micro_geometry(self: Self, value: "bool"):
        self.wrapped.OverrideMicroGeometry = bool(value) if value is not None else False

    @property
    def reset_micro_geometry(self: Self) -> "_6950.ResetMicroGeometryOptions":
        """mastapy.system_model.analyses_and_results.static_loads.ResetMicroGeometryOptions"""
        temp = self.wrapped.ResetMicroGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ResetMicroGeometryOptions",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6950",
            "ResetMicroGeometryOptions",
        )(value)

    @reset_micro_geometry.setter
    @enforce_parameter_types
    def reset_micro_geometry(self: Self, value: "_6950.ResetMicroGeometryOptions"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ResetMicroGeometryOptions",
        )
        self.wrapped.ResetMicroGeometry = value

    @property
    def use_design_coefficient_of_friction_calculation_method(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod

        if temp is None:
            return False

        return temp

    @use_design_coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def use_design_coefficient_of_friction_calculation_method(
        self: Self, value: "bool"
    ):
        self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod = (
            bool(value) if value is not None else False
        )

    @property
    def use_design_default_ltca_settings(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignDefaultLTCASettings

        if temp is None:
            return False

        return temp

    @use_design_default_ltca_settings.setter
    @enforce_parameter_types
    def use_design_default_ltca_settings(self: Self, value: "bool"):
        self.wrapped.UseDesignDefaultLTCASettings = (
            bool(value) if value is not None else False
        )

    @property
    def assembly_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ltca(self: Self) -> "_1063.LTCALoadCaseModifiableSettings":
        """mastapy.gears.gear_designs.cylindrical.LTCALoadCaseModifiableSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LTCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overridden_micro_geometry(
        self: Self,
    ) -> "_1113.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverriddenMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6870.CylindricalGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase]

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
    def cylindrical_gears_load_case(
        self: Self,
    ) -> "List[_6870.CylindricalGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_load_case(
        self: Self,
    ) -> "List[_6872.CylindricalGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesLoadCase

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
    ) -> "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase":
        return self._Cast_CylindricalGearSetLoadCase(self)
