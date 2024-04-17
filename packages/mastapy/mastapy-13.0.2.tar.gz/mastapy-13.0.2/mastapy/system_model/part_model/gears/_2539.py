"""GearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.gears.gear_designs import _954
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2521,
        _2523,
        _2527,
        _2529,
        _2531,
        _2533,
        _2536,
        _2542,
        _2544,
        _2546,
        _2548,
        _2549,
        _2551,
        _2553,
        _2555,
        _2559,
        _2561,
    )
    from mastapy.system_model.part_model import _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("GearSet",)


Self = TypeVar("Self", bound="GearSet")


class GearSet(_2483.SpecialisedAssembly):
    """GearSet

    This is a mastapy class.
    """

    TYPE = _GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSet")

    class _Cast_GearSet:
        """Special nested class for casting GearSet to subclasses."""

        def __init__(self: "GearSet._Cast_GearSet", parent: "GearSet"):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "GearSet._Cast_GearSet",
        ) -> "_2483.SpecialisedAssembly":
            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "GearSet._Cast_GearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "GearSet._Cast_GearSet") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "GearSet._Cast_GearSet") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def agma_gleason_conical_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2521.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2523.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self: "GearSet._Cast_GearSet") -> "_2527.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.BevelGearSet)

        @property
        def concept_gear_set(self: "GearSet._Cast_GearSet") -> "_2529.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.ConceptGearSet)

        @property
        def conical_gear_set(self: "GearSet._Cast_GearSet") -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def cylindrical_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2533.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.CylindricalGearSet)

        @property
        def face_gear_set(self: "GearSet._Cast_GearSet") -> "_2536.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.FaceGearSet)

        @property
        def hypoid_gear_set(self: "GearSet._Cast_GearSet") -> "_2542.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2549.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2551.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2553.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2555.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.StraightBevelGearSet)

        @property
        def worm_gear_set(self: "GearSet._Cast_GearSet") -> "_2559.WormGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.WormGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "GearSet._Cast_GearSet",
        ) -> "_2561.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.ZerolBevelGearSet)

        @property
        def gear_set(self: "GearSet._Cast_GearSet") -> "GearSet":
            return self._parent

        def __getattr__(self: "GearSet._Cast_GearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_design(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_GearSetDesign":
        """ListWithSelectedItem[mastapy.gears.gear_designs.GearSetDesign]"""
        temp = self.wrapped.ActiveDesign

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GearSetDesign",
        )(temp)

    @active_design.setter
    @enforce_parameter_types
    def active_design(self: Self, value: "_954.GearSetDesign"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GearSetDesign.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GearSetDesign.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ActiveDesign = value

    @property
    def maximum_number_of_teeth_in_mesh(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfTeethInMesh

        if temp is None:
            return 0

        return temp

    @maximum_number_of_teeth_in_mesh.setter
    @enforce_parameter_types
    def maximum_number_of_teeth_in_mesh(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfTeethInMesh = int(value) if value is not None else 0

    @property
    def mesh_ratio_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeshRatioLimit

        if temp is None:
            return 0.0

        return temp

    @mesh_ratio_limit.setter
    @enforce_parameter_types
    def mesh_ratio_limit(self: Self, value: "float"):
        self.wrapped.MeshRatioLimit = float(value) if value is not None else 0.0

    @property
    def minimum_number_of_teeth_in_mesh(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfTeethInMesh

        if temp is None:
            return 0

        return temp

    @minimum_number_of_teeth_in_mesh.setter
    @enforce_parameter_types
    def minimum_number_of_teeth_in_mesh(self: Self, value: "int"):
        self.wrapped.MinimumNumberOfTeethInMesh = int(value) if value is not None else 0

    @property
    def required_safety_factor_for_bending(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_bending.setter
    @enforce_parameter_types
    def required_safety_factor_for_bending(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForBending = value

    @property
    def required_safety_factor_for_contact(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_contact.setter
    @enforce_parameter_types
    def required_safety_factor_for_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForContact = value

    @property
    def required_safety_factor_for_static_bending(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForStaticBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_static_bending.setter
    @enforce_parameter_types
    def required_safety_factor_for_static_bending(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForStaticBending = value

    @property
    def required_safety_factor_for_static_contact(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForStaticContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_static_contact.setter
    @enforce_parameter_types
    def required_safety_factor_for_static_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForStaticContact = value

    @property
    def active_gear_set_design(self: Self) -> "_954.GearSetDesign":
        """mastapy.gears.gear_designs.GearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_designs(self: Self) -> "List[_954.GearSetDesign]":
        """List[mastapy.gears.gear_designs.GearSetDesign]

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

    @enforce_parameter_types
    def add_gear_set_design(self: Self, design: "_954.GearSetDesign"):
        """Method does not return.

        Args:
            design (mastapy.gears.gear_designs.GearSetDesign)
        """
        self.wrapped.AddGearSetDesign(design.wrapped if design else None)

    @enforce_parameter_types
    def remove_design(self: Self, design: "_954.GearSetDesign"):
        """Method does not return.

        Args:
            design (mastapy.gears.gear_designs.GearSetDesign)
        """
        self.wrapped.RemoveDesign(design.wrapped if design else None)

    @enforce_parameter_types
    def set_active_gear_set_design(self: Self, gear_set_design: "_954.GearSetDesign"):
        """Method does not return.

        Args:
            gear_set_design (mastapy.gears.gear_designs.GearSetDesign)
        """
        self.wrapped.SetActiveGearSetDesign(
            gear_set_design.wrapped if gear_set_design else None
        )

    @property
    def cast_to(self: Self) -> "GearSet._Cast_GearSet":
        return self._Cast_GearSet(self)
