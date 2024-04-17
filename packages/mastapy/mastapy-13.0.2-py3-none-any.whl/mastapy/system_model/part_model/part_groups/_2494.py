"""ConcentricPartGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_2d import Vector2D
from mastapy.system_model.part_model.part_groups import _2493
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_PART_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.PartGroups", "ConcentricPartGroup"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2495, _2499


__docformat__ = "restructuredtext en"
__all__ = ("ConcentricPartGroup",)


Self = TypeVar("Self", bound="ConcentricPartGroup")


class ConcentricPartGroup(_2493.ConcentricOrParallelPartGroup):
    """ConcentricPartGroup

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_PART_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConcentricPartGroup")

    class _Cast_ConcentricPartGroup:
        """Special nested class for casting ConcentricPartGroup to subclasses."""

        def __init__(
            self: "ConcentricPartGroup._Cast_ConcentricPartGroup",
            parent: "ConcentricPartGroup",
        ):
            self._parent = parent

        @property
        def concentric_or_parallel_part_group(
            self: "ConcentricPartGroup._Cast_ConcentricPartGroup",
        ) -> "_2493.ConcentricOrParallelPartGroup":
            return self._parent._cast(_2493.ConcentricOrParallelPartGroup)

        @property
        def part_group(
            self: "ConcentricPartGroup._Cast_ConcentricPartGroup",
        ) -> "_2499.PartGroup":
            from mastapy.system_model.part_model.part_groups import _2499

            return self._parent._cast(_2499.PartGroup)

        @property
        def concentric_part_group(
            self: "ConcentricPartGroup._Cast_ConcentricPartGroup",
        ) -> "ConcentricPartGroup":
            return self._parent

        def __getattr__(
            self: "ConcentricPartGroup._Cast_ConcentricPartGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConcentricPartGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_of_cylindrical_gear_face_widths(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalOfCylindricalGearFaceWidths

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_position(self: Self) -> "Vector2D":
        """Vector2D"""
        temp = self.wrapped.RadialPosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @radial_position.setter
    @enforce_parameter_types
    def radial_position(self: Self, value: "Vector2D"):
        value = conversion.mp_to_pn_vector2d(value)
        self.wrapped.RadialPosition = value

    @property
    def parallel_groups(self: Self) -> "List[_2495.ConcentricPartGroupParallelToThis]":
        """List[mastapy.system_model.part_model.part_groups.ConcentricPartGroupParallelToThis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParallelGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConcentricPartGroup._Cast_ConcentricPartGroup":
        return self._Cast_ConcentricPartGroup(self)
