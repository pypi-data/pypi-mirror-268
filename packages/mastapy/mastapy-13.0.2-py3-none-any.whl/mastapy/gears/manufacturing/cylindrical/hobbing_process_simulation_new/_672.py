"""HobbingProcessMarkOnShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _669
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_MARK_ON_SHAFT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessMarkOnShaft",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1872
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessMarkOnShaft",)


Self = TypeVar("Self", bound="HobbingProcessMarkOnShaft")


class HobbingProcessMarkOnShaft(_669.HobbingProcessCalculation):
    """HobbingProcessMarkOnShaft

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_MARK_ON_SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessMarkOnShaft")

    class _Cast_HobbingProcessMarkOnShaft:
        """Special nested class for casting HobbingProcessMarkOnShaft to subclasses."""

        def __init__(
            self: "HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft",
            parent: "HobbingProcessMarkOnShaft",
        ):
            self._parent = parent

        @property
        def hobbing_process_calculation(
            self: "HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft",
        ) -> "_669.HobbingProcessCalculation":
            return self._parent._cast(_669.HobbingProcessCalculation)

        @property
        def process_calculation(
            self: "HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft",
        ) -> "_683.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _683,
            )

            return self._parent._cast(_683.ProcessCalculation)

        @property
        def hobbing_process_mark_on_shaft(
            self: "HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft",
        ) -> "HobbingProcessMarkOnShaft":
            return self._parent

        def __getattr__(
            self: "HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobbingProcessMarkOnShaft.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_profile_bands(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    @enforce_parameter_types
    def number_of_profile_bands(self: Self, value: "int"):
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def number_of_transverse_plane(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTransversePlane

        if temp is None:
            return 0

        return temp

    @number_of_transverse_plane.setter
    @enforce_parameter_types
    def number_of_transverse_plane(self: Self, value: "int"):
        self.wrapped.NumberOfTransversePlane = int(value) if value is not None else 0

    @property
    def shaft_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftDiameter

        if temp is None:
            return 0.0

        return temp

    @shaft_diameter.setter
    @enforce_parameter_types
    def shaft_diameter(self: Self, value: "float"):
        self.wrapped.ShaftDiameter = float(value) if value is not None else 0.0

    @property
    def shaft_mark_chart(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftMarkChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft":
        return self._Cast_HobbingProcessMarkOnShaft(self)
