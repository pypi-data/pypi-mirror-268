"""ConcentricPartGroupParallelToThis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_PART_GROUP_PARALLEL_TO_THIS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.PartGroups", "ConcentricPartGroupParallelToThis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2493


__docformat__ = "restructuredtext en"
__all__ = ("ConcentricPartGroupParallelToThis",)


Self = TypeVar("Self", bound="ConcentricPartGroupParallelToThis")


class ConcentricPartGroupParallelToThis(_0.APIBase):
    """ConcentricPartGroupParallelToThis

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_PART_GROUP_PARALLEL_TO_THIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConcentricPartGroupParallelToThis")

    class _Cast_ConcentricPartGroupParallelToThis:
        """Special nested class for casting ConcentricPartGroupParallelToThis to subclasses."""

        def __init__(
            self: "ConcentricPartGroupParallelToThis._Cast_ConcentricPartGroupParallelToThis",
            parent: "ConcentricPartGroupParallelToThis",
        ):
            self._parent = parent

        @property
        def concentric_part_group_parallel_to_this(
            self: "ConcentricPartGroupParallelToThis._Cast_ConcentricPartGroupParallelToThis",
        ) -> "ConcentricPartGroupParallelToThis":
            return self._parent

        def __getattr__(
            self: "ConcentricPartGroupParallelToThis._Cast_ConcentricPartGroupParallelToThis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ConcentricPartGroupParallelToThis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def parallel_group(self: Self) -> "_2493.ConcentricOrParallelPartGroup":
        """mastapy.system_model.part_model.part_groups.ConcentricOrParallelPartGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParallelGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConcentricPartGroupParallelToThis._Cast_ConcentricPartGroupParallelToThis":
        return self._Cast_ConcentricPartGroupParallelToThis(self)
