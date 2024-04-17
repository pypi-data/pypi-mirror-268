"""Pulley"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.couplings import _2592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Pulley",)


Self = TypeVar("Self", bound="Pulley")


class Pulley(_2592.CouplingHalf):
    """Pulley

    This is a mastapy class.
    """

    TYPE = _PULLEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Pulley")

    class _Cast_Pulley:
        """Special nested class for casting Pulley to subclasses."""

        def __init__(self: "Pulley._Cast_Pulley", parent: "Pulley"):
            self._parent = parent

        @property
        def coupling_half(self: "Pulley._Cast_Pulley") -> "_2592.CouplingHalf":
            return self._parent._cast(_2592.CouplingHalf)

        @property
        def mountable_component(
            self: "Pulley._Cast_Pulley",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "Pulley._Cast_Pulley") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "Pulley._Cast_Pulley") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Pulley._Cast_Pulley") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cvt_pulley(self: "Pulley._Cast_Pulley") -> "_2595.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.CVTPulley)

        @property
        def pulley(self: "Pulley._Cast_Pulley") -> "Pulley":
            return self._parent

        def __getattr__(self: "Pulley._Cast_Pulley", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Pulley.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Pulley._Cast_Pulley":
        return self._Cast_Pulley(self)
