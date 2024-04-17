"""ConceptGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Concept", "ConceptGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1184, _1182
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshDesign",)


Self = TypeVar("Self", bound="ConceptGearMeshDesign")


class ConceptGearMeshDesign(_953.GearMeshDesign):
    """ConceptGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshDesign")

    class _Cast_ConceptGearMeshDesign:
        """Special nested class for casting ConceptGearMeshDesign to subclasses."""

        def __init__(
            self: "ConceptGearMeshDesign._Cast_ConceptGearMeshDesign",
            parent: "ConceptGearMeshDesign",
        ):
            self._parent = parent

        @property
        def gear_mesh_design(
            self: "ConceptGearMeshDesign._Cast_ConceptGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "ConceptGearMeshDesign._Cast_ConceptGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def concept_gear_mesh_design(
            self: "ConceptGearMeshDesign._Cast_ConceptGearMeshDesign",
        ) -> "ConceptGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshDesign._Cast_ConceptGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

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
    def concept_gear_set(self: Self) -> "_1184.ConceptGearSetDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "ConceptGearMeshDesign._Cast_ConceptGearMeshDesign":
        return self._Cast_ConceptGearMeshDesign(self)
