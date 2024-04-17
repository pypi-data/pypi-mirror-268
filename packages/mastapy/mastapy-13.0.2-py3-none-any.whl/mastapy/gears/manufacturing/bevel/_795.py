"""ConicalSetMicroGeometryConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.bevel import _796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalSetMicroGeometryConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _780, _789
    from mastapy.gears.analysis import _1237, _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("ConicalSetMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalSetMicroGeometryConfig")


class ConicalSetMicroGeometryConfig(_796.ConicalSetMicroGeometryConfigBase):
    """ConicalSetMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalSetMicroGeometryConfig")

    class _Cast_ConicalSetMicroGeometryConfig:
        """Special nested class for casting ConicalSetMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
            parent: "ConicalSetMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_set_micro_geometry_config_base(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
        ) -> "_796.ConicalSetMicroGeometryConfigBase":
            return self._parent._cast(_796.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_implementation_detail(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
        ) -> "_1237.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1237

            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def conical_set_micro_geometry_config(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
        ) -> "ConicalSetMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalSetMicroGeometryConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_micro_geometry_configuration(
        self: Self,
    ) -> "List[_780.ConicalGearMicroGeometryConfig]":
        """List[mastapy.gears.manufacturing.bevel.ConicalGearMicroGeometryConfig]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMicroGeometryConfiguration

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes(self: Self) -> "List[_789.ConicalMeshMicroGeometryConfig]":
        """List[mastapy.gears.manufacturing.bevel.ConicalMeshMicroGeometryConfig]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def duplicate(self: Self) -> "ConicalSetMicroGeometryConfig":
        """mastapy.gears.manufacturing.bevel.ConicalSetMicroGeometryConfig"""
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
    ) -> "ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig":
        return self._Cast_ConicalSetMicroGeometryConfig(self)
