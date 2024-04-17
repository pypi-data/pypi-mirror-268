"""ClutchHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.couplings import _2592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalf",)


Self = TypeVar("Self", bound="ClutchHalf")


class ClutchHalf(_2592.CouplingHalf):
    """ClutchHalf

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalf")

    class _Cast_ClutchHalf:
        """Special nested class for casting ClutchHalf to subclasses."""

        def __init__(self: "ClutchHalf._Cast_ClutchHalf", parent: "ClutchHalf"):
            self._parent = parent

        @property
        def coupling_half(self: "ClutchHalf._Cast_ClutchHalf") -> "_2592.CouplingHalf":
            return self._parent._cast(_2592.CouplingHalf)

        @property
        def mountable_component(
            self: "ClutchHalf._Cast_ClutchHalf",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "ClutchHalf._Cast_ClutchHalf") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "ClutchHalf._Cast_ClutchHalf") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "ClutchHalf._Cast_ClutchHalf") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def clutch_half(self: "ClutchHalf._Cast_ClutchHalf") -> "ClutchHalf":
            return self._parent

        def __getattr__(self: "ClutchHalf._Cast_ClutchHalf", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_mounted_on_shaft_outer(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMountedOnShaftOuter

        if temp is None:
            return False

        return temp

    @is_mounted_on_shaft_outer.setter
    @enforce_parameter_types
    def is_mounted_on_shaft_outer(self: Self, value: "bool"):
        self.wrapped.IsMountedOnShaftOuter = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "ClutchHalf._Cast_ClutchHalf":
        return self._Cast_ClutchHalf(self)
