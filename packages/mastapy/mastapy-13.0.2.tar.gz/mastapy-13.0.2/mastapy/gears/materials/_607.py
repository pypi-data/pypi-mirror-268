"""PlasticSNCurve"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_SN_CURVE = python_net_import("SMT.MastaAPI.Gears.Materials", "PlasticSNCurve")

if TYPE_CHECKING:
    from mastapy.materials import _291, _288, _289
    from mastapy.gears.materials import _606
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498


__docformat__ = "restructuredtext en"
__all__ = ("PlasticSNCurve",)


Self = TypeVar("Self", bound="PlasticSNCurve")


class PlasticSNCurve(_0.APIBase):
    """PlasticSNCurve

    This is a mastapy class.
    """

    TYPE = _PLASTIC_SN_CURVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlasticSNCurve")

    class _Cast_PlasticSNCurve:
        """Special nested class for casting PlasticSNCurve to subclasses."""

        def __init__(
            self: "PlasticSNCurve._Cast_PlasticSNCurve", parent: "PlasticSNCurve"
        ):
            self._parent = parent

        @property
        def plastic_sn_curve_for_the_specified_operating_conditions(
            self: "PlasticSNCurve._Cast_PlasticSNCurve",
        ) -> "_498.PlasticSNCurveForTheSpecifiedOperatingConditions":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498

            return self._parent._cast(
                _498.PlasticSNCurveForTheSpecifiedOperatingConditions
            )

        @property
        def plastic_sn_curve(
            self: "PlasticSNCurve._Cast_PlasticSNCurve",
        ) -> "PlasticSNCurve":
            return self._parent

        def __getattr__(self: "PlasticSNCurve._Cast_PlasticSNCurve", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlasticSNCurve.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_number_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlankTemperature

        if temp is None:
            return 0.0

        return temp

    @flank_temperature.setter
    @enforce_parameter_types
    def flank_temperature(self: Self, value: "float"):
        self.wrapped.FlankTemperature = float(value) if value is not None else 0.0

    @property
    def life_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LifeCycles

        if temp is None:
            return 0.0

        return temp

    @life_cycles.setter
    @enforce_parameter_types
    def life_cycles(self: Self, value: "float"):
        self.wrapped.LifeCycles = float(value) if value is not None else 0.0

    @property
    def lubricant(self: Self) -> "_291.VDI2736LubricantType":
        """mastapy.materials.VDI2736LubricantType"""
        temp = self.wrapped.Lubricant

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.VDI2736LubricantType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._291", "VDI2736LubricantType"
        )(value)

    @lubricant.setter
    @enforce_parameter_types
    def lubricant(self: Self, value: "_291.VDI2736LubricantType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.VDI2736LubricantType"
        )
        self.wrapped.Lubricant = value

    @property
    def nominal_stress_number_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def note_1(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Note1

        if temp is None:
            return ""

        return temp

    @property
    def note_2(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Note2

        if temp is None:
            return ""

        return temp

    @property
    def number_of_rows_in_the_bending_sn_table(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRowsInTheBendingSNTable

        if temp is None:
            return 0

        return temp

    @number_of_rows_in_the_bending_sn_table.setter
    @enforce_parameter_types
    def number_of_rows_in_the_bending_sn_table(self: Self, value: "int"):
        self.wrapped.NumberOfRowsInTheBendingSNTable = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_rows_in_the_contact_sn_table(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRowsInTheContactSNTable

        if temp is None:
            return 0

        return temp

    @number_of_rows_in_the_contact_sn_table.setter
    @enforce_parameter_types
    def number_of_rows_in_the_contact_sn_table(self: Self, value: "int"):
        self.wrapped.NumberOfRowsInTheContactSNTable = (
            int(value) if value is not None else 0
        )

    @property
    def root_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootTemperature

        if temp is None:
            return 0.0

        return temp

    @root_temperature.setter
    @enforce_parameter_types
    def root_temperature(self: Self, value: "float"):
        self.wrapped.RootTemperature = float(value) if value is not None else 0.0

    @property
    def material(self: Self) -> "_606.PlasticCylindricalGearMaterial":
        """mastapy.gears.materials.PlasticCylindricalGearMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Material

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bending_stress_cycle_data_for_damage_tables(
        self: Self,
    ) -> "List[_288.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]":
        """List[mastapy.materials.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressCycleDataForDamageTables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bending_stress_cycle_data(
        self: Self,
    ) -> "List[_288.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]":
        """List[mastapy.materials.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressCycleData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def contact_stress_cycle_data_for_damage_tables(
        self: Self,
    ) -> "List[_289.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]":
        """List[mastapy.materials.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressCycleDataForDamageTables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def contact_stress_cycle_data(
        self: Self,
    ) -> "List[_289.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]":
        """List[mastapy.materials.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressCycleData

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
    def cast_to(self: Self) -> "PlasticSNCurve._Cast_PlasticSNCurve":
        return self._Cast_PlasticSNCurve(self)
