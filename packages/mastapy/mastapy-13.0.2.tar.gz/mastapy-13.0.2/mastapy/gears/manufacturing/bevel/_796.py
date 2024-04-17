"""ConicalSetMicroGeometryConfigBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalSetMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from mastapy.gears import _328
    from mastapy.gears.manufacturing.bevel import _794, _795
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("ConicalSetMicroGeometryConfigBase",)


Self = TypeVar("Self", bound="ConicalSetMicroGeometryConfigBase")


class ConicalSetMicroGeometryConfigBase(_1237.GearSetImplementationDetail):
    """ConicalSetMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MICRO_GEOMETRY_CONFIG_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalSetMicroGeometryConfigBase")

    class _Cast_ConicalSetMicroGeometryConfigBase:
        """Special nested class for casting ConicalSetMicroGeometryConfigBase to subclasses."""

        def __init__(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
            parent: "ConicalSetMicroGeometryConfigBase",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_detail(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
        ) -> "_1237.GearSetImplementationDetail":
            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
        ) -> "_794.ConicalSetManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
        ) -> "_795.ConicalSetMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _795

            return self._parent._cast(_795.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
        ) -> "ConicalSetMicroGeometryConfigBase":
            return self._parent

        def __getattr__(
            self: "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase",
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
        self: Self, instance_to_wrap: "ConicalSetMicroGeometryConfigBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_layer_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CompoundLayerThickness

        if temp is None:
            return 0.0

        return temp

    @compound_layer_thickness.setter
    @enforce_parameter_types
    def compound_layer_thickness(self: Self, value: "float"):
        self.wrapped.CompoundLayerThickness = float(value) if value is not None else 0.0

    @property
    def deflection_from_bending_option(
        self: Self,
    ) -> "_328.DeflectionFromBendingOption":
        """mastapy.gears.DeflectionFromBendingOption"""
        temp = self.wrapped.DeflectionFromBendingOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.DeflectionFromBendingOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._328", "DeflectionFromBendingOption"
        )(value)

    @deflection_from_bending_option.setter
    @enforce_parameter_types
    def deflection_from_bending_option(
        self: Self, value: "_328.DeflectionFromBendingOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.DeflectionFromBendingOption"
        )
        self.wrapped.DeflectionFromBendingOption = value

    @property
    def file_location_for_contact_chart(self: Self) -> "str":
        """str"""
        temp = self.wrapped.FileLocationForContactChart

        if temp is None:
            return ""

        return temp

    @file_location_for_contact_chart.setter
    @enforce_parameter_types
    def file_location_for_contact_chart(self: Self, value: "str"):
        self.wrapped.FileLocationForContactChart = (
            str(value) if value is not None else ""
        )

    @property
    def number_of_columns_for_grid(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfColumnsForGrid

        if temp is None:
            return 0

        return temp

    @number_of_columns_for_grid.setter
    @enforce_parameter_types
    def number_of_columns_for_grid(self: Self, value: "int"):
        self.wrapped.NumberOfColumnsForGrid = int(value) if value is not None else 0

    @property
    def number_of_points_for_interpolated_surface_u(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsForInterpolatedSurfaceU

        if temp is None:
            return 0

        return temp

    @number_of_points_for_interpolated_surface_u.setter
    @enforce_parameter_types
    def number_of_points_for_interpolated_surface_u(self: Self, value: "int"):
        self.wrapped.NumberOfPointsForInterpolatedSurfaceU = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_for_interpolated_surface_v(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsForInterpolatedSurfaceV

        if temp is None:
            return 0

        return temp

    @number_of_points_for_interpolated_surface_v.setter
    @enforce_parameter_types
    def number_of_points_for_interpolated_surface_v(self: Self, value: "int"):
        self.wrapped.NumberOfPointsForInterpolatedSurfaceV = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_rows_for_fillet_grid(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRowsForFilletGrid

        if temp is None:
            return 0

        return temp

    @number_of_rows_for_fillet_grid.setter
    @enforce_parameter_types
    def number_of_rows_for_fillet_grid(self: Self, value: "int"):
        self.wrapped.NumberOfRowsForFilletGrid = int(value) if value is not None else 0

    @property
    def number_of_rows_for_flank_grid(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRowsForFlankGrid

        if temp is None:
            return 0

        return temp

    @number_of_rows_for_flank_grid.setter
    @enforce_parameter_types
    def number_of_rows_for_flank_grid(self: Self, value: "int"):
        self.wrapped.NumberOfRowsForFlankGrid = int(value) if value is not None else 0

    @property
    def single_tooth_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SingleToothStiffness

        if temp is None:
            return 0.0

        return temp

    @single_tooth_stiffness.setter
    @enforce_parameter_types
    def single_tooth_stiffness(self: Self, value: "float"):
        self.wrapped.SingleToothStiffness = float(value) if value is not None else 0.0

    @property
    def write_contact_chart_to_file_after_solve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.WriteContactChartToFileAfterSolve

        if temp is None:
            return False

        return temp

    @write_contact_chart_to_file_after_solve.setter
    @enforce_parameter_types
    def write_contact_chart_to_file_after_solve(self: Self, value: "bool"):
        self.wrapped.WriteContactChartToFileAfterSolve = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase":
        return self._Cast_ConicalSetMicroGeometryConfigBase(self)
