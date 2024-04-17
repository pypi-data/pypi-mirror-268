"""ConicalGearManufactureError"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6900
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConicalGearManufactureError",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearManufactureError",)


Self = TypeVar("Self", bound="ConicalGearManufactureError")


class ConicalGearManufactureError(_6900.GearManufactureError):
    """ConicalGearManufactureError

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearManufactureError")

    class _Cast_ConicalGearManufactureError:
        """Special nested class for casting ConicalGearManufactureError to subclasses."""

        def __init__(
            self: "ConicalGearManufactureError._Cast_ConicalGearManufactureError",
            parent: "ConicalGearManufactureError",
        ):
            self._parent = parent

        @property
        def gear_manufacture_error(
            self: "ConicalGearManufactureError._Cast_ConicalGearManufactureError",
        ) -> "_6900.GearManufactureError":
            return self._parent._cast(_6900.GearManufactureError)

        @property
        def conical_gear_manufacture_error(
            self: "ConicalGearManufactureError._Cast_ConicalGearManufactureError",
        ) -> "ConicalGearManufactureError":
            return self._parent

        def __getattr__(
            self: "ConicalGearManufactureError._Cast_ConicalGearManufactureError",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pitch_error_phase_shift_on_concave_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchErrorPhaseShiftOnConcaveFlank

        if temp is None:
            return 0.0

        return temp

    @pitch_error_phase_shift_on_concave_flank.setter
    @enforce_parameter_types
    def pitch_error_phase_shift_on_concave_flank(self: Self, value: "float"):
        self.wrapped.PitchErrorPhaseShiftOnConcaveFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_error_phase_shift_on_convex_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchErrorPhaseShiftOnConvexFlank

        if temp is None:
            return 0.0

        return temp

    @pitch_error_phase_shift_on_convex_flank.setter
    @enforce_parameter_types
    def pitch_error_phase_shift_on_convex_flank(self: Self, value: "float"):
        self.wrapped.PitchErrorPhaseShiftOnConvexFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_errors_concave_flank(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.PitchErrorsConcaveFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @pitch_errors_concave_flank.setter
    @enforce_parameter_types
    def pitch_errors_concave_flank(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.PitchErrorsConcaveFlank = value.wrapped

    @property
    def pitch_errors_convex_flank(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.PitchErrorsConvexFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @pitch_errors_convex_flank.setter
    @enforce_parameter_types
    def pitch_errors_convex_flank(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.PitchErrorsConvexFlank = value.wrapped

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearManufactureError._Cast_ConicalGearManufactureError":
        return self._Cast_ConicalGearManufactureError(self)
