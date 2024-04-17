"""ConceptAxialClearanceBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs.concept import _2205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_AXIAL_CLEARANCE_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Concept", "ConceptAxialClearanceBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.concept import _2203
    from mastapy.bearings.bearing_designs import _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("ConceptAxialClearanceBearing",)


Self = TypeVar("Self", bound="ConceptAxialClearanceBearing")


class ConceptAxialClearanceBearing(_2205.ConceptClearanceBearing):
    """ConceptAxialClearanceBearing

    This is a mastapy class.
    """

    TYPE = _CONCEPT_AXIAL_CLEARANCE_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptAxialClearanceBearing")

    class _Cast_ConceptAxialClearanceBearing:
        """Special nested class for casting ConceptAxialClearanceBearing to subclasses."""

        def __init__(
            self: "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing",
            parent: "ConceptAxialClearanceBearing",
        ):
            self._parent = parent

        @property
        def concept_clearance_bearing(
            self: "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing",
        ) -> "_2205.ConceptClearanceBearing":
            return self._parent._cast(_2205.ConceptClearanceBearing)

        @property
        def non_linear_bearing(
            self: "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def concept_axial_clearance_bearing(
            self: "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing",
        ) -> "ConceptAxialClearanceBearing":
            return self._parent

        def __getattr__(
            self: "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptAxialClearanceBearing.TYPE"):
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
    def node_position(self: Self) -> "_2203.BearingNodePosition":
        """mastapy.bearings.bearing_designs.concept.BearingNodePosition"""
        temp = self.wrapped.NodePosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDesigns.Concept.BearingNodePosition"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.concept._2203", "BearingNodePosition"
        )(value)

    @node_position.setter
    @enforce_parameter_types
    def node_position(self: Self, value: "_2203.BearingNodePosition"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingDesigns.Concept.BearingNodePosition"
        )
        self.wrapped.NodePosition = value

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
    def thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Thickness

        if temp is None:
            return 0.0

        return temp

    @thickness.setter
    @enforce_parameter_types
    def thickness(self: Self, value: "float"):
        self.wrapped.Thickness = float(value) if value is not None else 0.0

    @property
    def x_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XStiffness

        if temp is None:
            return 0.0

        return temp

    @x_stiffness.setter
    @enforce_parameter_types
    def x_stiffness(self: Self, value: "float"):
        self.wrapped.XStiffness = float(value) if value is not None else 0.0

    @property
    def x_stiffness_applied_only_when_contacting(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.XStiffnessAppliedOnlyWhenContacting

        if temp is None:
            return False

        return temp

    @x_stiffness_applied_only_when_contacting.setter
    @enforce_parameter_types
    def x_stiffness_applied_only_when_contacting(self: Self, value: "bool"):
        self.wrapped.XStiffnessAppliedOnlyWhenContacting = (
            bool(value) if value is not None else False
        )

    @property
    def y_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YStiffness

        if temp is None:
            return 0.0

        return temp

    @y_stiffness.setter
    @enforce_parameter_types
    def y_stiffness(self: Self, value: "float"):
        self.wrapped.YStiffness = float(value) if value is not None else 0.0

    @property
    def y_stiffness_applied_only_when_contacting(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.YStiffnessAppliedOnlyWhenContacting

        if temp is None:
            return False

        return temp

    @y_stiffness_applied_only_when_contacting.setter
    @enforce_parameter_types
    def y_stiffness_applied_only_when_contacting(self: Self, value: "bool"):
        self.wrapped.YStiffnessAppliedOnlyWhenContacting = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptAxialClearanceBearing._Cast_ConceptAxialClearanceBearing":
        return self._Cast_ConceptAxialClearanceBearing(self)
