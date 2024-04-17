"""DetailedBoltedJointDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BOLTED_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.Bolts", "DetailedBoltedJointDesign"
)

if TYPE_CHECKING:
    from mastapy.bolts import _1489


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBoltedJointDesign",)


Self = TypeVar("Self", bound="DetailedBoltedJointDesign")


class DetailedBoltedJointDesign(_0.APIBase):
    """DetailedBoltedJointDesign

    This is a mastapy class.
    """

    TYPE = _DETAILED_BOLTED_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedBoltedJointDesign")

    class _Cast_DetailedBoltedJointDesign:
        """Special nested class for casting DetailedBoltedJointDesign to subclasses."""

        def __init__(
            self: "DetailedBoltedJointDesign._Cast_DetailedBoltedJointDesign",
            parent: "DetailedBoltedJointDesign",
        ):
            self._parent = parent

        @property
        def detailed_bolted_joint_design(
            self: "DetailedBoltedJointDesign._Cast_DetailedBoltedJointDesign",
        ) -> "DetailedBoltedJointDesign":
            return self._parent

        def __getattr__(
            self: "DetailedBoltedJointDesign._Cast_DetailedBoltedJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedBoltedJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def number_of_bolts(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfBolts

        if temp is None:
            return 0

        return temp

    @property
    def loaded_bolts(self: Self) -> "List[_1489.LoadedBolt]":
        """List[mastapy.bolts.LoadedBolt]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "DetailedBoltedJointDesign._Cast_DetailedBoltedJointDesign":
        return self._Cast_DetailedBoltedJointDesign(self)
