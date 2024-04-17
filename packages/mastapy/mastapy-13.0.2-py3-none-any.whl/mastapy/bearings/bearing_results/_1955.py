"""LoadedBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings import _1882
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBearingDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs import _2137
    from mastapy.utility.property import _1845
    from mastapy.bearings.bearing_results import _1956, _1963, _1966
    from mastapy.bearings.bearing_results.rolling import (
        _1999,
        _2006,
        _2014,
        _2030,
        _2053,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedBearingDutyCycle")


class LoadedBearingDutyCycle(_0.APIBase):
    """LoadedBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBearingDutyCycle")

    class _Cast_LoadedBearingDutyCycle:
        """Special nested class for casting LoadedBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
            parent: "LoadedBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_1963.LoadedNonLinearBearingDutyCycleResults":
            from mastapy.bearings.bearing_results import _1963

            return self._parent._cast(_1963.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_1966.LoadedRollingBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedRollingBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_1999.LoadedAxialThrustCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _1999

            return self._parent._cast(
                _1999.LoadedAxialThrustCylindricalRollerBearingDutyCycle
            )

        @property
        def loaded_ball_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_2006.LoadedBallBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(_2006.LoadedBallBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_2014.LoadedCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_2030.LoadedNonBarrelRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "_2053.LoadedTaperRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle",
        ) -> "LoadedBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBearingDutyCycle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def duty_cycle_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ""

        return temp

    @duty_cycle_name.setter
    @enforce_parameter_types
    def duty_cycle_name(self: Self, value: "str"):
        self.wrapped.DutyCycleName = str(value) if value is not None else ""

    @property
    def bearing_design(self: Self) -> "_2137.BearingDesign":
        """mastapy.bearings.bearing_designs.BearingDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def radial_load_summary(
        self: Self,
    ) -> "_1845.DutyCyclePropertySummaryForce[_1882.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummaryForce[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialLoadSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1882.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def z_thrust_reaction_summary(
        self: Self,
    ) -> "_1845.DutyCyclePropertySummaryForce[_1882.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummaryForce[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZThrustReactionSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1882.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def bearing_load_case_results(self: Self) -> "List[_1956.LoadedBearingResults]":
        """List[mastapy.bearings.bearing_results.LoadedBearingResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingLoadCaseResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle":
        return self._Cast_LoadedBearingDutyCycle(self)
