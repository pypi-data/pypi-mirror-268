"""ConceptGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.gears.gear_designs import _954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Concept", "ConceptGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1182, _1183
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetDesign",)


Self = TypeVar("Self", bound="ConceptGearSetDesign")


class ConceptGearSetDesign(_954.GearSetDesign):
    """ConceptGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetDesign")

    class _Cast_ConceptGearSetDesign:
        """Special nested class for casting ConceptGearSetDesign to subclasses."""

        def __init__(
            self: "ConceptGearSetDesign._Cast_ConceptGearSetDesign",
            parent: "ConceptGearSetDesign",
        ):
            self._parent = parent

        @property
        def gear_set_design(
            self: "ConceptGearSetDesign._Cast_ConceptGearSetDesign",
        ) -> "_954.GearSetDesign":
            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "ConceptGearSetDesign._Cast_ConceptGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def concept_gear_set_design(
            self: "ConceptGearSetDesign._Cast_ConceptGearSetDesign",
        ) -> "ConceptGearSetDesign":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetDesign._Cast_ConceptGearSetDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def working_normal_pressure_angle_gear_a_concave_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WorkingNormalPressureAngleGearAConcaveFlank

        if temp is None:
            return 0.0

        return temp

    @working_normal_pressure_angle_gear_a_concave_flank.setter
    @enforce_parameter_types
    def working_normal_pressure_angle_gear_a_concave_flank(self: Self, value: "float"):
        self.wrapped.WorkingNormalPressureAngleGearAConcaveFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def working_normal_pressure_angle_gear_a_convex_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WorkingNormalPressureAngleGearAConvexFlank

        if temp is None:
            return 0.0

        return temp

    @working_normal_pressure_angle_gear_a_convex_flank.setter
    @enforce_parameter_types
    def working_normal_pressure_angle_gear_a_convex_flank(self: Self, value: "float"):
        self.wrapped.WorkingNormalPressureAngleGearAConvexFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def gears(self: Self) -> "List[_1182.ConceptGearDesign]":
        """List[mastapy.gears.gear_designs.concept.ConceptGearDesign]

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
    def concept_gears(self: Self) -> "List[_1182.ConceptGearDesign]":
        """List[mastapy.gears.gear_designs.concept.ConceptGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes(self: Self) -> "List[_1183.ConceptGearMeshDesign]":
        """List[mastapy.gears.gear_designs.concept.ConceptGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConceptGearSetDesign._Cast_ConceptGearSetDesign":
        return self._Cast_ConceptGearSetDesign(self)
