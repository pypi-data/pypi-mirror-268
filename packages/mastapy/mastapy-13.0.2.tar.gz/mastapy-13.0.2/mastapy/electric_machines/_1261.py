"""CoolingDuctLayerSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COOLING_DUCT_LAYER_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CoolingDuctLayerSpecification"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1262


__docformat__ = "restructuredtext en"
__all__ = ("CoolingDuctLayerSpecification",)


Self = TypeVar("Self", bound="CoolingDuctLayerSpecification")


class CoolingDuctLayerSpecification(_0.APIBase):
    """CoolingDuctLayerSpecification

    This is a mastapy class.
    """

    TYPE = _COOLING_DUCT_LAYER_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoolingDuctLayerSpecification")

    class _Cast_CoolingDuctLayerSpecification:
        """Special nested class for casting CoolingDuctLayerSpecification to subclasses."""

        def __init__(
            self: "CoolingDuctLayerSpecification._Cast_CoolingDuctLayerSpecification",
            parent: "CoolingDuctLayerSpecification",
        ):
            self._parent = parent

        @property
        def cooling_duct_layer_specification(
            self: "CoolingDuctLayerSpecification._Cast_CoolingDuctLayerSpecification",
        ) -> "CoolingDuctLayerSpecification":
            return self._parent

        def __getattr__(
            self: "CoolingDuctLayerSpecification._Cast_CoolingDuctLayerSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoolingDuctLayerSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def corner_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CornerRadius

        if temp is None:
            return 0.0

        return temp

    @corner_radius.setter
    @enforce_parameter_types
    def corner_radius(self: Self, value: "float"):
        self.wrapped.CornerRadius = float(value) if value is not None else 0.0

    @property
    def distance_to_lower_arc(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceToLowerArc

        if temp is None:
            return 0.0

        return temp

    @distance_to_lower_arc.setter
    @enforce_parameter_types
    def distance_to_lower_arc(self: Self, value: "float"):
        self.wrapped.DistanceToLowerArc = float(value) if value is not None else 0.0

    @property
    def duct_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DuctDiameter

        if temp is None:
            return 0.0

        return temp

    @duct_diameter.setter
    @enforce_parameter_types
    def duct_diameter(self: Self, value: "float"):
        self.wrapped.DuctDiameter = float(value) if value is not None else 0.0

    @property
    def first_duct_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstDuctAngle

        if temp is None:
            return 0.0

        return temp

    @first_duct_angle.setter
    @enforce_parameter_types
    def first_duct_angle(self: Self, value: "float"):
        self.wrapped.FirstDuctAngle = float(value) if value is not None else 0.0

    @property
    def length_in_radial_direction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LengthInRadialDirection

        if temp is None:
            return 0.0

        return temp

    @length_in_radial_direction.setter
    @enforce_parameter_types
    def length_in_radial_direction(self: Self, value: "float"):
        self.wrapped.LengthInRadialDirection = (
            float(value) if value is not None else 0.0
        )

    @property
    def lower_arc_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LowerArcLength

        if temp is None:
            return 0.0

        return temp

    @lower_arc_length.setter
    @enforce_parameter_types
    def lower_arc_length(self: Self, value: "float"):
        self.wrapped.LowerArcLength = float(value) if value is not None else 0.0

    @property
    def lower_fillet_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LowerFilletRadius

        if temp is None:
            return 0.0

        return temp

    @lower_fillet_radius.setter
    @enforce_parameter_types
    def lower_fillet_radius(self: Self, value: "float"):
        self.wrapped.LowerFilletRadius = float(value) if value is not None else 0.0

    @property
    def major_axis_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MajorAxisLength

        if temp is None:
            return 0.0

        return temp

    @major_axis_length.setter
    @enforce_parameter_types
    def major_axis_length(self: Self, value: "float"):
        self.wrapped.MajorAxisLength = float(value) if value is not None else 0.0

    @property
    def minor_axis_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinorAxisLength

        if temp is None:
            return 0.0

        return temp

    @minor_axis_length.setter
    @enforce_parameter_types
    def minor_axis_length(self: Self, value: "float"):
        self.wrapped.MinorAxisLength = float(value) if value is not None else 0.0

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
    def number_of_ducts(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfDucts

        if temp is None:
            return 0

        return temp

    @number_of_ducts.setter
    @enforce_parameter_types
    def number_of_ducts(self: Self, value: "int"):
        self.wrapped.NumberOfDucts = int(value) if value is not None else 0

    @property
    def radial_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialOffset

        if temp is None:
            return 0.0

        return temp

    @radial_offset.setter
    @enforce_parameter_types
    def radial_offset(self: Self, value: "float"):
        self.wrapped.RadialOffset = float(value) if value is not None else 0.0

    @property
    def rectangular_duct_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RectangularDuctHeight

        if temp is None:
            return 0.0

        return temp

    @rectangular_duct_height.setter
    @enforce_parameter_types
    def rectangular_duct_height(self: Self, value: "float"):
        self.wrapped.RectangularDuctHeight = float(value) if value is not None else 0.0

    @property
    def rectangular_duct_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RectangularDuctWidth

        if temp is None:
            return 0.0

        return temp

    @rectangular_duct_width.setter
    @enforce_parameter_types
    def rectangular_duct_width(self: Self, value: "float"):
        self.wrapped.RectangularDuctWidth = float(value) if value is not None else 0.0

    @property
    def rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Rotation

        if temp is None:
            return 0.0

        return temp

    @rotation.setter
    @enforce_parameter_types
    def rotation(self: Self, value: "float"):
        self.wrapped.Rotation = float(value) if value is not None else 0.0

    @property
    def shape(self: Self) -> "_1262.CoolingDuctShape":
        """mastapy.electric_machines.CoolingDuctShape"""
        temp = self.wrapped.Shape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.CoolingDuctShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1262", "CoolingDuctShape"
        )(value)

    @shape.setter
    @enforce_parameter_types
    def shape(self: Self, value: "_1262.CoolingDuctShape"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.CoolingDuctShape"
        )
        self.wrapped.Shape = value

    @property
    def upper_arc_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UpperArcLength

        if temp is None:
            return 0.0

        return temp

    @upper_arc_length.setter
    @enforce_parameter_types
    def upper_arc_length(self: Self, value: "float"):
        self.wrapped.UpperArcLength = float(value) if value is not None else 0.0

    @property
    def upper_fillet_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UpperFilletRadius

        if temp is None:
            return 0.0

        return temp

    @upper_fillet_radius.setter
    @enforce_parameter_types
    def upper_fillet_radius(self: Self, value: "float"):
        self.wrapped.UpperFilletRadius = float(value) if value is not None else 0.0

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
    ) -> "CoolingDuctLayerSpecification._Cast_CoolingDuctLayerSpecification":
        return self._Cast_CoolingDuctLayerSpecification(self)
