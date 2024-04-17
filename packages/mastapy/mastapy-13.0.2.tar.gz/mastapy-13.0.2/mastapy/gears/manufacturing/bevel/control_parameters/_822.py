"""ConicalManufacturingSGTControlParameters"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.bevel.control_parameters import _820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MANUFACTURING_SGT_CONTROL_PARAMETERS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters",
    "ConicalManufacturingSGTControlParameters",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalManufacturingSGTControlParameters",)


Self = TypeVar("Self", bound="ConicalManufacturingSGTControlParameters")


class ConicalManufacturingSGTControlParameters(
    _820.ConicalGearManufacturingControlParameters
):
    """ConicalManufacturingSGTControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_MANUFACTURING_SGT_CONTROL_PARAMETERS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalManufacturingSGTControlParameters"
    )

    class _Cast_ConicalManufacturingSGTControlParameters:
        """Special nested class for casting ConicalManufacturingSGTControlParameters to subclasses."""

        def __init__(
            self: "ConicalManufacturingSGTControlParameters._Cast_ConicalManufacturingSGTControlParameters",
            parent: "ConicalManufacturingSGTControlParameters",
        ):
            self._parent = parent

        @property
        def conical_gear_manufacturing_control_parameters(
            self: "ConicalManufacturingSGTControlParameters._Cast_ConicalManufacturingSGTControlParameters",
        ) -> "_820.ConicalGearManufacturingControlParameters":
            return self._parent._cast(_820.ConicalGearManufacturingControlParameters)

        @property
        def conical_manufacturing_sgt_control_parameters(
            self: "ConicalManufacturingSGTControlParameters._Cast_ConicalManufacturingSGTControlParameters",
        ) -> "ConicalManufacturingSGTControlParameters":
            return self._parent

        def __getattr__(
            self: "ConicalManufacturingSGTControlParameters._Cast_ConicalManufacturingSGTControlParameters",
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
        self: Self, instance_to_wrap: "ConicalManufacturingSGTControlParameters.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_ax(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaAX

        if temp is None:
            return 0.0

        return temp

    @delta_ax.setter
    @enforce_parameter_types
    def delta_ax(self: Self, value: "float"):
        self.wrapped.DeltaAX = float(value) if value is not None else 0.0

    @property
    def delta_gamma_m(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaGammaM

        if temp is None:
            return 0.0

        return temp

    @delta_gamma_m.setter
    @enforce_parameter_types
    def delta_gamma_m(self: Self, value: "float"):
        self.wrapped.DeltaGammaM = float(value) if value is not None else 0.0

    @property
    def delta_gamma_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaGammaX

        if temp is None:
            return 0.0

        return temp

    @delta_gamma_x.setter
    @enforce_parameter_types
    def delta_gamma_x(self: Self, value: "float"):
        self.wrapped.DeltaGammaX = float(value) if value is not None else 0.0

    @property
    def root_angle_of_the_pinion(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootAngleOfThePinion

        if temp is None:
            return 0.0

        return temp

    @root_angle_of_the_pinion.setter
    @enforce_parameter_types
    def root_angle_of_the_pinion(self: Self, value: "float"):
        self.wrapped.RootAngleOfThePinion = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalManufacturingSGTControlParameters._Cast_ConicalManufacturingSGTControlParameters":
        return self._Cast_ConicalManufacturingSGTControlParameters(self)
