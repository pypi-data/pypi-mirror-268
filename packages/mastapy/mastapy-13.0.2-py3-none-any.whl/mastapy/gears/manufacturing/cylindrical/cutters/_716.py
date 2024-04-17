"""CylindricalGearRealCutterDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _709
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_REAL_CUTTER_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearRealCutterDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _707,
        _710,
        _711,
        _712,
        _713,
        _715,
        _717,
        _718,
        _721,
    )
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearRealCutterDesign",)


Self = TypeVar("Self", bound="CylindricalGearRealCutterDesign")


class CylindricalGearRealCutterDesign(_709.CylindricalGearAbstractCutterDesign):
    """CylindricalGearRealCutterDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_REAL_CUTTER_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearRealCutterDesign")

    class _Cast_CylindricalGearRealCutterDesign:
        """Special nested class for casting CylindricalGearRealCutterDesign to subclasses."""

        def __init__(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
            parent: "CylindricalGearRealCutterDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_709.CylindricalGearAbstractCutterDesign":
            return self._parent._cast(_709.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_form_grinding_wheel(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_710.CylindricalGearFormGrindingWheel":
            from mastapy.gears.manufacturing.cylindrical.cutters import _710

            return self._parent._cast(_710.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_711.CylindricalGearGrindingWorm":
            from mastapy.gears.manufacturing.cylindrical.cutters import _711

            return self._parent._cast(_711.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_712.CylindricalGearHobDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _712

            return self._parent._cast(_712.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_713.CylindricalGearPlungeShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_715.CylindricalGearRackDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _715

            return self._parent._cast(_715.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_shaper(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_717.CylindricalGearShaper":
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_718.CylindricalGearShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _718

            return self._parent._cast(_718.CylindricalGearShaver)

        @property
        def involute_cutter_design(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "_721.InvoluteCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _721

            return self._parent._cast(_721.InvoluteCutterDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
        ) -> "CylindricalGearRealCutterDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearRealCutterDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_and_gear_normal_base_pitch_comparison_tolerance(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CutterAndGearNormalBasePitchComparisonTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cutter_and_gear_normal_base_pitch_comparison_tolerance.setter
    @enforce_parameter_types
    def cutter_and_gear_normal_base_pitch_comparison_tolerance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CutterAndGearNormalBasePitchComparisonTolerance = value

    @property
    def has_tolerances(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasTolerances

        if temp is None:
            return False

        return temp

    @has_tolerances.setter
    @enforce_parameter_types
    def has_tolerances(self: Self, value: "bool"):
        self.wrapped.HasTolerances = bool(value) if value is not None else False

    @property
    def nominal_cutter_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalCutterDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_constant_base_pitch(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngleConstantBasePitch

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle_constant_base_pitch.setter
    @enforce_parameter_types
    def normal_pressure_angle_constant_base_pitch(self: Self, value: "float"):
        self.wrapped.NormalPressureAngleConstantBasePitch = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_points_for_reporting_fillet_shape(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPointsForReportingFilletShape

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_points_for_reporting_fillet_shape.setter
    @enforce_parameter_types
    def number_of_points_for_reporting_fillet_shape(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPointsForReportingFilletShape = value

    @property
    def number_of_points_for_reporting_main_blade_shape(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPointsForReportingMainBladeShape

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_points_for_reporting_main_blade_shape.setter
    @enforce_parameter_types
    def number_of_points_for_reporting_main_blade_shape(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPointsForReportingMainBladeShape = value

    @property
    def specify_custom_blade_shape(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyCustomBladeShape

        if temp is None:
            return False

        return temp

    @specify_custom_blade_shape.setter
    @enforce_parameter_types
    def specify_custom_blade_shape(self: Self, value: "bool"):
        self.wrapped.SpecifyCustomBladeShape = (
            bool(value) if value is not None else False
        )

    @property
    def customised_cutting_edge_profile(self: Self) -> "_707.CustomisableEdgeProfile":
        """mastapy.gears.manufacturing.cylindrical.cutters.CustomisableEdgeProfile

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CustomisedCuttingEdgeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def nominal_cutter_shape(self: Self) -> "_726.CutterShapeDefinition":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.CutterShapeDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalCutterShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign":
        return self._Cast_CylindricalGearRealCutterDesign(self)
