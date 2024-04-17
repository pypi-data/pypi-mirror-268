"""CylindricalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CylindricalGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6871,
        _6875,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLoadCase",)


Self = TypeVar("Self", bound="CylindricalGearLoadCase")


class CylindricalGearLoadCase(_6899.GearLoadCase):
    """CylindricalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearLoadCase")

    class _Cast_CylindricalGearLoadCase:
        """Special nested class for casting CylindricalGearLoadCase to subclasses."""

        def __init__(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
            parent: "CylindricalGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_6899.GearLoadCase":
            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_6875.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.CylindricalPlanetGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "CylindricalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_reaction_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialReactionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def lateral_reaction_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LateralReactionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def lateral_reaction_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LateralReactionMoment

        if temp is None:
            return 0.0

        return temp

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
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def reversed_bending_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ReversedBendingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @reversed_bending_factor.setter
    @enforce_parameter_types
    def reversed_bending_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ReversedBendingFactor = value

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def vertical_reaction_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VerticalReactionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def vertical_reaction_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VerticalReactionMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_manufacture_errors(self: Self) -> "_6871.CylindricalGearManufactureError":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overridden_micro_geometry(
        self: Self,
    ) -> "_1107.CylindricalGearMicroGeometryBase":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverriddenMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase]

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

    @property
    def cast_to(self: Self) -> "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase":
        return self._Cast_CylindricalGearLoadCase(self)
