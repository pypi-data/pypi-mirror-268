"""GearMeshLoadDistributionAtRotation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOAD_DISTRIBUTION_AT_ROTATION = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearMeshLoadDistributionAtRotation"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _852, _846
    from mastapy.gears.ltca.cylindrical import _864
    from mastapy.gears.ltca.conical import _874


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshLoadDistributionAtRotation",)


Self = TypeVar("Self", bound="GearMeshLoadDistributionAtRotation")


class GearMeshLoadDistributionAtRotation(_0.APIBase):
    """GearMeshLoadDistributionAtRotation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOAD_DISTRIBUTION_AT_ROTATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshLoadDistributionAtRotation")

    class _Cast_GearMeshLoadDistributionAtRotation:
        """Special nested class for casting GearMeshLoadDistributionAtRotation to subclasses."""

        def __init__(
            self: "GearMeshLoadDistributionAtRotation._Cast_GearMeshLoadDistributionAtRotation",
            parent: "GearMeshLoadDistributionAtRotation",
        ):
            self._parent = parent

        @property
        def cylindrical_mesh_load_distribution_at_rotation(
            self: "GearMeshLoadDistributionAtRotation._Cast_GearMeshLoadDistributionAtRotation",
        ) -> "_864.CylindricalMeshLoadDistributionAtRotation":
            from mastapy.gears.ltca.cylindrical import _864

            return self._parent._cast(_864.CylindricalMeshLoadDistributionAtRotation)

        @property
        def conical_mesh_load_distribution_at_rotation(
            self: "GearMeshLoadDistributionAtRotation._Cast_GearMeshLoadDistributionAtRotation",
        ) -> "_874.ConicalMeshLoadDistributionAtRotation":
            from mastapy.gears.ltca.conical import _874

            return self._parent._cast(_874.ConicalMeshLoadDistributionAtRotation)

        @property
        def gear_mesh_load_distribution_at_rotation(
            self: "GearMeshLoadDistributionAtRotation._Cast_GearMeshLoadDistributionAtRotation",
        ) -> "GearMeshLoadDistributionAtRotation":
            return self._parent

        def __getattr__(
            self: "GearMeshLoadDistributionAtRotation._Cast_GearMeshLoadDistributionAtRotation",
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
        self: Self, instance_to_wrap: "GearMeshLoadDistributionAtRotation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Index

        if temp is None:
            return 0

        return temp

    @property
    def mesh_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_loaded_teeth(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfLoadedTeeth

        if temp is None:
            return 0

        return temp

    @property
    def number_of_potentially_loaded_teeth(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfPotentiallyLoadedTeeth

        if temp is None:
            return 0

        return temp

    @property
    def transmission_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TransmissionError

        if temp is None:
            return 0.0

        return temp

    @transmission_error.setter
    @enforce_parameter_types
    def transmission_error(self: Self, value: "float"):
        self.wrapped.TransmissionError = float(value) if value is not None else 0.0

    @property
    def gear_a_in_mesh(
        self: Self,
    ) -> "_852.MeshedGearLoadDistributionAnalysisAtRotation":
        """mastapy.gears.ltca.MeshedGearLoadDistributionAnalysisAtRotation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAInMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_in_mesh(
        self: Self,
    ) -> "_852.MeshedGearLoadDistributionAnalysisAtRotation":
        """mastapy.gears.ltca.MeshedGearLoadDistributionAnalysisAtRotation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBInMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loaded_contact_lines(self: Self) -> "List[_846.GearMeshLoadedContactLine]":
        """List[mastapy.gears.ltca.GearMeshLoadedContactLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedContactLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshed_gears(
        self: Self,
    ) -> "List[_852.MeshedGearLoadDistributionAnalysisAtRotation]":
        """List[mastapy.gears.ltca.MeshedGearLoadDistributionAnalysisAtRotation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

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
    def cast_to(
        self: Self,
    ) -> "GearMeshLoadDistributionAtRotation._Cast_GearMeshLoadDistributionAtRotation":
        return self._Cast_GearMeshLoadDistributionAtRotation(self)
