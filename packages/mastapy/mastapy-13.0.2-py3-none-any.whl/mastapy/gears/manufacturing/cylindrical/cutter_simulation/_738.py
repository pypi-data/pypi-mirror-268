"""CylindricalManufacturedVirtualGearInMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_VIRTUAL_GEAR_IN_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "CylindricalManufacturedVirtualGearInMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _750


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedVirtualGearInMesh",)


Self = TypeVar("Self", bound="CylindricalManufacturedVirtualGearInMesh")


class CylindricalManufacturedVirtualGearInMesh(_0.APIBase):
    """CylindricalManufacturedVirtualGearInMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_VIRTUAL_GEAR_IN_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalManufacturedVirtualGearInMesh"
    )

    class _Cast_CylindricalManufacturedVirtualGearInMesh:
        """Special nested class for casting CylindricalManufacturedVirtualGearInMesh to subclasses."""

        def __init__(
            self: "CylindricalManufacturedVirtualGearInMesh._Cast_CylindricalManufacturedVirtualGearInMesh",
            parent: "CylindricalManufacturedVirtualGearInMesh",
        ):
            self._parent = parent

        @property
        def cylindrical_manufactured_virtual_gear_in_mesh(
            self: "CylindricalManufacturedVirtualGearInMesh._Cast_CylindricalManufacturedVirtualGearInMesh",
        ) -> "CylindricalManufacturedVirtualGearInMesh":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedVirtualGearInMesh._Cast_CylindricalManufacturedVirtualGearInMesh",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedVirtualGearInMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_moment_arm_for_agma_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingMomentArmForAGMARating

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_moment_arm_for_iso_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingMomentArmForISORating

        if temp is None:
            return 0.0

        return temp

    @property
    def form_factor_for_iso_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormFactorForISORating

        if temp is None:
            return 0.0

        return temp

    @property
    def load_direction_for_agma_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDirectionForAGMARating

        if temp is None:
            return 0.0

        return temp

    @property
    def load_direction_angle_for_iso_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDirectionAngleForISORating

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
    def stress_correction_factor_for_iso_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactorForISORating

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chord_for_agma_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordForAGMARating

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_gear(self: Self) -> "_750.VirtualSimulationCalculator":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.VirtualSimulationCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualGear

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
    ) -> "CylindricalManufacturedVirtualGearInMesh._Cast_CylindricalManufacturedVirtualGearInMesh":
        return self._Cast_CylindricalManufacturedVirtualGearInMesh(self)
