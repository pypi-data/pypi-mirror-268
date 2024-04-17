"""ConicalManufacturingSGMControlParameters"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.bevel.control_parameters import _820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MANUFACTURING_SGM_CONTROL_PARAMETERS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters",
    "ConicalManufacturingSGMControlParameters",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalManufacturingSGMControlParameters",)


Self = TypeVar("Self", bound="ConicalManufacturingSGMControlParameters")


class ConicalManufacturingSGMControlParameters(
    _820.ConicalGearManufacturingControlParameters
):
    """ConicalManufacturingSGMControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_MANUFACTURING_SGM_CONTROL_PARAMETERS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalManufacturingSGMControlParameters"
    )

    class _Cast_ConicalManufacturingSGMControlParameters:
        """Special nested class for casting ConicalManufacturingSGMControlParameters to subclasses."""

        def __init__(
            self: "ConicalManufacturingSGMControlParameters._Cast_ConicalManufacturingSGMControlParameters",
            parent: "ConicalManufacturingSGMControlParameters",
        ):
            self._parent = parent

        @property
        def conical_gear_manufacturing_control_parameters(
            self: "ConicalManufacturingSGMControlParameters._Cast_ConicalManufacturingSGMControlParameters",
        ) -> "_820.ConicalGearManufacturingControlParameters":
            return self._parent._cast(_820.ConicalGearManufacturingControlParameters)

        @property
        def conical_manufacturing_sgm_control_parameters(
            self: "ConicalManufacturingSGMControlParameters._Cast_ConicalManufacturingSGMControlParameters",
        ) -> "ConicalManufacturingSGMControlParameters":
            return self._parent

        def __getattr__(
            self: "ConicalManufacturingSGMControlParameters._Cast_ConicalManufacturingSGMControlParameters",
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
        self: Self, instance_to_wrap: "ConicalManufacturingSGMControlParameters.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_gamma(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaGamma

        if temp is None:
            return 0.0

        return temp

    @delta_gamma.setter
    @enforce_parameter_types
    def delta_gamma(self: Self, value: "float"):
        self.wrapped.DeltaGamma = float(value) if value is not None else 0.0

    @property
    def profile_mismatch_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileMismatchFactor

        if temp is None:
            return 0.0

        return temp

    @profile_mismatch_factor.setter
    @enforce_parameter_types
    def profile_mismatch_factor(self: Self, value: "float"):
        self.wrapped.ProfileMismatchFactor = float(value) if value is not None else 0.0

    @property
    def work_head_offset_change(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WorkHeadOffsetChange

        if temp is None:
            return 0.0

        return temp

    @work_head_offset_change.setter
    @enforce_parameter_types
    def work_head_offset_change(self: Self, value: "float"):
        self.wrapped.WorkHeadOffsetChange = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalManufacturingSGMControlParameters._Cast_ConicalManufacturingSGMControlParameters":
        return self._Cast_ConicalManufacturingSGMControlParameters(self)
