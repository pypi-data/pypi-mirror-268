"""PlungeShaverCalculationInputs"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_CALCULATION_INPUTS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "PlungeShaverCalculationInputs",
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _735
    from mastapy.gears.gear_designs.cylindrical import _1092


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverCalculationInputs",)


Self = TypeVar("Self", bound="PlungeShaverCalculationInputs")


class PlungeShaverCalculationInputs(_0.APIBase):
    """PlungeShaverCalculationInputs

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_CALCULATION_INPUTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverCalculationInputs")

    class _Cast_PlungeShaverCalculationInputs:
        """Special nested class for casting PlungeShaverCalculationInputs to subclasses."""

        def __init__(
            self: "PlungeShaverCalculationInputs._Cast_PlungeShaverCalculationInputs",
            parent: "PlungeShaverCalculationInputs",
        ):
            self._parent = parent

        @property
        def plunge_shaver_calculation_inputs(
            self: "PlungeShaverCalculationInputs._Cast_PlungeShaverCalculationInputs",
        ) -> "PlungeShaverCalculationInputs":
            return self._parent

        def __getattr__(
            self: "PlungeShaverCalculationInputs._Cast_PlungeShaverCalculationInputs",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverCalculationInputs.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_for_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterForThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_for_thickness.setter
    @enforce_parameter_types
    def diameter_for_thickness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterForThickness = value

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
    def number_of_teeth_on_the_shaver(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethOnTheShaver

        if temp is None:
            return 0

        return temp

    @number_of_teeth_on_the_shaver.setter
    @enforce_parameter_types
    def number_of_teeth_on_the_shaver(self: Self, value: "int"):
        self.wrapped.NumberOfTeethOnTheShaver = int(value) if value is not None else 0

    @property
    def shaver_hand(self: Self) -> "_336.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.ShaverHand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._336", "Hand")(value)

    @shaver_hand.setter
    @enforce_parameter_types
    def shaver_hand(self: Self, value: "_336.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.ShaverHand = value

    @property
    def shaver_helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaverHelixAngle

        if temp is None:
            return 0.0

        return temp

    @shaver_helix_angle.setter
    @enforce_parameter_types
    def shaver_helix_angle(self: Self, value: "float"):
        self.wrapped.ShaverHelixAngle = float(value) if value is not None else 0.0

    @property
    def shaver_normal_module(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ShaverNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @shaver_normal_module.setter
    @enforce_parameter_types
    def shaver_normal_module(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ShaverNormalModule = value

    @property
    def shaver_normal_pressure_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ShaverNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @shaver_normal_pressure_angle.setter
    @enforce_parameter_types
    def shaver_normal_pressure_angle(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ShaverNormalPressureAngle = value

    @property
    def shaver_tip_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaverTipDiameter

        if temp is None:
            return 0.0

        return temp

    @shaver_tip_diameter.setter
    @enforce_parameter_types
    def shaver_tip_diameter(self: Self, value: "float"):
        self.wrapped.ShaverTipDiameter = float(value) if value is not None else 0.0

    @property
    def thickness_at_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ThicknessAtDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @thickness_at_diameter.setter
    @enforce_parameter_types
    def thickness_at_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ThicknessAtDiameter = value

    @property
    def input_gear_geometry(self: Self) -> "_735.CylindricalCutterSimulatableGear":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalCutterSimulatableGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputGearGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_thickness(self: Self) -> "_1092.ToothThicknessSpecificationBase":
        """mastapy.gears.gear_designs.cylindrical.ToothThicknessSpecificationBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThickness

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
    ) -> "PlungeShaverCalculationInputs._Cast_PlungeShaverCalculationInputs":
        return self._Cast_PlungeShaverCalculationInputs(self)
