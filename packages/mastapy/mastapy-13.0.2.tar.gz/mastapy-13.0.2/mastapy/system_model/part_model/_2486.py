"""VirtualComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2469,
        _2470,
        _2478,
        _2479,
        _2484,
        _2451,
        _2475,
    )
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponent",)


Self = TypeVar("Self", bound="VirtualComponent")


class VirtualComponent(_2471.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponent")

    class _Cast_VirtualComponent:
        """Special nested class for casting VirtualComponent to subclasses."""

        def __init__(
            self: "VirtualComponent._Cast_VirtualComponent", parent: "VirtualComponent"
        ):
            self._parent = parent

        @property
        def mountable_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2471.MountableComponent":
            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "VirtualComponent._Cast_VirtualComponent") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def mass_disc(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2469.MassDisc":
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.MassDisc)

        @property
        def measurement_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2470.MeasurementComponent":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.MeasurementComponent)

        @property
        def point_load(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2478.PointLoad":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.PointLoad)

        @property
        def power_load(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2479.PowerLoad":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.PowerLoad)

        @property
        def unbalanced_mass(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2484.UnbalancedMass":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.UnbalancedMass)

        @property
        def virtual_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "VirtualComponent":
            return self._parent

        def __getattr__(self: "VirtualComponent._Cast_VirtualComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "VirtualComponent._Cast_VirtualComponent":
        return self._Cast_VirtualComponent(self)
