"""WindTurbineSingleBladeDetails"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WIND_TURBINE_SINGLE_BLADE_DETAILS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "WindTurbineSingleBladeDetails"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2487


__docformat__ = "restructuredtext en"
__all__ = ("WindTurbineSingleBladeDetails",)


Self = TypeVar("Self", bound="WindTurbineSingleBladeDetails")


class WindTurbineSingleBladeDetails(_0.APIBase):
    """WindTurbineSingleBladeDetails

    This is a mastapy class.
    """

    TYPE = _WIND_TURBINE_SINGLE_BLADE_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindTurbineSingleBladeDetails")

    class _Cast_WindTurbineSingleBladeDetails:
        """Special nested class for casting WindTurbineSingleBladeDetails to subclasses."""

        def __init__(
            self: "WindTurbineSingleBladeDetails._Cast_WindTurbineSingleBladeDetails",
            parent: "WindTurbineSingleBladeDetails",
        ):
            self._parent = parent

        @property
        def wind_turbine_single_blade_details(
            self: "WindTurbineSingleBladeDetails._Cast_WindTurbineSingleBladeDetails",
        ) -> "WindTurbineSingleBladeDetails":
            return self._parent

        def __getattr__(
            self: "WindTurbineSingleBladeDetails._Cast_WindTurbineSingleBladeDetails",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindTurbineSingleBladeDetails.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def blade_drawing_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BladeDrawingLength

        if temp is None:
            return 0.0

        return temp

    @blade_drawing_length.setter
    @enforce_parameter_types
    def blade_drawing_length(self: Self, value: "float"):
        self.wrapped.BladeDrawingLength = float(value) if value is not None else 0.0

    @property
    def blade_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BladeLength

        if temp is None:
            return 0.0

        return temp

    @blade_length.setter
    @enforce_parameter_types
    def blade_length(self: Self, value: "float"):
        self.wrapped.BladeLength = float(value) if value is not None else 0.0

    @property
    def blade_mass(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BladeMass

        if temp is None:
            return 0.0

        return temp

    @blade_mass.setter
    @enforce_parameter_types
    def blade_mass(self: Self, value: "float"):
        self.wrapped.BladeMass = float(value) if value is not None else 0.0

    @property
    def mass_moment_of_inertia_about_hub(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MassMomentOfInertiaAboutHub

        if temp is None:
            return 0.0

        return temp

    @mass_moment_of_inertia_about_hub.setter
    @enforce_parameter_types
    def mass_moment_of_inertia_about_hub(self: Self, value: "float"):
        self.wrapped.MassMomentOfInertiaAboutHub = (
            float(value) if value is not None else 0.0
        )

    @property
    def scale_blade_drawing_to_blade_drawing_length(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ScaleBladeDrawingToBladeDrawingLength

        if temp is None:
            return False

        return temp

    @scale_blade_drawing_to_blade_drawing_length.setter
    @enforce_parameter_types
    def scale_blade_drawing_to_blade_drawing_length(self: Self, value: "bool"):
        self.wrapped.ScaleBladeDrawingToBladeDrawingLength = (
            bool(value) if value is not None else False
        )

    @property
    def edgewise_modes(self: Self) -> "_2487.WindTurbineBladeModeDetails":
        """mastapy.system_model.part_model.WindTurbineBladeModeDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EdgewiseModes

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def flapwise_modes(self: Self) -> "_2487.WindTurbineBladeModeDetails":
        """mastapy.system_model.part_model.WindTurbineBladeModeDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlapwiseModes

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WindTurbineSingleBladeDetails._Cast_WindTurbineSingleBladeDetails":
        return self._Cast_WindTurbineSingleBladeDetails(self)
