"""CylindricalMeshManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.analysis import _1231
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalMeshManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
        _734,
        _737,
        _738,
    )
    from mastapy.gears.analysis import _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshManufacturingConfig",)


Self = TypeVar("Self", bound="CylindricalMeshManufacturingConfig")


class CylindricalMeshManufacturingConfig(_1231.GearMeshImplementationDetail):
    """CylindricalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMeshManufacturingConfig")

    class _Cast_CylindricalMeshManufacturingConfig:
        """Special nested class for casting CylindricalMeshManufacturingConfig to subclasses."""

        def __init__(
            self: "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig",
            parent: "CylindricalMeshManufacturingConfig",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(
            self: "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig",
        ) -> "_1231.GearMeshImplementationDetail":
            return self._parent._cast(_1231.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig",
        ) -> "CylindricalMeshManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig",
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
        self: Self, instance_to_wrap: "CylindricalMeshManufacturingConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_as_manufactured(self: Self) -> "List[_734.CutterSimulationCalc]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_b_as_manufactured(self: Self) -> "List[_734.CutterSimulationCalc]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshed_gear_a_as_manufactured(
        self: Self,
    ) -> "List[_737.CylindricalManufacturedRealGearInMesh]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalManufacturedRealGearInMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGearAAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshed_gear_a_as_manufactured_virtual(
        self: Self,
    ) -> "List[_738.CylindricalManufacturedVirtualGearInMesh]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalManufacturedVirtualGearInMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGearAAsManufacturedVirtual

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshed_gear_b_as_manufactured(
        self: Self,
    ) -> "List[_737.CylindricalManufacturedRealGearInMesh]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalManufacturedRealGearInMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGearBAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshed_gear_b_as_manufactured_virtual(
        self: Self,
    ) -> "List[_738.CylindricalManufacturedVirtualGearInMesh]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalManufacturedVirtualGearInMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGearBAsManufacturedVirtual

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig":
        return self._Cast_CylindricalMeshManufacturingConfig(self)
