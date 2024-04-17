"""Bolt"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450, _2475
    from mastapy.bolts import _1489
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Bolt",)


Self = TypeVar("Self", bound="Bolt")


class Bolt(_2451.Component):
    """Bolt

    This is a mastapy class.
    """

    TYPE = _BOLT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Bolt")

    class _Cast_Bolt:
        """Special nested class for casting Bolt to subclasses."""

        def __init__(self: "Bolt._Cast_Bolt", parent: "Bolt"):
            self._parent = parent

        @property
        def component(self: "Bolt._Cast_Bolt") -> "_2451.Component":
            return self._parent._cast(_2451.Component)

        @property
        def part(self: "Bolt._Cast_Bolt") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Bolt._Cast_Bolt") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bolt(self: "Bolt._Cast_Bolt") -> "Bolt":
            return self._parent

        def __getattr__(self: "Bolt._Cast_Bolt", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Bolt.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bolted_joint(self: Self) -> "_2450.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltedJoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loaded_bolt(self: Self) -> "_1489.LoadedBolt":
        """mastapy.bolts.LoadedBolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBolt

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Bolt._Cast_Bolt":
        return self._Cast_Bolt(self)
