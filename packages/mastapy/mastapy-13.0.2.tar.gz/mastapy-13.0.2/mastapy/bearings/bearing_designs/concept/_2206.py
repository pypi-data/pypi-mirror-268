"""ConceptRadialClearanceBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.bearings.bearing_designs.concept import _2205
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CONCEPT_RADIAL_CLEARANCE_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Concept", "ConceptRadialClearanceBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs import _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("ConceptRadialClearanceBearing",)


Self = TypeVar("Self", bound="ConceptRadialClearanceBearing")


class ConceptRadialClearanceBearing(_2205.ConceptClearanceBearing):
    """ConceptRadialClearanceBearing

    This is a mastapy class.
    """

    TYPE = _CONCEPT_RADIAL_CLEARANCE_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptRadialClearanceBearing")

    class _Cast_ConceptRadialClearanceBearing:
        """Special nested class for casting ConceptRadialClearanceBearing to subclasses."""

        def __init__(
            self: "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing",
            parent: "ConceptRadialClearanceBearing",
        ):
            self._parent = parent

        @property
        def concept_clearance_bearing(
            self: "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing",
        ) -> "_2205.ConceptClearanceBearing":
            return self._parent._cast(_2205.ConceptClearanceBearing)

        @property
        def non_linear_bearing(
            self: "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def concept_radial_clearance_bearing(
            self: "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing",
        ) -> "ConceptRadialClearanceBearing":
            return self._parent

        def __getattr__(
            self: "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptRadialClearanceBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def contact_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactAngle

        if temp is None:
            return 0.0

        return temp

    @contact_angle.setter
    @enforce_parameter_types
    def contact_angle(self: Self, value: "float"):
        self.wrapped.ContactAngle = float(value) if value is not None else 0.0

    @property
    def contact_diameter_derived_from_connection_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ContactDiameterDerivedFromConnectionGeometry

        if temp is None:
            return False

        return temp

    @contact_diameter_derived_from_connection_geometry.setter
    @enforce_parameter_types
    def contact_diameter_derived_from_connection_geometry(self: Self, value: "bool"):
        self.wrapped.ContactDiameterDerivedFromConnectionGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def end_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EndAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @end_angle.setter
    @enforce_parameter_types
    def end_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EndAngle = value

    @property
    def has_stiffness_only_in_eccentricity_direction(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasStiffnessOnlyInEccentricityDirection

        if temp is None:
            return False

        return temp

    @has_stiffness_only_in_eccentricity_direction.setter
    @enforce_parameter_types
    def has_stiffness_only_in_eccentricity_direction(self: Self, value: "bool"):
        self.wrapped.HasStiffnessOnlyInEccentricityDirection = (
            bool(value) if value is not None else False
        )

    @property
    def inner_component_material_selector(self: Self) -> "str":
        """str"""
        temp = self.wrapped.InnerComponentMaterialSelector.SelectedItemName

        if temp is None:
            return ""

        return temp

    @inner_component_material_selector.setter
    @enforce_parameter_types
    def inner_component_material_selector(self: Self, value: "str"):
        self.wrapped.InnerComponentMaterialSelector.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def outer_component_material_selector(self: Self) -> "str":
        """str"""
        temp = self.wrapped.OuterComponentMaterialSelector.SelectedItemName

        if temp is None:
            return ""

        return temp

    @outer_component_material_selector.setter
    @enforce_parameter_types
    def outer_component_material_selector(self: Self, value: "str"):
        self.wrapped.OuterComponentMaterialSelector.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def start_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.StartAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @start_angle.setter
    @enforce_parameter_types
    def start_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.StartAngle = value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptRadialClearanceBearing._Cast_ConceptRadialClearanceBearing":
        return self._Cast_ConceptRadialClearanceBearing(self)
