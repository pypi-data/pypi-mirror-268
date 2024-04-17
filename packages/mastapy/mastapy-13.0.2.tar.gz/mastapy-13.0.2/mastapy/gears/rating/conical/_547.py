"""ConicalMeshDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating import _368
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalMeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _542
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshDutyCycleRating",)


Self = TypeVar("Self", bound="ConicalMeshDutyCycleRating")


class ConicalMeshDutyCycleRating(_368.MeshDutyCycleRating):
    """ConicalMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshDutyCycleRating")

    class _Cast_ConicalMeshDutyCycleRating:
        """Special nested class for casting ConicalMeshDutyCycleRating to subclasses."""

        def __init__(
            self: "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating",
            parent: "ConicalMeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(
            self: "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating",
        ) -> "_368.MeshDutyCycleRating":
            return self._parent._cast(_368.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(
            self: "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating",
        ) -> "ConicalMeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_ratings(self: Self) -> "List[_542.ConicalGearMeshRating]":
        """List[mastapy.gears.rating.conical.ConicalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating":
        return self._Cast_ConicalMeshDutyCycleRating(self)
