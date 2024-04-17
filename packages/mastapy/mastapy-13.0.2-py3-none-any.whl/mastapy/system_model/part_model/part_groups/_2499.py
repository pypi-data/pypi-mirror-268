"""PartGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.PartGroups", "PartGroup"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.part_model.part_groups import _2493, _2494, _2497, _2498


__docformat__ = "restructuredtext en"
__all__ = ("PartGroup",)


Self = TypeVar("Self", bound="PartGroup")


class PartGroup(_0.APIBase):
    """PartGroup

    This is a mastapy class.
    """

    TYPE = _PART_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartGroup")

    class _Cast_PartGroup:
        """Special nested class for casting PartGroup to subclasses."""

        def __init__(self: "PartGroup._Cast_PartGroup", parent: "PartGroup"):
            self._parent = parent

        @property
        def concentric_or_parallel_part_group(
            self: "PartGroup._Cast_PartGroup",
        ) -> "_2493.ConcentricOrParallelPartGroup":
            from mastapy.system_model.part_model.part_groups import _2493

            return self._parent._cast(_2493.ConcentricOrParallelPartGroup)

        @property
        def concentric_part_group(
            self: "PartGroup._Cast_PartGroup",
        ) -> "_2494.ConcentricPartGroup":
            from mastapy.system_model.part_model.part_groups import _2494

            return self._parent._cast(_2494.ConcentricPartGroup)

        @property
        def parallel_part_group(
            self: "PartGroup._Cast_PartGroup",
        ) -> "_2497.ParallelPartGroup":
            from mastapy.system_model.part_model.part_groups import _2497

            return self._parent._cast(_2497.ParallelPartGroup)

        @property
        def parallel_part_group_selection(
            self: "PartGroup._Cast_PartGroup",
        ) -> "_2498.ParallelPartGroupSelection":
            from mastapy.system_model.part_model.part_groups import _2498

            return self._parent._cast(_2498.ParallelPartGroupSelection)

        @property
        def part_group(self: "PartGroup._Cast_PartGroup") -> "PartGroup":
            return self._parent

        def __getattr__(self: "PartGroup._Cast_PartGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def parts(self: Self) -> "List[_2475.Part]":
        """List[mastapy.system_model.part_model.Part]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Parts

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
    def cast_to(self: Self) -> "PartGroup._Cast_PartGroup":
        return self._Cast_PartGroup(self)
