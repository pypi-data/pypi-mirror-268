"""ConicalManufacturingSMTControlParameters"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.bevel.control_parameters import _820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MANUFACTURING_SMT_CONTROL_PARAMETERS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters",
    "ConicalManufacturingSMTControlParameters",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalManufacturingSMTControlParameters",)


Self = TypeVar("Self", bound="ConicalManufacturingSMTControlParameters")


class ConicalManufacturingSMTControlParameters(
    _820.ConicalGearManufacturingControlParameters
):
    """ConicalManufacturingSMTControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_MANUFACTURING_SMT_CONTROL_PARAMETERS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalManufacturingSMTControlParameters"
    )

    class _Cast_ConicalManufacturingSMTControlParameters:
        """Special nested class for casting ConicalManufacturingSMTControlParameters to subclasses."""

        def __init__(
            self: "ConicalManufacturingSMTControlParameters._Cast_ConicalManufacturingSMTControlParameters",
            parent: "ConicalManufacturingSMTControlParameters",
        ):
            self._parent = parent

        @property
        def conical_gear_manufacturing_control_parameters(
            self: "ConicalManufacturingSMTControlParameters._Cast_ConicalManufacturingSMTControlParameters",
        ) -> "_820.ConicalGearManufacturingControlParameters":
            return self._parent._cast(_820.ConicalGearManufacturingControlParameters)

        @property
        def conical_manufacturing_smt_control_parameters(
            self: "ConicalManufacturingSMTControlParameters._Cast_ConicalManufacturingSMTControlParameters",
        ) -> "ConicalManufacturingSMTControlParameters":
            return self._parent

        def __getattr__(
            self: "ConicalManufacturingSMTControlParameters._Cast_ConicalManufacturingSMTControlParameters",
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
        self: Self, instance_to_wrap: "ConicalManufacturingSMTControlParameters.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_acceleration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngularAcceleration

        if temp is None:
            return 0.0

        return temp

    @angular_acceleration.setter
    @enforce_parameter_types
    def angular_acceleration(self: Self, value: "float"):
        self.wrapped.AngularAcceleration = float(value) if value is not None else 0.0

    @property
    def clearance_between_finish_root_and_rough_root(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClearanceBetweenFinishRootAndRoughRoot

        if temp is None:
            return 0.0

        return temp

    @clearance_between_finish_root_and_rough_root.setter
    @enforce_parameter_types
    def clearance_between_finish_root_and_rough_root(self: Self, value: "float"):
        self.wrapped.ClearanceBetweenFinishRootAndRoughRoot = (
            float(value) if value is not None else 0.0
        )

    @property
    def delta_e(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaE

        if temp is None:
            return 0.0

        return temp

    @delta_e.setter
    @enforce_parameter_types
    def delta_e(self: Self, value: "float"):
        self.wrapped.DeltaE = float(value) if value is not None else 0.0

    @property
    def delta_sigma(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaSigma

        if temp is None:
            return 0.0

        return temp

    @delta_sigma.setter
    @enforce_parameter_types
    def delta_sigma(self: Self, value: "float"):
        self.wrapped.DeltaSigma = float(value) if value is not None else 0.0

    @property
    def delta_xp(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaXP

        if temp is None:
            return 0.0

        return temp

    @delta_xp.setter
    @enforce_parameter_types
    def delta_xp(self: Self, value: "float"):
        self.wrapped.DeltaXP = float(value) if value is not None else 0.0

    @property
    def delta_xw(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaXW

        if temp is None:
            return 0.0

        return temp

    @delta_xw.setter
    @enforce_parameter_types
    def delta_xw(self: Self, value: "float"):
        self.wrapped.DeltaXW = float(value) if value is not None else 0.0

    @property
    def direction_angle_of_poc(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DirectionAngleOfPOC

        if temp is None:
            return 0.0

        return temp

    @direction_angle_of_poc.setter
    @enforce_parameter_types
    def direction_angle_of_poc(self: Self, value: "float"):
        self.wrapped.DirectionAngleOfPOC = float(value) if value is not None else 0.0

    @property
    def initial_workhead_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialWorkheadOffset

        if temp is None:
            return 0.0

        return temp

    @initial_workhead_offset.setter
    @enforce_parameter_types
    def initial_workhead_offset(self: Self, value: "float"):
        self.wrapped.InitialWorkheadOffset = float(value) if value is not None else 0.0

    @property
    def mean_contact_point_h(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanContactPointH

        if temp is None:
            return 0.0

        return temp

    @mean_contact_point_h.setter
    @enforce_parameter_types
    def mean_contact_point_h(self: Self, value: "float"):
        self.wrapped.MeanContactPointH = float(value) if value is not None else 0.0

    @property
    def mean_contact_point_v(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanContactPointV

        if temp is None:
            return 0.0

        return temp

    @mean_contact_point_v.setter
    @enforce_parameter_types
    def mean_contact_point_v(self: Self, value: "float"):
        self.wrapped.MeanContactPointV = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalManufacturingSMTControlParameters._Cast_ConicalManufacturingSMTControlParameters":
        return self._Cast_ConicalManufacturingSMTControlParameters(self)
