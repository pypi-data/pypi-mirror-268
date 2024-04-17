"""HobbingProcessSimulationInput"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _661,
    _688,
)
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_INPUT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessSimulationInput",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _679,
        _680,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessSimulationInput",)


Self = TypeVar("Self", bound="HobbingProcessSimulationInput")


class HobbingProcessSimulationInput(_688.ProcessSimulationInput):
    """HobbingProcessSimulationInput

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_INPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessSimulationInput")

    class _Cast_HobbingProcessSimulationInput:
        """Special nested class for casting HobbingProcessSimulationInput to subclasses."""

        def __init__(
            self: "HobbingProcessSimulationInput._Cast_HobbingProcessSimulationInput",
            parent: "HobbingProcessSimulationInput",
        ):
            self._parent = parent

        @property
        def process_simulation_input(
            self: "HobbingProcessSimulationInput._Cast_HobbingProcessSimulationInput",
        ) -> "_688.ProcessSimulationInput":
            return self._parent._cast(_688.ProcessSimulationInput)

        @property
        def hobbing_process_simulation_input(
            self: "HobbingProcessSimulationInput._Cast_HobbingProcessSimulationInput",
        ) -> "HobbingProcessSimulationInput":
            return self._parent

        def __getattr__(
            self: "HobbingProcessSimulationInput._Cast_HobbingProcessSimulationInput",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobbingProcessSimulationInput.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def process_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ActiveProcessMethod":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ActiveProcessMethod]"""
        temp = self.wrapped.ProcessMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ActiveProcessMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @process_method.setter
    @enforce_parameter_types
    def process_method(self: Self, value: "_661.ActiveProcessMethod"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ActiveProcessMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ProcessMethod = value

    @property
    def hob_manufacture_error(self: Self) -> "_679.HobManufactureError":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobManufactureError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hob_resharpening_error(self: Self) -> "_680.HobResharpeningError":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobResharpeningError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobResharpeningError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessSimulationInput._Cast_HobbingProcessSimulationInput":
        return self._Cast_HobbingProcessSimulationInput(self)
