"""ConicalMeshFlankManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshFlankManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel.control_parameters import _820
    from mastapy.gears.manufacturing.bevel.basic_machine_settings import _827, _826


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshFlankManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalMeshFlankManufacturingConfig")


class ConicalMeshFlankManufacturingConfig(_785.ConicalMeshFlankMicroGeometryConfig):
    """ConicalMeshFlankManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshFlankManufacturingConfig")

    class _Cast_ConicalMeshFlankManufacturingConfig:
        """Special nested class for casting ConicalMeshFlankManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalMeshFlankManufacturingConfig._Cast_ConicalMeshFlankManufacturingConfig",
            parent: "ConicalMeshFlankManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_mesh_flank_micro_geometry_config(
            self: "ConicalMeshFlankManufacturingConfig._Cast_ConicalMeshFlankManufacturingConfig",
        ) -> "_785.ConicalMeshFlankMicroGeometryConfig":
            return self._parent._cast(_785.ConicalMeshFlankMicroGeometryConfig)

        @property
        def conical_mesh_flank_manufacturing_config(
            self: "ConicalMeshFlankManufacturingConfig._Cast_ConicalMeshFlankManufacturingConfig",
        ) -> "ConicalMeshFlankManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshFlankManufacturingConfig._Cast_ConicalMeshFlankManufacturingConfig",
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
        self: Self, instance_to_wrap: "ConicalMeshFlankManufacturingConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_parameters(
        self: Self,
    ) -> "_820.ConicalGearManufacturingControlParameters":
        """mastapy.gears.manufacturing.bevel.control_parameters.ConicalGearManufacturingControlParameters

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ControlParameters

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specified_cradle_style_machine_settings(
        self: Self,
    ) -> "_827.CradleStyleConicalMachineSettingsGenerated":
        """mastapy.gears.manufacturing.bevel.basic_machine_settings.CradleStyleConicalMachineSettingsGenerated

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedCradleStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specified_phoenix_style_machine_settings(
        self: Self,
    ) -> "_826.BasicConicalGearMachineSettingsGenerated":
        """mastapy.gears.manufacturing.bevel.basic_machine_settings.BasicConicalGearMachineSettingsGenerated

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedPhoenixStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalMeshFlankManufacturingConfig._Cast_ConicalMeshFlankManufacturingConfig"
    ):
        return self._Cast_ConicalMeshFlankManufacturingConfig(self)
