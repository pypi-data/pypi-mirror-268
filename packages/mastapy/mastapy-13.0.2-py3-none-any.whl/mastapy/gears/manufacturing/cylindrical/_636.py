"""MicroGeometryInputs"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "MicroGeometryInputs"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _639, _637, _638


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryInputs",)


Self = TypeVar("Self", bound="MicroGeometryInputs")
T = TypeVar("T", bound="_639.ModificationSegment")


class MicroGeometryInputs(_0.APIBase, Generic[T]):
    """MicroGeometryInputs

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MICRO_GEOMETRY_INPUTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MicroGeometryInputs")

    class _Cast_MicroGeometryInputs:
        """Special nested class for casting MicroGeometryInputs to subclasses."""

        def __init__(
            self: "MicroGeometryInputs._Cast_MicroGeometryInputs",
            parent: "MicroGeometryInputs",
        ):
            self._parent = parent

        @property
        def micro_geometry_inputs_lead(
            self: "MicroGeometryInputs._Cast_MicroGeometryInputs",
        ) -> "_637.MicroGeometryInputsLead":
            from mastapy.gears.manufacturing.cylindrical import _637

            return self._parent._cast(_637.MicroGeometryInputsLead)

        @property
        def micro_geometry_inputs_profile(
            self: "MicroGeometryInputs._Cast_MicroGeometryInputs",
        ) -> "_638.MicroGeometryInputsProfile":
            from mastapy.gears.manufacturing.cylindrical import _638

            return self._parent._cast(_638.MicroGeometryInputsProfile)

        @property
        def micro_geometry_inputs(
            self: "MicroGeometryInputs._Cast_MicroGeometryInputs",
        ) -> "MicroGeometryInputs":
            return self._parent

        def __getattr__(
            self: "MicroGeometryInputs._Cast_MicroGeometryInputs", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MicroGeometryInputs.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def modification_at_starting_point(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModificationAtStartingPoint

        if temp is None:
            return 0.0

        return temp

    @modification_at_starting_point.setter
    @enforce_parameter_types
    def modification_at_starting_point(self: Self, value: "float"):
        self.wrapped.ModificationAtStartingPoint = (
            float(value) if value is not None else 0.0
        )

    @property
    def micro_geometry_segments(self: Self) -> "List[T]":
        """List[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometrySegments

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
    def cast_to(self: Self) -> "MicroGeometryInputs._Cast_MicroGeometryInputs":
        return self._Cast_MicroGeometryInputs(self)
