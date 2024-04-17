"""FEStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_STIFFNESS = python_net_import("SMT.MastaAPI.NodalAnalysis", "FEStiffness")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _79
    from mastapy.gears.ltca import _836, _838, _850
    from mastapy.gears.ltca.cylindrical import _854, _856
    from mastapy.gears.ltca.conical import _866, _868
    from mastapy.system_model.fe import _2390


__docformat__ = "restructuredtext en"
__all__ = ("FEStiffness",)


Self = TypeVar("Self", bound="FEStiffness")


class FEStiffness(_0.APIBase):
    """FEStiffness

    This is a mastapy class.
    """

    TYPE = _FE_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEStiffness")

    class _Cast_FEStiffness:
        """Special nested class for casting FEStiffness to subclasses."""

        def __init__(self: "FEStiffness._Cast_FEStiffness", parent: "FEStiffness"):
            self._parent = parent

        @property
        def gear_bending_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_836.GearBendingStiffness":
            from mastapy.gears.ltca import _836

            return self._parent._cast(_836.GearBendingStiffness)

        @property
        def gear_contact_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_838.GearContactStiffness":
            from mastapy.gears.ltca import _838

            return self._parent._cast(_838.GearContactStiffness)

        @property
        def gear_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_850.GearStiffness":
            from mastapy.gears.ltca import _850

            return self._parent._cast(_850.GearStiffness)

        @property
        def cylindrical_gear_bending_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_854.CylindricalGearBendingStiffness":
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearBendingStiffness)

        @property
        def cylindrical_gear_contact_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_856.CylindricalGearContactStiffness":
            from mastapy.gears.ltca.cylindrical import _856

            return self._parent._cast(_856.CylindricalGearContactStiffness)

        @property
        def conical_gear_bending_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_866.ConicalGearBendingStiffness":
            from mastapy.gears.ltca.conical import _866

            return self._parent._cast(_866.ConicalGearBendingStiffness)

        @property
        def conical_gear_contact_stiffness(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_868.ConicalGearContactStiffness":
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalGearContactStiffness)

        @property
        def fe_substructure(
            self: "FEStiffness._Cast_FEStiffness",
        ) -> "_2390.FESubstructure":
            from mastapy.system_model.fe import _2390

            return self._parent._cast(_2390.FESubstructure)

        @property
        def fe_stiffness(self: "FEStiffness._Cast_FEStiffness") -> "FEStiffness":
            return self._parent

        def __getattr__(self: "FEStiffness._Cast_FEStiffness", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_alignment_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialAlignmentTolerance

        if temp is None:
            return 0.0

        return temp

    @axial_alignment_tolerance.setter
    @enforce_parameter_types
    def axial_alignment_tolerance(self: Self, value: "float"):
        self.wrapped.AxialAlignmentTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def calculate_acceleration_force_from_mass_matrix(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CalculateAccelerationForceFromMassMatrix

        if temp is None:
            return False

        return temp

    @calculate_acceleration_force_from_mass_matrix.setter
    @enforce_parameter_types
    def calculate_acceleration_force_from_mass_matrix(self: Self, value: "bool"):
        self.wrapped.CalculateAccelerationForceFromMassMatrix = (
            bool(value) if value is not None else False
        )

    @property
    def frequency_of_highest_mode(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfHighestMode

        if temp is None:
            return 0.0

        return temp

    @property
    def gyroscopic_matrix_is_known(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GyroscopicMatrixIsKnown

        if temp is None:
            return False

        return temp

    @property
    def is_grounded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsGrounded

        if temp is None:
            return False

        return temp

    @property
    def is_using_full_fe_model(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsUsingFullFEModel

        if temp is None:
            return False

        return temp

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_matrix_is_known(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassMatrixIsKnown

        if temp is None:
            return False

        return temp

    @property
    def number_of_internal_modes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfInternalModes

        if temp is None:
            return 0

        return temp

    @number_of_internal_modes.setter
    @enforce_parameter_types
    def number_of_internal_modes(self: Self, value: "int"):
        self.wrapped.NumberOfInternalModes = int(value) if value is not None else 0

    @property
    def number_of_physical_nodes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPhysicalNodes

        if temp is None:
            return 0

        return temp

    @number_of_physical_nodes.setter
    @enforce_parameter_types
    def number_of_physical_nodes(self: Self, value: "int"):
        self.wrapped.NumberOfPhysicalNodes = int(value) if value is not None else 0

    @property
    def radial_alignment_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialAlignmentTolerance

        if temp is None:
            return 0.0

        return temp

    @radial_alignment_tolerance.setter
    @enforce_parameter_types
    def radial_alignment_tolerance(self: Self, value: "float"):
        self.wrapped.RadialAlignmentTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def reason_scalar_mass_not_known(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonScalarMassNotKnown

        if temp is None:
            return ""

        return temp

    @property
    def tolerance_for_zero_frequencies(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceForZeroFrequencies

        if temp is None:
            return 0.0

        return temp

    @tolerance_for_zero_frequencies.setter
    @enforce_parameter_types
    def tolerance_for_zero_frequencies(self: Self, value: "float"):
        self.wrapped.ToleranceForZeroFrequencies = (
            float(value) if value is not None else 0.0
        )

    @property
    def centre_of_mass_in_local_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOfMassInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def mass_matrix_mn_rad_s_kg(self: Self) -> "_79.NodalMatrix":
        """mastapy.nodal_analysis.NodalMatrix

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassMatrixMNRadSKg

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_in_fe_coordinate_system_mn_rad(self: Self) -> "_79.NodalMatrix":
        """mastapy.nodal_analysis.NodalMatrix

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessInFECoordinateSystemMNRad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_matrix(self: Self) -> "_79.NodalMatrix":
        """mastapy.nodal_analysis.NodalMatrix

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrix

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
    def set_stiffness_and_mass(
        self: Self,
        stiffness: "_79.NodalMatrix",
        mass: Optional["_79.NodalMatrix"] = None,
    ):
        """Method does not return.

        Args:
            stiffness (mastapy.nodal_analysis.NodalMatrix)
            mass (mastapy.nodal_analysis.NodalMatrix, optional)
        """
        self.wrapped.SetStiffnessAndMass(
            stiffness.wrapped if stiffness else None, mass.wrapped if mass else None
        )

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
    def cast_to(self: Self) -> "FEStiffness._Cast_FEStiffness":
        return self._Cast_FEStiffness(self)
