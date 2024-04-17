"""TorqueConverterTurbine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.couplings import _2592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbine",)


Self = TypeVar("Self", bound="TorqueConverterTurbine")


class TorqueConverterTurbine(_2592.CouplingHalf):
    """TorqueConverterTurbine

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterTurbine")

    class _Cast_TorqueConverterTurbine:
        """Special nested class for casting TorqueConverterTurbine to subclasses."""

        def __init__(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
            parent: "TorqueConverterTurbine",
        ):
            self._parent = parent

        @property
        def coupling_half(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
        ) -> "_2592.CouplingHalf":
            return self._parent._cast(_2592.CouplingHalf)

        @property
        def mountable_component(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def torque_converter_turbine(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine",
        ) -> "TorqueConverterTurbine":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbine._Cast_TorqueConverterTurbine", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterTurbine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TorqueConverterTurbine._Cast_TorqueConverterTurbine":
        return self._Cast_TorqueConverterTurbine(self)
