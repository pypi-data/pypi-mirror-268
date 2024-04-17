"""ConceptGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Concept", "ConceptGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1183
    from mastapy.gears.rating.concept import _554
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshRating",)


Self = TypeVar("Self", bound="ConceptGearMeshRating")


class ConceptGearMeshRating(_363.GearMeshRating):
    """ConceptGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshRating")

    class _Cast_ConceptGearMeshRating:
        """Special nested class for casting ConceptGearMeshRating to subclasses."""

        def __init__(
            self: "ConceptGearMeshRating._Cast_ConceptGearMeshRating",
            parent: "ConceptGearMeshRating",
        ):
            self._parent = parent

        @property
        def gear_mesh_rating(
            self: "ConceptGearMeshRating._Cast_ConceptGearMeshRating",
        ) -> "_363.GearMeshRating":
            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "ConceptGearMeshRating._Cast_ConceptGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConceptGearMeshRating._Cast_ConceptGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def concept_gear_mesh_rating(
            self: "ConceptGearMeshRating._Cast_ConceptGearMeshRating",
        ) -> "ConceptGearMeshRating":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshRating._Cast_ConceptGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concept_gear_mesh(self: Self) -> "_1183.ConceptGearMeshDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear_ratings(self: Self) -> "List[_554.ConceptGearRating]":
        """List[mastapy.gears.rating.concept.ConceptGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConceptGearMeshRating._Cast_ConceptGearMeshRating":
        return self._Cast_ConceptGearMeshRating(self)
