"""MeasurementComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2486
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponent",)


Self = TypeVar("Self", bound="MeasurementComponent")


class MeasurementComponent(_2486.VirtualComponent):
    """MeasurementComponent

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementComponent")

    class _Cast_MeasurementComponent:
        """Special nested class for casting MeasurementComponent to subclasses."""

        def __init__(
            self: "MeasurementComponent._Cast_MeasurementComponent",
            parent: "MeasurementComponent",
        ):
            self._parent = parent

        @property
        def virtual_component(
            self: "MeasurementComponent._Cast_MeasurementComponent",
        ) -> "_2486.VirtualComponent":
            return self._parent._cast(_2486.VirtualComponent)

        @property
        def mountable_component(
            self: "MeasurementComponent._Cast_MeasurementComponent",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "MeasurementComponent._Cast_MeasurementComponent",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "MeasurementComponent._Cast_MeasurementComponent",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "MeasurementComponent._Cast_MeasurementComponent",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def measurement_component(
            self: "MeasurementComponent._Cast_MeasurementComponent",
        ) -> "MeasurementComponent":
            return self._parent

        def __getattr__(
            self: "MeasurementComponent._Cast_MeasurementComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasurementComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MeasurementComponent._Cast_MeasurementComponent":
        return self._Cast_MeasurementComponent(self)
