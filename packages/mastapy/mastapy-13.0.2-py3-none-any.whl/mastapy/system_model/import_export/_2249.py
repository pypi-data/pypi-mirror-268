"""GeometryExportOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.ImportExport", "GeometryExportOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometryExportOptions",)


Self = TypeVar("Self", bound="GeometryExportOptions")


class GeometryExportOptions(_0.APIBase):
    """GeometryExportOptions

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryExportOptions")

    class _Cast_GeometryExportOptions:
        """Special nested class for casting GeometryExportOptions to subclasses."""

        def __init__(
            self: "GeometryExportOptions._Cast_GeometryExportOptions",
            parent: "GeometryExportOptions",
        ):
            self._parent = parent

        @property
        def geometry_export_options(
            self: "GeometryExportOptions._Cast_GeometryExportOptions",
        ) -> "GeometryExportOptions":
            return self._parent

        def __getattr__(
            self: "GeometryExportOptions._Cast_GeometryExportOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryExportOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_solid(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateSolid

        if temp is None:
            return False

        return temp

    @create_solid.setter
    @enforce_parameter_types
    def create_solid(self: Self, value: "bool"):
        self.wrapped.CreateSolid = bool(value) if value is not None else False

    @property
    def draw_fillets(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawFillets

        if temp is None:
            return False

        return temp

    @draw_fillets.setter
    @enforce_parameter_types
    def draw_fillets(self: Self, value: "bool"):
        self.wrapped.DrawFillets = bool(value) if value is not None else False

    @property
    def draw_gear_teeth(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawGearTeeth

        if temp is None:
            return False

        return temp

    @draw_gear_teeth.setter
    @enforce_parameter_types
    def draw_gear_teeth(self: Self, value: "bool"):
        self.wrapped.DrawGearTeeth = bool(value) if value is not None else False

    @property
    def draw_to_tip_diameter(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawToTipDiameter

        if temp is None:
            return False

        return temp

    @draw_to_tip_diameter.setter
    @enforce_parameter_types
    def draw_to_tip_diameter(self: Self, value: "bool"):
        self.wrapped.DrawToTipDiameter = bool(value) if value is not None else False

    @property
    def include_bearing_cage(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingCage

        if temp is None:
            return False

        return temp

    @include_bearing_cage.setter
    @enforce_parameter_types
    def include_bearing_cage(self: Self, value: "bool"):
        self.wrapped.IncludeBearingCage = bool(value) if value is not None else False

    @property
    def include_bearing_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingElements

        if temp is None:
            return False

        return temp

    @include_bearing_elements.setter
    @enforce_parameter_types
    def include_bearing_elements(self: Self, value: "bool"):
        self.wrapped.IncludeBearingElements = (
            bool(value) if value is not None else False
        )

    @property
    def include_bearing_inner_race(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingInnerRace

        if temp is None:
            return False

        return temp

    @include_bearing_inner_race.setter
    @enforce_parameter_types
    def include_bearing_inner_race(self: Self, value: "bool"):
        self.wrapped.IncludeBearingInnerRace = (
            bool(value) if value is not None else False
        )

    @property
    def include_bearing_outer_race(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingOuterRace

        if temp is None:
            return False

        return temp

    @include_bearing_outer_race.setter
    @enforce_parameter_types
    def include_bearing_outer_race(self: Self, value: "bool"):
        self.wrapped.IncludeBearingOuterRace = (
            bool(value) if value is not None else False
        )

    @property
    def include_virtual_components(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeVirtualComponents

        if temp is None:
            return False

        return temp

    @include_virtual_components.setter
    @enforce_parameter_types
    def include_virtual_components(self: Self, value: "bool"):
        self.wrapped.IncludeVirtualComponents = (
            bool(value) if value is not None else False
        )

    @property
    def number_of_points_per_cycloidal_disc_half_lobe(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsPerCycloidalDiscHalfLobe

        if temp is None:
            return 0

        return temp

    @number_of_points_per_cycloidal_disc_half_lobe.setter
    @enforce_parameter_types
    def number_of_points_per_cycloidal_disc_half_lobe(self: Self, value: "int"):
        self.wrapped.NumberOfPointsPerCycloidalDiscHalfLobe = (
            int(value) if value is not None else 0
        )

    @enforce_parameter_types
    def export_to_stp(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.ExportToSTP(file_name if file_name else "")

    @enforce_parameter_types
    def save_stl_to_separate_files(
        self: Self, directory_path: "str", save_in_sub_folders: "bool"
    ):
        """Method does not return.

        Args:
            directory_path (str)
            save_in_sub_folders (bool)
        """
        directory_path = str(directory_path)
        save_in_sub_folders = bool(save_in_sub_folders)
        self.wrapped.SaveStlToSeparateFiles(
            directory_path if directory_path else "",
            save_in_sub_folders if save_in_sub_folders else False,
        )

    def to_stl_code(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.ToSTLCode()
        return method_result

    @property
    def cast_to(self: Self) -> "GeometryExportOptions._Cast_GeometryExportOptions":
        return self._Cast_GeometryExportOptions(self)
