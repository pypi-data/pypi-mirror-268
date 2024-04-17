"""RingPinToDiscContactReporting"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PIN_TO_DISC_CONTACT_REPORTING = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "RingPinToDiscContactReporting",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2858,
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2774


__docformat__ = "restructuredtext en"
__all__ = ("RingPinToDiscContactReporting",)


Self = TypeVar("Self", bound="RingPinToDiscContactReporting")


class RingPinToDiscContactReporting(_0.APIBase):
    """RingPinToDiscContactReporting

    This is a mastapy class.
    """

    TYPE = _RING_PIN_TO_DISC_CONTACT_REPORTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinToDiscContactReporting")

    class _Cast_RingPinToDiscContactReporting:
        """Special nested class for casting RingPinToDiscContactReporting to subclasses."""

        def __init__(
            self: "RingPinToDiscContactReporting._Cast_RingPinToDiscContactReporting",
            parent: "RingPinToDiscContactReporting",
        ):
            self._parent = parent

        @property
        def ring_pin_to_disc_contact_reporting(
            self: "RingPinToDiscContactReporting._Cast_RingPinToDiscContactReporting",
        ) -> "RingPinToDiscContactReporting":
            return self._parent

        def __getattr__(
            self: "RingPinToDiscContactReporting._Cast_RingPinToDiscContactReporting",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinToDiscContactReporting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pin_number(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinNumber

        if temp is None:
            return 0

        return temp

    @property
    def pressure_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def contact(self: Self) -> "_2858.SplineFlankContactReporting":
        """mastapy.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Contact

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def information_at_ring_pin_to_disc_contact_point_from_geometry(
        self: Self,
    ) -> "_6918.InformationAtRingPinToDiscContactPointFromGeometry":
        """mastapy.system_model.analyses_and_results.static_loads.InformationAtRingPinToDiscContactPointFromGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InformationAtRingPinToDiscContactPointFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def information_for_contact_points_along_face_width(
        self: Self,
    ) -> "List[_2774.InformationForContactAtPointAlongFaceWidth]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.InformationForContactAtPointAlongFaceWidth]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InformationForContactPointsAlongFaceWidth

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
    def cast_to(
        self: Self,
    ) -> "RingPinToDiscContactReporting._Cast_RingPinToDiscContactReporting":
        return self._Cast_RingPinToDiscContactReporting(self)
