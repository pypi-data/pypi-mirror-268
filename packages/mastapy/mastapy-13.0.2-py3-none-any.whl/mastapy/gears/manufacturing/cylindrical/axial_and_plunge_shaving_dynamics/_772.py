"""ShavingDynamicsConfiguration"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _754,
    _758,
)
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_CONFIGURATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsConfiguration",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _769,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsConfiguration",)


Self = TypeVar("Self", bound="ShavingDynamicsConfiguration")


class ShavingDynamicsConfiguration(_0.APIBase):
    """ShavingDynamicsConfiguration

    This is a mastapy class.
    """

    TYPE = _SHAVING_DYNAMICS_CONFIGURATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShavingDynamicsConfiguration")

    class _Cast_ShavingDynamicsConfiguration:
        """Special nested class for casting ShavingDynamicsConfiguration to subclasses."""

        def __init__(
            self: "ShavingDynamicsConfiguration._Cast_ShavingDynamicsConfiguration",
            parent: "ShavingDynamicsConfiguration",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_configuration(
            self: "ShavingDynamicsConfiguration._Cast_ShavingDynamicsConfiguration",
        ) -> "ShavingDynamicsConfiguration":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsConfiguration._Cast_ShavingDynamicsConfiguration",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShavingDynamicsConfiguration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conventional_shaving_dynamics(
        self: Self,
    ) -> "_769.ShavingDynamicsCalculation[_754.ConventionalShavingDynamics]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShavingDynamicsCalculation[mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ConventionalShavingDynamics]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConventionalShavingDynamics

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _754.ConventionalShavingDynamics
        ](temp)

    @property
    def plunge_shaving_dynamics(
        self: Self,
    ) -> "_769.ShavingDynamicsCalculation[_758.PlungeShaverDynamics]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShavingDynamicsCalculation[mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamics]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlungeShavingDynamics

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_758.PlungeShaverDynamics](
            temp
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingDynamicsConfiguration._Cast_ShavingDynamicsConfiguration":
        return self._Cast_ShavingDynamicsConfiguration(self)
