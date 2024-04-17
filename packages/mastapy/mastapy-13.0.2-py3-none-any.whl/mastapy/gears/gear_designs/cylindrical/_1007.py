"""CrossedAxisCylindricalGearPair"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CrossedAxisCylindricalGearPair"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _735
    from mastapy.gears.gear_designs.cylindrical import _1008, _1009


__docformat__ = "restructuredtext en"
__all__ = ("CrossedAxisCylindricalGearPair",)


Self = TypeVar("Self", bound="CrossedAxisCylindricalGearPair")


class CrossedAxisCylindricalGearPair(_0.APIBase):
    """CrossedAxisCylindricalGearPair

    This is a mastapy class.
    """

    TYPE = _CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CrossedAxisCylindricalGearPair")

    class _Cast_CrossedAxisCylindricalGearPair:
        """Special nested class for casting CrossedAxisCylindricalGearPair to subclasses."""

        def __init__(
            self: "CrossedAxisCylindricalGearPair._Cast_CrossedAxisCylindricalGearPair",
            parent: "CrossedAxisCylindricalGearPair",
        ):
            self._parent = parent

        @property
        def crossed_axis_cylindrical_gear_pair_line_contact(
            self: "CrossedAxisCylindricalGearPair._Cast_CrossedAxisCylindricalGearPair",
        ) -> "_1008.CrossedAxisCylindricalGearPairLineContact":
            from mastapy.gears.gear_designs.cylindrical import _1008

            return self._parent._cast(_1008.CrossedAxisCylindricalGearPairLineContact)

        @property
        def crossed_axis_cylindrical_gear_pair_point_contact(
            self: "CrossedAxisCylindricalGearPair._Cast_CrossedAxisCylindricalGearPair",
        ) -> "_1009.CrossedAxisCylindricalGearPairPointContact":
            from mastapy.gears.gear_designs.cylindrical import _1009

            return self._parent._cast(_1009.CrossedAxisCylindricalGearPairPointContact)

        @property
        def crossed_axis_cylindrical_gear_pair(
            self: "CrossedAxisCylindricalGearPair._Cast_CrossedAxisCylindricalGearPair",
        ) -> "CrossedAxisCylindricalGearPair":
            return self._parent

        def __getattr__(
            self: "CrossedAxisCylindricalGearPair._Cast_CrossedAxisCylindricalGearPair",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CrossedAxisCylindricalGearPair.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @centre_distance.setter
    @enforce_parameter_types
    def centre_distance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CentreDistance = value

    @property
    def contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_gear_start_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveGearStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_end_of_active_profile_diameter(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearEndOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def gear_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_operating_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearOperatingRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_start_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @shaft_angle.setter
    @enforce_parameter_types
    def shaft_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ShaftAngle = value

    @property
    def shaver_end_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverEndOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_operating_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverOperatingRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_required_end_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverRequiredEndOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_start_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_tip_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverTipRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_tip_radius_calculated_by_gear_sap(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverTipRadiusCalculatedByGearSAP

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver(self: Self) -> "_735.CylindricalCutterSimulatableGear":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalCutterSimulatableGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaver

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
    ) -> "CrossedAxisCylindricalGearPair._Cast_CrossedAxisCylindricalGearPair":
        return self._Cast_CrossedAxisCylindricalGearPair(self)
