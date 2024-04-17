"""CylindricalGearAbstractRackFlank"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, Union, Tuple, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_RACK_FLANK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearAbstractRackFlank"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1010, _1016, _1013, _1028, _1083


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAbstractRackFlank",)


Self = TypeVar("Self", bound="CylindricalGearAbstractRackFlank")


class CylindricalGearAbstractRackFlank(_0.APIBase):
    """CylindricalGearAbstractRackFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ABSTRACT_RACK_FLANK

    class ProtuberanceSpecificationMethod(Enum):
        """ProtuberanceSpecificationMethod is a nested enum."""

        @classmethod
        def type_(cls):
            return _CYLINDRICAL_GEAR_ABSTRACT_RACK_FLANK.ProtuberanceSpecificationMethod

        PROTUBERANCE_HEIGHT_AND_ANGLE = 0
        RESIDUAL_FILLET_UNDERCUT = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    ProtuberanceSpecificationMethod.__setattr__ = __enum_setattr
    ProtuberanceSpecificationMethod.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearAbstractRackFlank")

    class _Cast_CylindricalGearAbstractRackFlank:
        """Special nested class for casting CylindricalGearAbstractRackFlank to subclasses."""

        def __init__(
            self: "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank",
            parent: "CylindricalGearAbstractRackFlank",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack_flank(
            self: "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank",
        ) -> "_1013.CylindricalGearBasicRackFlank":
            from mastapy.gears.gear_designs.cylindrical import _1013

            return self._parent._cast(_1013.CylindricalGearBasicRackFlank)

        @property
        def cylindrical_gear_pinion_type_cutter_flank(
            self: "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank",
        ) -> "_1028.CylindricalGearPinionTypeCutterFlank":
            from mastapy.gears.gear_designs.cylindrical import _1028

            return self._parent._cast(_1028.CylindricalGearPinionTypeCutterFlank)

        @property
        def standard_rack_flank(
            self: "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank",
        ) -> "_1083.StandardRackFlank":
            from mastapy.gears.gear_designs.cylindrical import _1083

            return self._parent._cast(_1083.StandardRackFlank)

        @property
        def cylindrical_gear_abstract_rack_flank(
            self: "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank",
        ) -> "CylindricalGearAbstractRackFlank":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearAbstractRackFlank.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chamfer_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ChamferAngle

        if temp is None:
            return 0.0

        return temp

    @chamfer_angle.setter
    @enforce_parameter_types
    def chamfer_angle(self: Self, value: "float"):
        self.wrapped.ChamferAngle = float(value) if value is not None else 0.0

    @property
    def chamfer_angle_in_transverse_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ChamferAngleInTransversePlane

        if temp is None:
            return 0.0

        return temp

    @chamfer_angle_in_transverse_plane.setter
    @enforce_parameter_types
    def chamfer_angle_in_transverse_plane(self: Self, value: "float"):
        self.wrapped.ChamferAngleInTransversePlane = (
            float(value) if value is not None else 0.0
        )

    @property
    def diameter_chamfer_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiameterChamferHeight

        if temp is None:
            return 0.0

        return temp

    @diameter_chamfer_height.setter
    @enforce_parameter_types
    def diameter_chamfer_height(self: Self, value: "float"):
        self.wrapped.DiameterChamferHeight = float(value) if value is not None else 0.0

    @property
    def edge_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    @enforce_parameter_types
    def edge_radius(self: Self, value: "float"):
        self.wrapped.EdgeRadius = float(value) if value is not None else 0.0

    @property
    def edge_radius_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EdgeRadiusFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @edge_radius_factor.setter
    @enforce_parameter_types
    def edge_radius_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EdgeRadiusFactor = value

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
    def protuberance_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceAngle

        if temp is None:
            return 0.0

        return temp

    @protuberance_angle.setter
    @enforce_parameter_types
    def protuberance_angle(self: Self, value: "float"):
        self.wrapped.ProtuberanceAngle = float(value) if value is not None else 0.0

    @property
    def protuberance_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @protuberance_height.setter
    @enforce_parameter_types
    def protuberance_height(self: Self, value: "float"):
        self.wrapped.ProtuberanceHeight = float(value) if value is not None else 0.0

    @property
    def protuberance_height_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceHeightFactor

        if temp is None:
            return 0.0

        return temp

    @protuberance_height_factor.setter
    @enforce_parameter_types
    def protuberance_height_factor(self: Self, value: "float"):
        self.wrapped.ProtuberanceHeightFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def protuberance_specification(
        self: Self,
    ) -> "CylindricalGearAbstractRackFlank.ProtuberanceSpecificationMethod":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRackFlank.ProtuberanceSpecificationMethod"""
        temp = self.wrapped.ProtuberanceSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearAbstractRackFlank+ProtuberanceSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRackFlank.CylindricalGearAbstractRackFlank",
            "ProtuberanceSpecificationMethod",
        )(value)

    @protuberance_specification.setter
    @enforce_parameter_types
    def protuberance_specification(
        self: Self,
        value: "CylindricalGearAbstractRackFlank.ProtuberanceSpecificationMethod",
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearAbstractRackFlank+ProtuberanceSpecificationMethod",
        )
        self.wrapped.ProtuberanceSpecification = value

    @property
    def rack_undercut_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RackUndercutClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def rack_undercut_clearance_normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RackUndercutClearanceNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_chamfer_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialChamferHeight

        if temp is None:
            return 0.0

        return temp

    @radial_chamfer_height.setter
    @enforce_parameter_types
    def radial_chamfer_height(self: Self, value: "float"):
        self.wrapped.RadialChamferHeight = float(value) if value is not None else 0.0

    @property
    def radial_chamfer_height_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialChamferHeightFactor

        if temp is None:
            return 0.0

        return temp

    @radial_chamfer_height_factor.setter
    @enforce_parameter_types
    def radial_chamfer_height_factor(self: Self, value: "float"):
        self.wrapped.RadialChamferHeightFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_fillet_undercut(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualFilletUndercut

        if temp is None:
            return 0.0

        return temp

    @residual_fillet_undercut.setter
    @enforce_parameter_types
    def residual_fillet_undercut(self: Self, value: "float"):
        self.wrapped.ResidualFilletUndercut = float(value) if value is not None else 0.0

    @property
    def residual_fillet_undercut_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualFilletUndercutFactor

        if temp is None:
            return 0.0

        return temp

    @residual_fillet_undercut_factor.setter
    @enforce_parameter_types
    def residual_fillet_undercut_factor(self: Self, value: "float"):
        self.wrapped.ResidualFilletUndercutFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def rough_protuberance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RoughProtuberance

        if temp is None:
            return 0.0

        return temp

    @rough_protuberance.setter
    @enforce_parameter_types
    def rough_protuberance(self: Self, value: "float"):
        self.wrapped.RoughProtuberance = float(value) if value is not None else 0.0

    @property
    def rough_protuberance_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RoughProtuberanceFactor

        if temp is None:
            return 0.0

        return temp

    @rough_protuberance_factor.setter
    @enforce_parameter_types
    def rough_protuberance_factor(self: Self, value: "float"):
        self.wrapped.RoughProtuberanceFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def cutter(self: Self) -> "_1010.CylindricalGearAbstractRack":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRack

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    ) -> "CylindricalGearAbstractRackFlank._Cast_CylindricalGearAbstractRackFlank":
        return self._Cast_CylindricalGearAbstractRackFlank(self)
