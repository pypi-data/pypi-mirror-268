"""ScuffingResultsRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCUFFING_RESULTS_ROW = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "ScuffingResultsRow"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _488, _454, _477


__docformat__ = "restructuredtext en"
__all__ = ("ScuffingResultsRow",)


Self = TypeVar("Self", bound="ScuffingResultsRow")


class ScuffingResultsRow(_0.APIBase):
    """ScuffingResultsRow

    This is a mastapy class.
    """

    TYPE = _SCUFFING_RESULTS_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScuffingResultsRow")

    class _Cast_ScuffingResultsRow:
        """Special nested class for casting ScuffingResultsRow to subclasses."""

        def __init__(
            self: "ScuffingResultsRow._Cast_ScuffingResultsRow",
            parent: "ScuffingResultsRow",
        ):
            self._parent = parent

        @property
        def agma_scuffing_results_row(
            self: "ScuffingResultsRow._Cast_ScuffingResultsRow",
        ) -> "_454.AGMAScuffingResultsRow":
            from mastapy.gears.rating.cylindrical import _454

            return self._parent._cast(_454.AGMAScuffingResultsRow)

        @property
        def iso_scuffing_results_row(
            self: "ScuffingResultsRow._Cast_ScuffingResultsRow",
        ) -> "_477.ISOScuffingResultsRow":
            from mastapy.gears.rating.cylindrical import _477

            return self._parent._cast(_477.ISOScuffingResultsRow)

        @property
        def scuffing_results_row(
            self: "ScuffingResultsRow._Cast_ScuffingResultsRow",
        ) -> "ScuffingResultsRow":
            return self._parent

        def __getattr__(self: "ScuffingResultsRow._Cast_ScuffingResultsRow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScuffingResultsRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactTemperature

        if temp is None:
            return 0.0

        return temp

    @contact_temperature.setter
    @enforce_parameter_types
    def contact_temperature(self: Self, value: "float"):
        self.wrapped.ContactTemperature = float(value) if value is not None else 0.0

    @property
    def flash_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlashTemperature

        if temp is None:
            return 0.0

        return temp

    @flash_temperature.setter
    @enforce_parameter_types
    def flash_temperature(self: Self, value: "float"):
        self.wrapped.FlashTemperature = float(value) if value is not None else 0.0

    @property
    def index_label(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IndexLabel

        if temp is None:
            return ""

        return temp

    @property
    def line_of_action_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LineOfActionParameter

        if temp is None:
            return 0.0

        return temp

    @line_of_action_parameter.setter
    @enforce_parameter_types
    def line_of_action_parameter(self: Self, value: "float"):
        self.wrapped.LineOfActionParameter = float(value) if value is not None else 0.0

    @property
    def load_sharing_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @load_sharing_factor.setter
    @enforce_parameter_types
    def load_sharing_factor(self: Self, value: "float"):
        self.wrapped.LoadSharingFactor = float(value) if value is not None else 0.0

    @property
    def normal_relative_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalRelativeRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @normal_relative_radius_of_curvature.setter
    @enforce_parameter_types
    def normal_relative_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.NormalRelativeRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_flank_transverse_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionFlankTransverseRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @pinion_flank_transverse_radius_of_curvature.setter
    @enforce_parameter_types
    def pinion_flank_transverse_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.PinionFlankTransverseRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_rolling_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @pinion_rolling_velocity.setter
    @enforce_parameter_types
    def pinion_rolling_velocity(self: Self, value: "float"):
        self.wrapped.PinionRollingVelocity = float(value) if value is not None else 0.0

    @property
    def sliding_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @sliding_velocity.setter
    @enforce_parameter_types
    def sliding_velocity(self: Self, value: "float"):
        self.wrapped.SlidingVelocity = float(value) if value is not None else 0.0

    @property
    def wheel_flank_transverse_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFlankTransverseRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @wheel_flank_transverse_radius_of_curvature.setter
    @enforce_parameter_types
    def wheel_flank_transverse_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.WheelFlankTransverseRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_rolling_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @wheel_rolling_velocity.setter
    @enforce_parameter_types
    def wheel_rolling_velocity(self: Self, value: "float"):
        self.wrapped.WheelRollingVelocity = float(value) if value is not None else 0.0

    @property
    def pinion(self: Self) -> "_488.ScuffingResultsRowGear":
        """mastapy.gears.rating.cylindrical.ScuffingResultsRowGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Pinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ScuffingResultsRow._Cast_ScuffingResultsRow":
        return self._Cast_ScuffingResultsRow(self)
