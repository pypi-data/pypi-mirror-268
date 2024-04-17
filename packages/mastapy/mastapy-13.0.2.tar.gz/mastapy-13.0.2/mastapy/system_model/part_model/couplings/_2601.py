"""RigidConnectorToothLocation"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_CONNECTOR_TOOTH_LOCATION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RigidConnectorToothLocation"
)


__docformat__ = "restructuredtext en"
__all__ = ("RigidConnectorToothLocation",)


Self = TypeVar("Self", bound="RigidConnectorToothLocation")


class RigidConnectorToothLocation(_0.APIBase):
    """RigidConnectorToothLocation

    This is a mastapy class.
    """

    TYPE = _RIGID_CONNECTOR_TOOTH_LOCATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RigidConnectorToothLocation")

    class _Cast_RigidConnectorToothLocation:
        """Special nested class for casting RigidConnectorToothLocation to subclasses."""

        def __init__(
            self: "RigidConnectorToothLocation._Cast_RigidConnectorToothLocation",
            parent: "RigidConnectorToothLocation",
        ):
            self._parent = parent

        @property
        def rigid_connector_tooth_location(
            self: "RigidConnectorToothLocation._Cast_RigidConnectorToothLocation",
        ) -> "RigidConnectorToothLocation":
            return self._parent

        def __getattr__(
            self: "RigidConnectorToothLocation._Cast_RigidConnectorToothLocation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RigidConnectorToothLocation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreAngle

        if temp is None:
            return 0.0

        return temp

    @centre_angle.setter
    @enforce_parameter_types
    def centre_angle(self: Self, value: "float"):
        self.wrapped.CentreAngle = float(value) if value is not None else 0.0

    @property
    def end_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndAngle

        if temp is None:
            return 0.0

        return temp

    @end_angle.setter
    @enforce_parameter_types
    def end_angle(self: Self, value: "float"):
        self.wrapped.EndAngle = float(value) if value is not None else 0.0

    @property
    def extent(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Extent

        if temp is None:
            return 0.0

        return temp

    @extent.setter
    @enforce_parameter_types
    def extent(self: Self, value: "float"):
        self.wrapped.Extent = float(value) if value is not None else 0.0

    @property
    def id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

    @property
    def major_diameter_error(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MajorDiameterError

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @major_diameter_error.setter
    @enforce_parameter_types
    def major_diameter_error(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MajorDiameterError = value

    @property
    def major_diameter_radial_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MajorDiameterRadialClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def normal_clearance_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalClearanceLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_clearance_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalClearanceRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_error_left_flank(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchErrorLeftFlank

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_error_left_flank.setter
    @enforce_parameter_types
    def pitch_error_left_flank(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchErrorLeftFlank = value

    @property
    def pitch_error_right_flank(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchErrorRightFlank

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_error_right_flank.setter
    @enforce_parameter_types
    def pitch_error_right_flank(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchErrorRightFlank = value

    @property
    def start_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartAngle

        if temp is None:
            return 0.0

        return temp

    @start_angle.setter
    @enforce_parameter_types
    def start_angle(self: Self, value: "float"):
        self.wrapped.StartAngle = float(value) if value is not None else 0.0

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
    ) -> "RigidConnectorToothLocation._Cast_RigidConnectorToothLocation":
        return self._Cast_RigidConnectorToothLocation(self)
