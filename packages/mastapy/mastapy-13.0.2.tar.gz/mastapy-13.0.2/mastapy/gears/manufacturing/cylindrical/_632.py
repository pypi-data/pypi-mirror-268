"""GearManufacturingConfigurationViewModelPlaceholder"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical import _631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL_PLACEHOLDER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "GearManufacturingConfigurationViewModelPlaceholder",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearManufacturingConfigurationViewModelPlaceholder",)


Self = TypeVar("Self", bound="GearManufacturingConfigurationViewModelPlaceholder")


class GearManufacturingConfigurationViewModelPlaceholder(
    _631.GearManufacturingConfigurationViewModel
):
    """GearManufacturingConfigurationViewModelPlaceholder

    This is a mastapy class.
    """

    TYPE = _GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL_PLACEHOLDER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearManufacturingConfigurationViewModelPlaceholder"
    )

    class _Cast_GearManufacturingConfigurationViewModelPlaceholder:
        """Special nested class for casting GearManufacturingConfigurationViewModelPlaceholder to subclasses."""

        def __init__(
            self: "GearManufacturingConfigurationViewModelPlaceholder._Cast_GearManufacturingConfigurationViewModelPlaceholder",
            parent: "GearManufacturingConfigurationViewModelPlaceholder",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model(
            self: "GearManufacturingConfigurationViewModelPlaceholder._Cast_GearManufacturingConfigurationViewModelPlaceholder",
        ) -> "_631.GearManufacturingConfigurationViewModel":
            return self._parent._cast(_631.GearManufacturingConfigurationViewModel)

        @property
        def gear_manufacturing_configuration_view_model_placeholder(
            self: "GearManufacturingConfigurationViewModelPlaceholder._Cast_GearManufacturingConfigurationViewModelPlaceholder",
        ) -> "GearManufacturingConfigurationViewModelPlaceholder":
            return self._parent

        def __getattr__(
            self: "GearManufacturingConfigurationViewModelPlaceholder._Cast_GearManufacturingConfigurationViewModelPlaceholder",
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
        self: Self,
        instance_to_wrap: "GearManufacturingConfigurationViewModelPlaceholder.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearManufacturingConfigurationViewModelPlaceholder._Cast_GearManufacturingConfigurationViewModelPlaceholder":
        return self._Cast_GearManufacturingConfigurationViewModelPlaceholder(self)
