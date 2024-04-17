"""ConceptGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Concept", "ConceptGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.gear_designs.concept import _1182
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearRating",)


Self = TypeVar("Self", bound="ConceptGearRating")


class ConceptGearRating(_364.GearRating):
    """ConceptGearRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearRating")

    class _Cast_ConceptGearRating:
        """Special nested class for casting ConceptGearRating to subclasses."""

        def __init__(
            self: "ConceptGearRating._Cast_ConceptGearRating",
            parent: "ConceptGearRating",
        ):
            self._parent = parent

        @property
        def gear_rating(
            self: "ConceptGearRating._Cast_ConceptGearRating",
        ) -> "_364.GearRating":
            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "ConceptGearRating._Cast_ConceptGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "ConceptGearRating._Cast_ConceptGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def concept_gear_rating(
            self: "ConceptGearRating._Cast_ConceptGearRating",
        ) -> "ConceptGearRating":
            return self._parent

        def __getattr__(self: "ConceptGearRating._Cast_ConceptGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear(self: Self) -> "_1182.ConceptGearDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def convex_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearRating._Cast_ConceptGearRating":
        return self._Cast_ConceptGearRating(self)
