"""LinearDQModel"""

from __future__ import annotations

from typing import TypeVar

from mastapy.electric_machines.results import _1330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_DQ_MODEL = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "LinearDQModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearDQModel",)


Self = TypeVar("Self", bound="LinearDQModel")


class LinearDQModel(_1330.ElectricMachineDQModel):
    """LinearDQModel

    This is a mastapy class.
    """

    TYPE = _LINEAR_DQ_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearDQModel")

    class _Cast_LinearDQModel:
        """Special nested class for casting LinearDQModel to subclasses."""

        def __init__(
            self: "LinearDQModel._Cast_LinearDQModel", parent: "LinearDQModel"
        ):
            self._parent = parent

        @property
        def electric_machine_dq_model(
            self: "LinearDQModel._Cast_LinearDQModel",
        ) -> "_1330.ElectricMachineDQModel":
            return self._parent._cast(_1330.ElectricMachineDQModel)

        @property
        def linear_dq_model(
            self: "LinearDQModel._Cast_LinearDQModel",
        ) -> "LinearDQModel":
            return self._parent

        def __getattr__(self: "LinearDQModel._Cast_LinearDQModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearDQModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apparent_d_axis_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentDAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_q_axis_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentQAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def base_speed_from_mtpa_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseSpeedFromMTPAAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def max_speed_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxSpeedAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "LinearDQModel._Cast_LinearDQModel":
        return self._Cast_LinearDQModel(self)
