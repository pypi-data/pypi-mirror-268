"""GearMaterialExpertSystemMaterialDetails"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_EXPERT_SYSTEM_MATERIAL_DETAILS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.Materials",
    "GearMaterialExpertSystemMaterialDetails",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMaterialExpertSystemMaterialDetails",)


Self = TypeVar("Self", bound="GearMaterialExpertSystemMaterialDetails")


class GearMaterialExpertSystemMaterialDetails(_0.APIBase):
    """GearMaterialExpertSystemMaterialDetails

    This is a mastapy class.
    """

    TYPE = _GEAR_MATERIAL_EXPERT_SYSTEM_MATERIAL_DETAILS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMaterialExpertSystemMaterialDetails"
    )

    class _Cast_GearMaterialExpertSystemMaterialDetails:
        """Special nested class for casting GearMaterialExpertSystemMaterialDetails to subclasses."""

        def __init__(
            self: "GearMaterialExpertSystemMaterialDetails._Cast_GearMaterialExpertSystemMaterialDetails",
            parent: "GearMaterialExpertSystemMaterialDetails",
        ):
            self._parent = parent

        @property
        def gear_material_expert_system_material_details(
            self: "GearMaterialExpertSystemMaterialDetails._Cast_GearMaterialExpertSystemMaterialDetails",
        ) -> "GearMaterialExpertSystemMaterialDetails":
            return self._parent

        def __getattr__(
            self: "GearMaterialExpertSystemMaterialDetails._Cast_GearMaterialExpertSystemMaterialDetails",
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
        self: Self, instance_to_wrap: "GearMaterialExpertSystemMaterialDetails.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bar_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarLength

        if temp is None:
            return 0.0

        return temp

    @bar_length.setter
    @enforce_parameter_types
    def bar_length(self: Self, value: "float"):
        self.wrapped.BarLength = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "GearMaterialExpertSystemMaterialDetails._Cast_GearMaterialExpertSystemMaterialDetails":
        return self._Cast_GearMaterialExpertSystemMaterialDetails(self)
