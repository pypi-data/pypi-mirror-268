"""ParallelPartGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy.system_model.part_model.part_groups import _2493
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARALLEL_PART_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.PartGroups", "ParallelPartGroup"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2494, _2498, _2499


__docformat__ = "restructuredtext en"
__all__ = ("ParallelPartGroup",)


Self = TypeVar("Self", bound="ParallelPartGroup")


class ParallelPartGroup(_2493.ConcentricOrParallelPartGroup):
    """ParallelPartGroup

    This is a mastapy class.
    """

    TYPE = _PARALLEL_PART_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParallelPartGroup")

    class _Cast_ParallelPartGroup:
        """Special nested class for casting ParallelPartGroup to subclasses."""

        def __init__(
            self: "ParallelPartGroup._Cast_ParallelPartGroup",
            parent: "ParallelPartGroup",
        ):
            self._parent = parent

        @property
        def concentric_or_parallel_part_group(
            self: "ParallelPartGroup._Cast_ParallelPartGroup",
        ) -> "_2493.ConcentricOrParallelPartGroup":
            return self._parent._cast(_2493.ConcentricOrParallelPartGroup)

        @property
        def part_group(
            self: "ParallelPartGroup._Cast_ParallelPartGroup",
        ) -> "_2499.PartGroup":
            from mastapy.system_model.part_model.part_groups import _2499

            return self._parent._cast(_2499.PartGroup)

        @property
        def parallel_part_group_selection(
            self: "ParallelPartGroup._Cast_ParallelPartGroup",
        ) -> "_2498.ParallelPartGroupSelection":
            from mastapy.system_model.part_model.part_groups import _2498

            return self._parent._cast(_2498.ParallelPartGroupSelection)

        @property
        def parallel_part_group(
            self: "ParallelPartGroup._Cast_ParallelPartGroup",
        ) -> "ParallelPartGroup":
            return self._parent

        def __getattr__(self: "ParallelPartGroup._Cast_ParallelPartGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParallelPartGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_dx_axis_direction(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDXAxisDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def two_dy_axis_direction(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDYAxisDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def two_dz_axis_direction(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDZAxisDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def concentric_part_groups(self: Self) -> "List[_2494.ConcentricPartGroup]":
        """List[mastapy.system_model.part_model.part_groups.ConcentricPartGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConcentricPartGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ParallelPartGroup._Cast_ParallelPartGroup":
        return self._Cast_ParallelPartGroup(self)
