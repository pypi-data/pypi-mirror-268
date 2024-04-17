"""GearMaterialExpertSystemMaterialOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_EXPERT_SYSTEM_MATERIAL_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.Materials",
    "GearMaterialExpertSystemMaterialOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMaterialExpertSystemMaterialOptions",)


Self = TypeVar("Self", bound="GearMaterialExpertSystemMaterialOptions")


class GearMaterialExpertSystemMaterialOptions(_0.APIBase):
    """GearMaterialExpertSystemMaterialOptions

    This is a mastapy class.
    """

    TYPE = _GEAR_MATERIAL_EXPERT_SYSTEM_MATERIAL_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMaterialExpertSystemMaterialOptions"
    )

    class _Cast_GearMaterialExpertSystemMaterialOptions:
        """Special nested class for casting GearMaterialExpertSystemMaterialOptions to subclasses."""

        def __init__(
            self: "GearMaterialExpertSystemMaterialOptions._Cast_GearMaterialExpertSystemMaterialOptions",
            parent: "GearMaterialExpertSystemMaterialOptions",
        ):
            self._parent = parent

        @property
        def gear_material_expert_system_material_options(
            self: "GearMaterialExpertSystemMaterialOptions._Cast_GearMaterialExpertSystemMaterialOptions",
        ) -> "GearMaterialExpertSystemMaterialOptions":
            return self._parent

        def __getattr__(
            self: "GearMaterialExpertSystemMaterialOptions._Cast_GearMaterialExpertSystemMaterialOptions",
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
        self: Self, instance_to_wrap: "GearMaterialExpertSystemMaterialOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GearMaterialExpertSystemMaterialOptions._Cast_GearMaterialExpertSystemMaterialOptions":
        return self._Cast_GearMaterialExpertSystemMaterialOptions(self)
