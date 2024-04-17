"""SingleCylindricalGearTriangularEndModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "SingleCylindricalGearTriangularEndModification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1123, _1130


__docformat__ = "restructuredtext en"
__all__ = ("SingleCylindricalGearTriangularEndModification",)


Self = TypeVar("Self", bound="SingleCylindricalGearTriangularEndModification")


class SingleCylindricalGearTriangularEndModification(_0.APIBase):
    """SingleCylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _SINGLE_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SingleCylindricalGearTriangularEndModification"
    )

    class _Cast_SingleCylindricalGearTriangularEndModification:
        """Special nested class for casting SingleCylindricalGearTriangularEndModification to subclasses."""

        def __init__(
            self: "SingleCylindricalGearTriangularEndModification._Cast_SingleCylindricalGearTriangularEndModification",
            parent: "SingleCylindricalGearTriangularEndModification",
        ):
            self._parent = parent

        @property
        def linear_cylindrical_gear_triangular_end_modification(
            self: "SingleCylindricalGearTriangularEndModification._Cast_SingleCylindricalGearTriangularEndModification",
        ) -> "_1123.LinearCylindricalGearTriangularEndModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1123

            return self._parent._cast(
                _1123.LinearCylindricalGearTriangularEndModification
            )

        @property
        def parabolic_cylindrical_gear_triangular_end_modification(
            self: "SingleCylindricalGearTriangularEndModification._Cast_SingleCylindricalGearTriangularEndModification",
        ) -> "_1130.ParabolicCylindricalGearTriangularEndModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1130

            return self._parent._cast(
                _1130.ParabolicCylindricalGearTriangularEndModification
            )

        @property
        def single_cylindrical_gear_triangular_end_modification(
            self: "SingleCylindricalGearTriangularEndModification._Cast_SingleCylindricalGearTriangularEndModification",
        ) -> "SingleCylindricalGearTriangularEndModification":
            return self._parent

        def __getattr__(
            self: "SingleCylindricalGearTriangularEndModification._Cast_SingleCylindricalGearTriangularEndModification",
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
        self: Self,
        instance_to_wrap: "SingleCylindricalGearTriangularEndModification.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Angle = value

    @property
    def face_width_position(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidthPosition

        if temp is None:
            return 0.0

        return temp

    @face_width_position.setter
    @enforce_parameter_types
    def face_width_position(self: Self, value: "float"):
        self.wrapped.FaceWidthPosition = float(value) if value is not None else 0.0

    @property
    def face_width_position_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidthPositionFactor

        if temp is None:
            return 0.0

        return temp

    @face_width_position_factor.setter
    @enforce_parameter_types
    def face_width_position_factor(self: Self, value: "float"):
        self.wrapped.FaceWidthPositionFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationDiameter

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_diameter.setter
    @enforce_parameter_types
    def profile_evaluation_diameter(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationFactor

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_factor.setter
    @enforce_parameter_types
    def profile_evaluation_factor(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationRadius

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_radius.setter
    @enforce_parameter_types
    def profile_evaluation_radius(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationRollAngle

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_roll_angle.setter
    @enforce_parameter_types
    def profile_evaluation_roll_angle(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationRollAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationRollDistance

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_roll_distance.setter
    @enforce_parameter_types
    def profile_evaluation_roll_distance(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_start_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileStartDiameter

        if temp is None:
            return 0.0

        return temp

    @profile_start_diameter.setter
    @enforce_parameter_types
    def profile_start_diameter(self: Self, value: "float"):
        self.wrapped.ProfileStartDiameter = float(value) if value is not None else 0.0

    @property
    def profile_start_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileStartFactor

        if temp is None:
            return 0.0

        return temp

    @profile_start_factor.setter
    @enforce_parameter_types
    def profile_start_factor(self: Self, value: "float"):
        self.wrapped.ProfileStartFactor = float(value) if value is not None else 0.0

    @property
    def profile_start_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileStartRadius

        if temp is None:
            return 0.0

        return temp

    @profile_start_radius.setter
    @enforce_parameter_types
    def profile_start_radius(self: Self, value: "float"):
        self.wrapped.ProfileStartRadius = float(value) if value is not None else 0.0

    @property
    def profile_start_roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileStartRollAngle

        if temp is None:
            return 0.0

        return temp

    @profile_start_roll_angle.setter
    @enforce_parameter_types
    def profile_start_roll_angle(self: Self, value: "float"):
        self.wrapped.ProfileStartRollAngle = float(value) if value is not None else 0.0

    @property
    def profile_start_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileStartRollDistance

        if temp is None:
            return 0.0

        return temp

    @profile_start_roll_distance.setter
    @enforce_parameter_types
    def profile_start_roll_distance(self: Self, value: "float"):
        self.wrapped.ProfileStartRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Relief

        if temp is None:
            return 0.0

        return temp

    @relief.setter
    @enforce_parameter_types
    def relief(self: Self, value: "float"):
        self.wrapped.Relief = float(value) if value is not None else 0.0

    @property
    def profile_evaluation(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileEvaluation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_start(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileStart

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
    ) -> "SingleCylindricalGearTriangularEndModification._Cast_SingleCylindricalGearTriangularEndModification":
        return self._Cast_SingleCylindricalGearTriangularEndModification(self)
