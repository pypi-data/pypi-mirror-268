"""ConceptGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Concept", "ConceptGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearDesign",)


Self = TypeVar("Self", bound="ConceptGearDesign")


class ConceptGearDesign(_951.GearDesign):
    """ConceptGearDesign

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearDesign")

    class _Cast_ConceptGearDesign:
        """Special nested class for casting ConceptGearDesign to subclasses."""

        def __init__(
            self: "ConceptGearDesign._Cast_ConceptGearDesign",
            parent: "ConceptGearDesign",
        ):
            self._parent = parent

        @property
        def gear_design(
            self: "ConceptGearDesign._Cast_ConceptGearDesign",
        ) -> "_951.GearDesign":
            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "ConceptGearDesign._Cast_ConceptGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def concept_gear_design(
            self: "ConceptGearDesign._Cast_ConceptGearDesign",
        ) -> "ConceptGearDesign":
            return self._parent

        def __getattr__(self: "ConceptGearDesign._Cast_ConceptGearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self: Self) -> "_336.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._336", "Hand")(value)

    @hand.setter
    @enforce_parameter_types
    def hand(self: Self, value: "_336.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def mean_point_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPointToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @pitch_angle.setter
    @enforce_parameter_types
    def pitch_angle(self: Self, value: "float"):
        self.wrapped.PitchAngle = float(value) if value is not None else 0.0

    @property
    def pitch_apex_to_crossing_point(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchApexToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @pitch_apex_to_crossing_point.setter
    @enforce_parameter_types
    def pitch_apex_to_crossing_point(self: Self, value: "float"):
        self.wrapped.PitchApexToCrossingPoint = (
            float(value) if value is not None else 0.0
        )

    @property
    def working_helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WorkingHelixAngle

        if temp is None:
            return 0.0

        return temp

    @working_helix_angle.setter
    @enforce_parameter_types
    def working_helix_angle(self: Self, value: "float"):
        self.wrapped.WorkingHelixAngle = float(value) if value is not None else 0.0

    @property
    def working_pitch_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WorkingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @working_pitch_diameter.setter
    @enforce_parameter_types
    def working_pitch_diameter(self: Self, value: "float"):
        self.wrapped.WorkingPitchDiameter = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConceptGearDesign._Cast_ConceptGearDesign":
        return self._Cast_ConceptGearDesign(self)
