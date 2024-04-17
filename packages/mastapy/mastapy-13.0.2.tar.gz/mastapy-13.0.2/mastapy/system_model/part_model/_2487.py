"""WindTurbineBladeModeDetails"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WIND_TURBINE_BLADE_MODE_DETAILS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "WindTurbineBladeModeDetails"
)


__docformat__ = "restructuredtext en"
__all__ = ("WindTurbineBladeModeDetails",)


Self = TypeVar("Self", bound="WindTurbineBladeModeDetails")


class WindTurbineBladeModeDetails(_0.APIBase):
    """WindTurbineBladeModeDetails

    This is a mastapy class.
    """

    TYPE = _WIND_TURBINE_BLADE_MODE_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindTurbineBladeModeDetails")

    class _Cast_WindTurbineBladeModeDetails:
        """Special nested class for casting WindTurbineBladeModeDetails to subclasses."""

        def __init__(
            self: "WindTurbineBladeModeDetails._Cast_WindTurbineBladeModeDetails",
            parent: "WindTurbineBladeModeDetails",
        ):
            self._parent = parent

        @property
        def wind_turbine_blade_mode_details(
            self: "WindTurbineBladeModeDetails._Cast_WindTurbineBladeModeDetails",
        ) -> "WindTurbineBladeModeDetails":
            return self._parent

        def __getattr__(
            self: "WindTurbineBladeModeDetails._Cast_WindTurbineBladeModeDetails",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindTurbineBladeModeDetails.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_mode_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstModeFrequency

        if temp is None:
            return 0.0

        return temp

    @first_mode_frequency.setter
    @enforce_parameter_types
    def first_mode_frequency(self: Self, value: "float"):
        self.wrapped.FirstModeFrequency = float(value) if value is not None else 0.0

    @property
    def include_mode(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeMode

        if temp is None:
            return False

        return temp

    @include_mode.setter
    @enforce_parameter_types
    def include_mode(self: Self, value: "bool"):
        self.wrapped.IncludeMode = bool(value) if value is not None else False

    @property
    def inertia_of_centre(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaOfCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def inertia_of_hub(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaOfHub

        if temp is None:
            return 0.0

        return temp

    @property
    def inertia_of_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaOfTip

        if temp is None:
            return 0.0

        return temp

    @property
    def second_mode_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SecondModeFrequency

        if temp is None:
            return 0.0

        return temp

    @second_mode_frequency.setter
    @enforce_parameter_types
    def second_mode_frequency(self: Self, value: "float"):
        self.wrapped.SecondModeFrequency = float(value) if value is not None else 0.0

    @property
    def stiffness_centre_to_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessCentreToTip

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_hub_to_centre(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessHubToCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "WindTurbineBladeModeDetails._Cast_WindTurbineBladeModeDetails":
        return self._Cast_WindTurbineBladeModeDetails(self)
