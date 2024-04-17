"""ConceptGearMeshDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _368
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Concept", "ConceptGearMeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshDutyCycleRating",)


Self = TypeVar("Self", bound="ConceptGearMeshDutyCycleRating")


class ConceptGearMeshDutyCycleRating(_368.MeshDutyCycleRating):
    """ConceptGearMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshDutyCycleRating")

    class _Cast_ConceptGearMeshDutyCycleRating:
        """Special nested class for casting ConceptGearMeshDutyCycleRating to subclasses."""

        def __init__(
            self: "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating",
            parent: "ConceptGearMeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(
            self: "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating",
        ) -> "_368.MeshDutyCycleRating":
            return self._parent._cast(_368.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(
            self: "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating",
        ) -> "ConceptGearMeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshDutyCycleRating._Cast_ConceptGearMeshDutyCycleRating":
        return self._Cast_ConceptGearMeshDutyCycleRating(self)
