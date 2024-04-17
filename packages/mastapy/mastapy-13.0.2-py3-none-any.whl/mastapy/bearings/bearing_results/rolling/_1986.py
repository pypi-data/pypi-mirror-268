"""ISOTR141792001Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTR141792001_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ISOTR141792001Results"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1985, _1987


__docformat__ = "restructuredtext en"
__all__ = ("ISOTR141792001Results",)


Self = TypeVar("Self", bound="ISOTR141792001Results")


class ISOTR141792001Results(_0.APIBase):
    """ISOTR141792001Results

    This is a mastapy class.
    """

    TYPE = _ISOTR141792001_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISOTR141792001Results")

    class _Cast_ISOTR141792001Results:
        """Special nested class for casting ISOTR141792001Results to subclasses."""

        def __init__(
            self: "ISOTR141792001Results._Cast_ISOTR141792001Results",
            parent: "ISOTR141792001Results",
        ):
            self._parent = parent

        @property
        def isotr1417912001_results(
            self: "ISOTR141792001Results._Cast_ISOTR141792001Results",
        ) -> "_1985.ISOTR1417912001Results":
            from mastapy.bearings.bearing_results.rolling import _1985

            return self._parent._cast(_1985.ISOTR1417912001Results)

        @property
        def isotr1417922001_results(
            self: "ISOTR141792001Results._Cast_ISOTR141792001Results",
        ) -> "_1987.ISOTR1417922001Results":
            from mastapy.bearings.bearing_results.rolling import _1987

            return self._parent._cast(_1987.ISOTR1417922001Results)

        @property
        def isotr141792001_results(
            self: "ISOTR141792001Results._Cast_ISOTR141792001Results",
        ) -> "ISOTR141792001Results":
            return self._parent

        def __getattr__(
            self: "ISOTR141792001Results._Cast_ISOTR141792001Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISOTR141792001Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_load_dependent_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialLoadDependentMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_axial_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAxialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_radial_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicRadialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_dependent_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDependentTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def no_load_bearing_resistive_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoLoadBearingResistiveTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def power_rating_f0(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerRatingF0

        if temp is None:
            return 0.0

        return temp

    @property
    def power_rating_f1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerRatingF1

        if temp is None:
            return 0.0

        return temp

    @property
    def static_axial_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticAxialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def static_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def static_radial_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticRadialLoadFactor

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self: Self) -> "ISOTR141792001Results._Cast_ISOTR141792001Results":
        return self._Cast_ISOTR141792001Results(self)
