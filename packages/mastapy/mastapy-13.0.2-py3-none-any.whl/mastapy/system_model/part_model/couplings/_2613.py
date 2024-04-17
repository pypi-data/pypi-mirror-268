"""SynchroniserPart"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.couplings import _2592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612, _2614
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPart",)


Self = TypeVar("Self", bound="SynchroniserPart")


class SynchroniserPart(_2592.CouplingHalf):
    """SynchroniserPart

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPart")

    class _Cast_SynchroniserPart:
        """Special nested class for casting SynchroniserPart to subclasses."""

        def __init__(
            self: "SynchroniserPart._Cast_SynchroniserPart", parent: "SynchroniserPart"
        ):
            self._parent = parent

        @property
        def coupling_half(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "_2592.CouplingHalf":
            return self._parent._cast(_2592.CouplingHalf)

        @property
        def mountable_component(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "SynchroniserPart._Cast_SynchroniserPart") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def synchroniser_half(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "_2612.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.SynchroniserHalf)

        @property
        def synchroniser_sleeve(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "_2614.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2614

            return self._parent._cast(_2614.SynchroniserSleeve)

        @property
        def synchroniser_part(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "SynchroniserPart":
            return self._parent

        def __getattr__(self: "SynchroniserPart._Cast_SynchroniserPart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SynchroniserPart._Cast_SynchroniserPart":
        return self._Cast_SynchroniserPart(self)
