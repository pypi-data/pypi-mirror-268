"""CylindricalMeshedGearFlankSystemDeflection"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR_FLANK_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalMeshedGearFlankSystemDeflection",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshedGearFlankSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalMeshedGearFlankSystemDeflection")


class CylindricalMeshedGearFlankSystemDeflection(_0.APIBase):
    """CylindricalMeshedGearFlankSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR_FLANK_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalMeshedGearFlankSystemDeflection"
    )

    class _Cast_CylindricalMeshedGearFlankSystemDeflection:
        """Special nested class for casting CylindricalMeshedGearFlankSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalMeshedGearFlankSystemDeflection._Cast_CylindricalMeshedGearFlankSystemDeflection",
            parent: "CylindricalMeshedGearFlankSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_meshed_gear_flank_system_deflection(
            self: "CylindricalMeshedGearFlankSystemDeflection._Cast_CylindricalMeshedGearFlankSystemDeflection",
        ) -> "CylindricalMeshedGearFlankSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshedGearFlankSystemDeflection._Cast_CylindricalMeshedGearFlankSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalMeshedGearFlankSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_clearance_from_form_diameter_to_sap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumClearanceFromFormDiameterToSAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_eap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingEAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_sap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingSAPDiameter

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
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshedGearFlankSystemDeflection._Cast_CylindricalMeshedGearFlankSystemDeflection":
        return self._Cast_CylindricalMeshedGearFlankSystemDeflection(self)
