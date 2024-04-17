"""RepositionComponentDetails"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REPOSITION_COMPONENT_DETAILS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "RepositionComponentDetails"
)


__docformat__ = "restructuredtext en"
__all__ = ("RepositionComponentDetails",)


Self = TypeVar("Self", bound="RepositionComponentDetails")


class RepositionComponentDetails(_0.APIBase):
    """RepositionComponentDetails

    This is a mastapy class.
    """

    TYPE = _REPOSITION_COMPONENT_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RepositionComponentDetails")

    class _Cast_RepositionComponentDetails:
        """Special nested class for casting RepositionComponentDetails to subclasses."""

        def __init__(
            self: "RepositionComponentDetails._Cast_RepositionComponentDetails",
            parent: "RepositionComponentDetails",
        ):
            self._parent = parent

        @property
        def reposition_component_details(
            self: "RepositionComponentDetails._Cast_RepositionComponentDetails",
        ) -> "RepositionComponentDetails":
            return self._parent

        def __getattr__(
            self: "RepositionComponentDetails._Cast_RepositionComponentDetails",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RepositionComponentDetails.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def only_move_concentric_components(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OnlyMoveConcentricComponents

        if temp is None:
            return False

        return temp

    @only_move_concentric_components.setter
    @enforce_parameter_types
    def only_move_concentric_components(self: Self, value: "bool"):
        self.wrapped.OnlyMoveConcentricComponents = (
            bool(value) if value is not None else False
        )

    @property
    def reverse_axis_direction(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReverseAxisDirection

        if temp is None:
            return False

        return temp

    @reverse_axis_direction.setter
    @enforce_parameter_types
    def reverse_axis_direction(self: Self, value: "bool"):
        self.wrapped.ReverseAxisDirection = bool(value) if value is not None else False

    @property
    def direction(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Direction

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @direction.setter
    @enforce_parameter_types
    def direction(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Direction = value

    @property
    def origin(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Origin

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @origin.setter
    @enforce_parameter_types
    def origin(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Origin = value

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
    ) -> "RepositionComponentDetails._Cast_RepositionComponentDetails":
        return self._Cast_RepositionComponentDetails(self)
