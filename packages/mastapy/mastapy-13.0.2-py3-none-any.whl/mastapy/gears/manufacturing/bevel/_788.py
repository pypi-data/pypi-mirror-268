"""ConicalMeshManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _790
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _791, _797
    from mastapy.gears.analysis import _1231, _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalMeshManufacturingConfig")


class ConicalMeshManufacturingConfig(_790.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshManufacturingConfig")

    class _Cast_ConicalMeshManufacturingConfig:
        """Special nested class for casting ConicalMeshManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
            parent: "ConicalMeshManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_790.ConicalMeshMicroGeometryConfigBase":
            return self._parent._cast(_790.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_implementation_detail(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_1231.GearMeshImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
        ) -> "ConicalMeshManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshManufacturingConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_config(self: Self) -> "_791.ConicalPinionManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalPinionManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_config(self: Self) -> "_797.ConicalWheelManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalWheelManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig":
        return self._Cast_ConicalMeshManufacturingConfig(self)
