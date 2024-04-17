"""WormGrindingProcessGearShape"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_GEAR_SHAPE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessGearShape",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessGearShape",)


Self = TypeVar("Self", bound="WormGrindingProcessGearShape")


class WormGrindingProcessGearShape(_697.WormGrindingProcessCalculation):
    """WormGrindingProcessGearShape

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_GEAR_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingProcessGearShape")

    class _Cast_WormGrindingProcessGearShape:
        """Special nested class for casting WormGrindingProcessGearShape to subclasses."""

        def __init__(
            self: "WormGrindingProcessGearShape._Cast_WormGrindingProcessGearShape",
            parent: "WormGrindingProcessGearShape",
        ):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingProcessGearShape._Cast_WormGrindingProcessGearShape",
        ) -> "_697.WormGrindingProcessCalculation":
            return self._parent._cast(_697.WormGrindingProcessCalculation)

        @property
        def process_calculation(
            self: "WormGrindingProcessGearShape._Cast_WormGrindingProcessGearShape",
        ) -> "_683.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _683,
            )

            return self._parent._cast(_683.ProcessCalculation)

        @property
        def worm_grinding_process_gear_shape(
            self: "WormGrindingProcessGearShape._Cast_WormGrindingProcessGearShape",
        ) -> "WormGrindingProcessGearShape":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessGearShape._Cast_WormGrindingProcessGearShape",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrindingProcessGearShape.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_tooth_shape_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearToothShapeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_gear_shape_bands(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfGearShapeBands

        if temp is None:
            return 0

        return temp

    @number_of_gear_shape_bands.setter
    @enforce_parameter_types
    def number_of_gear_shape_bands(self: Self, value: "int"):
        self.wrapped.NumberOfGearShapeBands = int(value) if value is not None else 0

    @property
    def result_z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResultZPlane

        if temp is None:
            return 0.0

        return temp

    @result_z_plane.setter
    @enforce_parameter_types
    def result_z_plane(self: Self, value: "float"):
        self.wrapped.ResultZPlane = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessGearShape._Cast_WormGrindingProcessGearShape":
        return self._Cast_WormGrindingProcessGearShape(self)
