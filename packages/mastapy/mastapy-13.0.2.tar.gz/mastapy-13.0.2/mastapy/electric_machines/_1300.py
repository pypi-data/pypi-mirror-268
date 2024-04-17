"""Rotor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, overridable_enum_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy.electric_machines import _1266
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ROTOR = python_net_import("SMT.MastaAPI.ElectricMachines", "Rotor")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1302, _1256, _1281, _1297, _1311


__docformat__ = "restructuredtext en"
__all__ = ("Rotor",)


Self = TypeVar("Self", bound="Rotor")


class Rotor(_0.APIBase):
    """Rotor

    This is a mastapy class.
    """

    TYPE = _ROTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Rotor")

    class _Cast_Rotor:
        """Special nested class for casting Rotor to subclasses."""

        def __init__(self: "Rotor._Cast_Rotor", parent: "Rotor"):
            self._parent = parent

        @property
        def cad_rotor(self: "Rotor._Cast_Rotor") -> "_1256.CADRotor":
            from mastapy.electric_machines import _1256

            return self._parent._cast(_1256.CADRotor)

        @property
        def interior_permanent_magnet_and_synchronous_reluctance_rotor(
            self: "Rotor._Cast_Rotor",
        ) -> "_1281.InteriorPermanentMagnetAndSynchronousReluctanceRotor":
            from mastapy.electric_machines import _1281

            return self._parent._cast(
                _1281.InteriorPermanentMagnetAndSynchronousReluctanceRotor
            )

        @property
        def permanent_magnet_rotor(
            self: "Rotor._Cast_Rotor",
        ) -> "_1297.PermanentMagnetRotor":
            from mastapy.electric_machines import _1297

            return self._parent._cast(_1297.PermanentMagnetRotor)

        @property
        def surface_permanent_magnet_rotor(
            self: "Rotor._Cast_Rotor",
        ) -> "_1311.SurfacePermanentMagnetRotor":
            from mastapy.electric_machines import _1311

            return self._parent._cast(_1311.SurfacePermanentMagnetRotor)

        @property
        def rotor(self: "Rotor._Cast_Rotor") -> "Rotor":
            return self._parent

        def __getattr__(self: "Rotor._Cast_Rotor", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Rotor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def d_axis_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_and_q_axis_convention(
        self: Self,
    ) -> "overridable.Overridable_DQAxisConvention":
        """Overridable[mastapy.electric_machines.DQAxisConvention]"""
        temp = self.wrapped.DAxisAndQAxisConvention

        if temp is None:
            return None

        value = overridable.Overridable_DQAxisConvention.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @d_axis_and_q_axis_convention.setter
    @enforce_parameter_types
    def d_axis_and_q_axis_convention(
        self: Self,
        value: "Union[_1266.DQAxisConvention, Tuple[_1266.DQAxisConvention, bool]]",
    ):
        wrapper_type = overridable.Overridable_DQAxisConvention.wrapper_type()
        enclosed_type = overridable.Overridable_DQAxisConvention.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.DAxisAndQAxisConvention = value

    @property
    def initial_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialAngle

        if temp is None:
            return 0.0

        return temp

    @initial_angle.setter
    @enforce_parameter_types
    def initial_angle(self: Self, value: "float"):
        self.wrapped.InitialAngle = float(value) if value is not None else 0.0

    @property
    def is_skewed(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsSkewed

        if temp is None:
            return False

        return temp

    @is_skewed.setter
    @enforce_parameter_types
    def is_skewed(self: Self, value: "bool"):
        self.wrapped.IsSkewed = bool(value) if value is not None else False

    @property
    def kair(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Kair

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_flux_barrier_length(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MagnetFluxBarrierLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @magnet_flux_barrier_length.setter
    @enforce_parameter_types
    def magnet_flux_barrier_length(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MagnetFluxBarrierLength = value

    @property
    def number_of_magnet_segments_in_axial_direction(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfMagnetSegmentsInAxialDirection

        if temp is None:
            return 0

        return temp

    @number_of_magnet_segments_in_axial_direction.setter
    @enforce_parameter_types
    def number_of_magnet_segments_in_axial_direction(self: Self, value: "int"):
        self.wrapped.NumberOfMagnetSegmentsInAxialDirection = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_poles(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPoles

        if temp is None:
            return 0

        return temp

    @number_of_poles.setter
    @enforce_parameter_types
    def number_of_poles(self: Self, value: "int"):
        self.wrapped.NumberOfPoles = int(value) if value is not None else 0

    @property
    def number_of_slices(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlices

        if temp is None:
            return 0

        return temp

    @number_of_slices.setter
    @enforce_parameter_types
    def number_of_slices(self: Self, value: "int"):
        self.wrapped.NumberOfSlices = int(value) if value is not None else 0

    @property
    def outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

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
    def polar_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_length(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RotorLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rotor_length.setter
    @enforce_parameter_types
    def rotor_length(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RotorLength = value

    @property
    def rotor_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.RotorMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @rotor_material_database.setter
    @enforce_parameter_types
    def rotor_material_database(self: Self, value: "str"):
        self.wrapped.RotorMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def use_same_material_as_stator(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSameMaterialAsStator

        if temp is None:
            return False

        return temp

    @use_same_material_as_stator.setter
    @enforce_parameter_types
    def use_same_material_as_stator(self: Self, value: "bool"):
        self.wrapped.UseSameMaterialAsStator = (
            bool(value) if value is not None else False
        )

    @property
    def skew_slices(self: Self) -> "List[_1302.RotorSkewSlice]":
        """List[mastapy.electric_machines.RotorSkewSlice]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SkewSlices

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
    def cast_to(self: Self) -> "Rotor._Cast_Rotor":
        return self._Cast_Rotor(self)
