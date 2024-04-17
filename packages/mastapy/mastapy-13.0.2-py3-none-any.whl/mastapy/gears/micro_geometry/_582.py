"""Modification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODIFICATION = python_net_import("SMT.MastaAPI.Gears.MicroGeometry", "Modification")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1026
    from mastapy.gears.micro_geometry import _572, _575, _585
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1099,
        _1102,
        _1103,
        _1111,
        _1112,
        _1116,
    )
    from mastapy.gears.gear_designs.conical.micro_geometry import _1178, _1180, _1181


__docformat__ = "restructuredtext en"
__all__ = ("Modification",)


Self = TypeVar("Self", bound="Modification")


class Modification(_0.APIBase):
    """Modification

    This is a mastapy class.
    """

    TYPE = _MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Modification")

    class _Cast_Modification:
        """Special nested class for casting Modification to subclasses."""

        def __init__(self: "Modification._Cast_Modification", parent: "Modification"):
            self._parent = parent

        @property
        def bias_modification(
            self: "Modification._Cast_Modification",
        ) -> "_572.BiasModification":
            from mastapy.gears.micro_geometry import _572

            return self._parent._cast(_572.BiasModification)

        @property
        def lead_modification(
            self: "Modification._Cast_Modification",
        ) -> "_575.LeadModification":
            from mastapy.gears.micro_geometry import _575

            return self._parent._cast(_575.LeadModification)

        @property
        def profile_modification(
            self: "Modification._Cast_Modification",
        ) -> "_585.ProfileModification":
            from mastapy.gears.micro_geometry import _585

            return self._parent._cast(_585.ProfileModification)

        @property
        def cylindrical_gear_bias_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1099.CylindricalGearBiasModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearBiasModification)

        @property
        def cylindrical_gear_lead_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1102.CylindricalGearLeadModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102

            return self._parent._cast(_1102.CylindricalGearLeadModification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(
            self: "Modification._Cast_Modification",
        ) -> "_1103.CylindricalGearLeadModificationAtProfilePosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1103

            return self._parent._cast(
                _1103.CylindricalGearLeadModificationAtProfilePosition
            )

        @property
        def cylindrical_gear_profile_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1111.CylindricalGearProfileModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111

            return self._parent._cast(_1111.CylindricalGearProfileModification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(
            self: "Modification._Cast_Modification",
        ) -> "_1112.CylindricalGearProfileModificationAtFaceWidthPosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112

            return self._parent._cast(
                _1112.CylindricalGearProfileModificationAtFaceWidthPosition
            )

        @property
        def cylindrical_gear_triangular_end_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1116.CylindricalGearTriangularEndModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1116

            return self._parent._cast(_1116.CylindricalGearTriangularEndModification)

        @property
        def conical_gear_bias_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1178.ConicalGearBiasModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1178

            return self._parent._cast(_1178.ConicalGearBiasModification)

        @property
        def conical_gear_lead_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1180.ConicalGearLeadModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1180

            return self._parent._cast(_1180.ConicalGearLeadModification)

        @property
        def conical_gear_profile_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1181.ConicalGearProfileModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1181

            return self._parent._cast(_1181.ConicalGearProfileModification)

        @property
        def modification(self: "Modification._Cast_Modification") -> "Modification":
            return self._parent

        def __getattr__(self: "Modification._Cast_Modification", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Modification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def settings(self: Self) -> "_1026.CylindricalGearMicroGeometrySettingsItem":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Settings

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
    def cast_to(self: Self) -> "Modification._Cast_Modification":
        return self._Cast_Modification(self)
