"""GearMeshLoadedContactPoint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOADED_CONTACT_POINT = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearMeshLoadedContactPoint"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _862


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshLoadedContactPoint",)


Self = TypeVar("Self", bound="GearMeshLoadedContactPoint")


class GearMeshLoadedContactPoint(_0.APIBase):
    """GearMeshLoadedContactPoint

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOADED_CONTACT_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshLoadedContactPoint")

    class _Cast_GearMeshLoadedContactPoint:
        """Special nested class for casting GearMeshLoadedContactPoint to subclasses."""

        def __init__(
            self: "GearMeshLoadedContactPoint._Cast_GearMeshLoadedContactPoint",
            parent: "GearMeshLoadedContactPoint",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_loaded_contact_point(
            self: "GearMeshLoadedContactPoint._Cast_GearMeshLoadedContactPoint",
        ) -> "_862.CylindricalGearMeshLoadedContactPoint":
            from mastapy.gears.ltca.cylindrical import _862

            return self._parent._cast(_862.CylindricalGearMeshLoadedContactPoint)

        @property
        def gear_mesh_loaded_contact_point(
            self: "GearMeshLoadedContactPoint._Cast_GearMeshLoadedContactPoint",
        ) -> "GearMeshLoadedContactPoint":
            return self._parent

        def __getattr__(
            self: "GearMeshLoadedContactPoint._Cast_GearMeshLoadedContactPoint",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshLoadedContactPoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_line_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLineIndex

        if temp is None:
            return 0

        return temp

    @property
    def contact_point_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPointIndex

        if temp is None:
            return 0

        return temp

    @property
    def contact_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_of_max_sheer_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaxSheerStress

        if temp is None:
            return 0.0

        return temp

    @property
    def force_unit_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def gaps_between_flanks_in_transverse_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GapsBetweenFlanksInTransversePlane

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_half_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactHalfWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def max_sheer_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxSheerStress

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_position_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPositionIndex

        if temp is None:
            return 0

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
    def strip_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StripLength

        if temp is None:
            return 0.0

        return temp

    @property
    def total_deflection_for_mesh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDeflectionForMesh

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
    ) -> "GearMeshLoadedContactPoint._Cast_GearMeshLoadedContactPoint":
        return self._Cast_GearMeshLoadedContactPoint(self)
