"""CylindricalSetManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SET_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalSetManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _615, _625
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalSetManufacturingConfig",)


Self = TypeVar("Self", bound="CylindricalSetManufacturingConfig")


class CylindricalSetManufacturingConfig(_1237.GearSetImplementationDetail):
    """CylindricalSetManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SET_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalSetManufacturingConfig")

    class _Cast_CylindricalSetManufacturingConfig:
        """Special nested class for casting CylindricalSetManufacturingConfig to subclasses."""

        def __init__(
            self: "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig",
            parent: "CylindricalSetManufacturingConfig",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_detail(
            self: "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig",
        ) -> "_1237.GearSetImplementationDetail":
            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_set_manufacturing_config(
            self: "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig",
        ) -> "CylindricalSetManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig",
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
        self: Self, instance_to_wrap: "CylindricalSetManufacturingConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_manufacturing_configurations(
        self: Self,
    ) -> "List[_615.CylindricalGearManufacturingConfig]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalGearManufacturingConfig]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearManufacturingConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_mesh_manufacturing_configurations(
        self: Self,
    ) -> "List[_625.CylindricalMeshManufacturingConfig]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalMeshManufacturingConfig]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshManufacturingConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def duplicate(self: Self) -> "CylindricalSetManufacturingConfig":
        """mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig"""
        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalSetManufacturingConfig._Cast_CylindricalSetManufacturingConfig":
        return self._Cast_CylindricalSetManufacturingConfig(self)
