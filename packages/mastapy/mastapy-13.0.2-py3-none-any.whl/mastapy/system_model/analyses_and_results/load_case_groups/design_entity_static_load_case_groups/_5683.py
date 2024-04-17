"""DesignEntityStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups",
    "DesignEntityStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5680,
        _5681,
        _5682,
        _5684,
        _5685,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntityStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="DesignEntityStaticLoadCaseGroup")


class DesignEntityStaticLoadCaseGroup(_0.APIBase):
    """DesignEntityStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntityStaticLoadCaseGroup")

    class _Cast_DesignEntityStaticLoadCaseGroup:
        """Special nested class for casting DesignEntityStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
            parent: "DesignEntityStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def abstract_assembly_static_load_case_group(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
        ) -> "_5680.AbstractAssemblyStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5680,
            )

            return self._parent._cast(_5680.AbstractAssemblyStaticLoadCaseGroup)

        @property
        def component_static_load_case_group(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
        ) -> "_5681.ComponentStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5681,
            )

            return self._parent._cast(_5681.ComponentStaticLoadCaseGroup)

        @property
        def connection_static_load_case_group(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
        ) -> "_5682.ConnectionStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5682,
            )

            return self._parent._cast(_5682.ConnectionStaticLoadCaseGroup)

        @property
        def gear_set_static_load_case_group(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
        ) -> "_5684.GearSetStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5684,
            )

            return self._parent._cast(_5684.GearSetStaticLoadCaseGroup)

        @property
        def part_static_load_case_group(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
        ) -> "_5685.PartStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5685,
            )

            return self._parent._cast(_5685.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
        ) -> "DesignEntityStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntityStaticLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    ) -> "DesignEntityStaticLoadCaseGroup._Cast_DesignEntityStaticLoadCaseGroup":
        return self._Cast_DesignEntityStaticLoadCaseGroup(self)
