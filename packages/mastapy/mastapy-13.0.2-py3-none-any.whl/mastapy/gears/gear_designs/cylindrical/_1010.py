"""CylindricalGearAbstractRack"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_RACK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearAbstractRack"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1016, _1011, _1012, _1027, _1082
    from mastapy.gears.manufacturing.cylindrical.cutters import _717


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAbstractRack",)


Self = TypeVar("Self", bound="CylindricalGearAbstractRack")


class CylindricalGearAbstractRack(_0.APIBase):
    """CylindricalGearAbstractRack

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ABSTRACT_RACK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearAbstractRack")

    class _Cast_CylindricalGearAbstractRack:
        """Special nested class for casting CylindricalGearAbstractRack to subclasses."""

        def __init__(
            self: "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack",
            parent: "CylindricalGearAbstractRack",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack(
            self: "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack",
        ) -> "_1012.CylindricalGearBasicRack":
            from mastapy.gears.gear_designs.cylindrical import _1012

            return self._parent._cast(_1012.CylindricalGearBasicRack)

        @property
        def cylindrical_gear_pinion_type_cutter(
            self: "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack",
        ) -> "_1027.CylindricalGearPinionTypeCutter":
            from mastapy.gears.gear_designs.cylindrical import _1027

            return self._parent._cast(_1027.CylindricalGearPinionTypeCutter)

        @property
        def standard_rack(
            self: "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack",
        ) -> "_1082.StandardRack":
            from mastapy.gears.gear_designs.cylindrical import _1082

            return self._parent._cast(_1082.StandardRack)

        @property
        def cylindrical_gear_abstract_rack(
            self: "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack",
        ) -> "CylindricalGearAbstractRack":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearAbstractRack.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_rack_addendum_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BasicRackAddendumFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @basic_rack_addendum_factor.setter
    @enforce_parameter_types
    def basic_rack_addendum_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BasicRackAddendumFactor = value

    @property
    def basic_rack_dedendum_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BasicRackDedendumFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @basic_rack_dedendum_factor.setter
    @enforce_parameter_types
    def basic_rack_dedendum_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BasicRackDedendumFactor = value

    @property
    def basic_rack_tip_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_tooth_depth_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackToothDepthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_tip_width_normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterTipWidthNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_possible_cutter_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPossibleCutterEdgeRadius

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
    def use_maximum_edge_radius(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMaximumEdgeRadius

        if temp is None:
            return False

        return temp

    @use_maximum_edge_radius.setter
    @enforce_parameter_types
    def use_maximum_edge_radius(self: Self, value: "bool"):
        self.wrapped.UseMaximumEdgeRadius = bool(value) if value is not None else False

    @property
    def gear(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank(self: Self) -> "_1011.CylindricalGearAbstractRackFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRackFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1011.CylindricalGearAbstractRackFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRackFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaper_for_agma_rating(self: Self) -> "_717.CylindricalGearShaper":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaperForAGMARating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def flanks(self: Self) -> "List[_1011.CylindricalGearAbstractRackFlank]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRackFlank]

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
    def both_flanks(self: Self) -> "_1011.CylindricalGearAbstractRackFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRackFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

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
    ) -> "CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack":
        return self._Cast_CylindricalGearAbstractRack(self)
