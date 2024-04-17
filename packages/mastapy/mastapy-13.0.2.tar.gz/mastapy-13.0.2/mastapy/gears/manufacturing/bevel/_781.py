"""ConicalGearMicroGeometryConfigBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _799, _779, _780, _791, _792, _797
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMicroGeometryConfigBase",)


Self = TypeVar("Self", bound="ConicalGearMicroGeometryConfigBase")


class ConicalGearMicroGeometryConfigBase(_1227.GearImplementationDetail):
    """ConicalGearMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMicroGeometryConfigBase")

    class _Cast_ConicalGearMicroGeometryConfigBase:
        """Special nested class for casting ConicalGearMicroGeometryConfigBase to subclasses."""

        def __init__(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
            parent: "ConicalGearMicroGeometryConfigBase",
        ):
            self._parent = parent

        @property
        def gear_implementation_detail(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_1227.GearImplementationDetail":
            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_779.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _779

            return self._parent._cast(_779.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_780.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _780

            return self._parent._cast(_780.ConicalGearMicroGeometryConfig)

        @property
        def conical_pinion_manufacturing_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_791.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_792.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "_797.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "ConicalGearMicroGeometryConfigBase":
            return self._parent

        def __getattr__(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
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
        self: Self, instance_to_wrap: "ConicalGearMicroGeometryConfigBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_measurement_border(self: Self) -> "_799.FlankMeasurementBorder":
        """mastapy.gears.manufacturing.bevel.FlankMeasurementBorder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase":
        return self._Cast_ConicalGearMicroGeometryConfigBase(self)
