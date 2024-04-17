"""CylindricalMeshedGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalMeshedGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1043, _1016, _1022


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshedGear",)


Self = TypeVar("Self", bound="CylindricalMeshedGear")


class CylindricalMeshedGear(_0.APIBase):
    """CylindricalMeshedGear

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMeshedGear")

    class _Cast_CylindricalMeshedGear:
        """Special nested class for casting CylindricalMeshedGear to subclasses."""

        def __init__(
            self: "CylindricalMeshedGear._Cast_CylindricalMeshedGear",
            parent: "CylindricalMeshedGear",
        ):
            self._parent = parent

        @property
        def cylindrical_meshed_gear(
            self: "CylindricalMeshedGear._Cast_CylindricalMeshedGear",
        ) -> "CylindricalMeshedGear":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshedGear._Cast_CylindricalMeshedGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalMeshedGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_face_width_to_reference_diameter_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidthToReferenceDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_to_working_pitch_diameter_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthToWorkingPitchDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_clearance_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_clearance_at_tight_mesh_maximum_metal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipClearanceAtTightMeshMaximumMetal

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_clearance_at_tight_mesh_minimum_metal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipClearanceAtTightMeshMinimumMetal

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def left_flank(self: Self) -> "_1043.CylindricalMeshedGearFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshedGearFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1043.CylindricalMeshedGearFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshedGearFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def flanks(self: Self) -> "List[_1043.CylindricalMeshedGearFlank]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalMeshedGearFlank]

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
    def both_flanks(self: Self) -> "_1043.CylindricalMeshedGearFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalMeshedGearFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

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
    def mesh(self: Self) -> "_1022.CylindricalGearMeshDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mesh

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
    def cast_to(self: Self) -> "CylindricalMeshedGear._Cast_CylindricalMeshedGear":
        return self._Cast_CylindricalMeshedGear(self)
