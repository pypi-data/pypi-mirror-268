"""AbstractStator"""

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
_ABSTRACT_STATOR = python_net_import("SMT.MastaAPI.ElectricMachines", "AbstractStator")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1250, _1323, _1257, _1306


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStator",)


Self = TypeVar("Self", bound="AbstractStator")


class AbstractStator(_0.APIBase):
    """AbstractStator

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_STATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractStator")

    class _Cast_AbstractStator:
        """Special nested class for casting AbstractStator to subclasses."""

        def __init__(
            self: "AbstractStator._Cast_AbstractStator", parent: "AbstractStator"
        ):
            self._parent = parent

        @property
        def cad_stator(
            self: "AbstractStator._Cast_AbstractStator",
        ) -> "_1257.CADStator":
            from mastapy.electric_machines import _1257

            return self._parent._cast(_1257.CADStator)

        @property
        def stator(self: "AbstractStator._Cast_AbstractStator") -> "_1306.Stator":
            from mastapy.electric_machines import _1306

            return self._parent._cast(_1306.Stator)

        @property
        def abstract_stator(
            self: "AbstractStator._Cast_AbstractStator",
        ) -> "AbstractStator":
            return self._parent

        def __getattr__(self: "AbstractStator._Cast_AbstractStator", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractStator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_stator_partitioning_lines(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngleBetweenStatorPartitioningLines

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle_between_stator_partitioning_lines.setter
    @enforce_parameter_types
    def angle_between_stator_partitioning_lines(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngleBetweenStatorPartitioningLines = value

    @property
    def back_iron_inner_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BackIronInnerRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def back_iron_mid_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BackIronMidRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_diameter_of_stator_teeth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    @enforce_parameter_types
    def inner_diameter_of_stator_teeth(self: Self, value: "float"):
        self.wrapped.InnerDiameterOfStatorTeeth = (
            float(value) if value is not None else 0.0
        )

    @property
    def mid_tooth_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MidToothRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_slots(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    @enforce_parameter_types
    def number_of_slots(self: Self, value: "int"):
        self.wrapped.NumberOfSlots = int(value) if value is not None else 0

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def outer_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def split_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SplitRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def stator_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StatorLength

        if temp is None:
            return 0.0

        return temp

    @stator_length.setter
    @enforce_parameter_types
    def stator_length(self: Self, value: "float"):
        self.wrapped.StatorLength = float(value) if value is not None else 0.0

    @property
    def stator_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.StatorMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @stator_material_database.setter
    @enforce_parameter_types
    def stator_material_database(self: Self, value: "str"):
        self.wrapped.StatorMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def tooth_and_slot(self: Self) -> "_1250.AbstractToothAndSlot":
        """mastapy.electric_machines.AbstractToothAndSlot

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def windings(self: Self) -> "_1323.Windings":
        """mastapy.electric_machines.Windings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Windings

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
    def cast_to(self: Self) -> "AbstractStator._Cast_AbstractStator":
        return self._Cast_AbstractStator(self)
