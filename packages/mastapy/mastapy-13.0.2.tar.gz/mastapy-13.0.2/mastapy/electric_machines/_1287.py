"""MagnetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_MAGNET_DESIGN = python_net_import("SMT.MastaAPI.ElectricMachines", "MagnetDesign")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1255, _1288


__docformat__ = "restructuredtext en"
__all__ = ("MagnetDesign",)


Self = TypeVar("Self", bound="MagnetDesign")


class MagnetDesign(_0.APIBase):
    """MagnetDesign

    This is a mastapy class.
    """

    TYPE = _MAGNET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagnetDesign")

    class _Cast_MagnetDesign:
        """Special nested class for casting MagnetDesign to subclasses."""

        def __init__(self: "MagnetDesign._Cast_MagnetDesign", parent: "MagnetDesign"):
            self._parent = parent

        @property
        def cad_magnets_for_layer(
            self: "MagnetDesign._Cast_MagnetDesign",
        ) -> "_1255.CADMagnetsForLayer":
            from mastapy.electric_machines import _1255

            return self._parent._cast(_1255.CADMagnetsForLayer)

        @property
        def magnet_for_layer(
            self: "MagnetDesign._Cast_MagnetDesign",
        ) -> "_1288.MagnetForLayer":
            from mastapy.electric_machines import _1288

            return self._parent._cast(_1288.MagnetForLayer)

        @property
        def magnet_design(self: "MagnetDesign._Cast_MagnetDesign") -> "MagnetDesign":
            return self._parent

        def __getattr__(self: "MagnetDesign._Cast_MagnetDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagnetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d3d_magnet_loss_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwoD3DMagnetLossFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @two_d3d_magnet_loss_factor.setter
    @enforce_parameter_types
    def two_d3d_magnet_loss_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwoD3DMagnetLossFactor = value

    @property
    def length_of_each_segment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfEachSegment

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MagnetMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @magnet_material_database.setter
    @enforce_parameter_types
    def magnet_material_database(self: Self, value: "str"):
        self.wrapped.MagnetMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

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
    def number_of_segments_in_axial_direction(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfSegmentsInAxialDirection

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_segments_in_axial_direction.setter
    @enforce_parameter_types
    def number_of_segments_in_axial_direction(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfSegmentsInAxialDirection = value

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
    def cast_to(self: Self) -> "MagnetDesign._Cast_MagnetDesign":
        return self._Cast_MagnetDesign(self)
