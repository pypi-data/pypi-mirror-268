"""GearSetDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "GearSetDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _954
    from mastapy.gears.rating import _361, _368
    from mastapy.gears.rating.worm import _378
    from mastapy.gears.rating.face import _452
    from mastapy.gears.rating.cylindrical import _466, _483
    from mastapy.gears.rating.conical import _544
    from mastapy.gears.rating.concept import _555
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDutyCycleRating",)


Self = TypeVar("Self", bound="GearSetDutyCycleRating")


class GearSetDutyCycleRating(_358.AbstractGearSetRating):
    """GearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDutyCycleRating")

    class _Cast_GearSetDutyCycleRating:
        """Special nested class for casting GearSetDutyCycleRating to subclasses."""

        def __init__(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
            parent: "GearSetDutyCycleRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_358.AbstractGearSetRating":
            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_378.WormGearSetDutyCycleRating":
            from mastapy.gears.rating.worm import _378

            return self._parent._cast(_378.WormGearSetDutyCycleRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_452.FaceGearSetDutyCycleRating":
            from mastapy.gears.rating.face import _452

            return self._parent._cast(_452.FaceGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_466.CylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _466

            return self._parent._cast(_466.CylindricalGearSetDutyCycleRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_483.ReducedCylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _483

            return self._parent._cast(_483.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_544.ConicalGearSetDutyCycleRating":
            from mastapy.gears.rating.conical import _544

            return self._parent._cast(_544.ConicalGearSetDutyCycleRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "_555.ConceptGearSetDutyCycleRating":
            from mastapy.gears.rating.concept import _555

            return self._parent._cast(_555.ConceptGearSetDutyCycleRating)

        @property
        def gear_set_duty_cycle_rating(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating",
        ) -> "GearSetDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ""

        return temp

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def total_duty_cycle_gear_set_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDutyCycleGearSetReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design(self: Self) -> "_954.GearSetDesign":
        """mastapy.gears.gear_designs.GearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_361.GearDutyCycleRating]":
        """List[mastapy.gears.rating.GearDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_duty_cycle_ratings(self: Self) -> "List[_361.GearDutyCycleRating]":
        """List[mastapy.gears.rating.GearDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: Self) -> "List[_368.MeshDutyCycleRating]":
        """List[mastapy.gears.rating.MeshDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_duty_cycle_ratings(self: Self) -> "List[_368.MeshDutyCycleRating]":
        """List[mastapy.gears.rating.MeshDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def set_face_widths_for_specified_safety_factors(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self: Self) -> "GearSetDutyCycleRating._Cast_GearSetDutyCycleRating":
        return self._Cast_GearSetDutyCycleRating(self)
