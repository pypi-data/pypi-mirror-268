"""CylindricalMeshedGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalMeshedGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2756,
        _2753,
        _2747,
    )
    from mastapy.gears.ltca import _848


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshedGearSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalMeshedGearSystemDeflection")


class CylindricalMeshedGearSystemDeflection(_0.APIBase):
    """CylindricalMeshedGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalMeshedGearSystemDeflection"
    )

    class _Cast_CylindricalMeshedGearSystemDeflection:
        """Special nested class for casting CylindricalMeshedGearSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalMeshedGearSystemDeflection._Cast_CylindricalMeshedGearSystemDeflection",
            parent: "CylindricalMeshedGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_meshed_gear_system_deflection(
            self: "CylindricalMeshedGearSystemDeflection._Cast_CylindricalMeshedGearSystemDeflection",
        ) -> "CylindricalMeshedGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshedGearSystemDeflection._Cast_CylindricalMeshedGearSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalMeshedGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def change_in_operating_pitch_diameter_due_to_thermal_effects(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInOperatingPitchDiameterDueToThermalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_tip_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingTipClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TiltX

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TiltY

        if temp is None:
            return 0.0

        return temp

    @property
    def left_flank(self: Self) -> "_2756.CylindricalMeshedGearFlankSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalMeshedGearFlankSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_2756.CylindricalMeshedGearFlankSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalMeshedGearFlankSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compression_side_fillet_results(
        self: Self,
    ) -> "List[_848.GearRootFilletStressResults]":
        """List[mastapy.gears.ltca.GearRootFilletStressResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompressionSideFilletResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flanks(self: Self) -> "List[_2756.CylindricalMeshedGearFlankSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalMeshedGearFlankSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tension_side_fillet_results(
        self: Self,
    ) -> "List[_848.GearRootFilletStressResults]":
        """List[mastapy.gears.ltca.GearRootFilletStressResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TensionSideFilletResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def both_flanks(self: Self) -> "_2756.CylindricalMeshedGearFlankSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalMeshedGearFlankSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_system_deflection(
        self: Self,
    ) -> "_2753.CylindricalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_mesh_system_deflection(
        self: Self,
    ) -> "_2747.CylindricalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMeshSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def other_cylindrical_gear_system_deflection(
        self: Self,
    ) -> "_2753.CylindricalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OtherCylindricalGearSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    ) -> "CylindricalMeshedGearSystemDeflection._Cast_CylindricalMeshedGearSystemDeflection":
        return self._Cast_CylindricalMeshedGearSystemDeflection(self)
