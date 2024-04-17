"""CylindricalGearShaver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters import _721
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAVER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "CylindricalGearShaver"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _713, _716, _709
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearShaver",)


Self = TypeVar("Self", bound="CylindricalGearShaver")


class CylindricalGearShaver(_721.InvoluteCutterDesign):
    """CylindricalGearShaver

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearShaver")

    class _Cast_CylindricalGearShaver:
        """Special nested class for casting CylindricalGearShaver to subclasses."""

        def __init__(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
            parent: "CylindricalGearShaver",
        ):
            self._parent = parent

        @property
        def involute_cutter_design(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
        ) -> "_721.InvoluteCutterDesign":
            return self._parent._cast(_721.InvoluteCutterDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
        ) -> "_716.CylindricalGearRealCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
        ) -> "_709.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
        ) -> "_713.CylindricalGearPlungeShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_shaver(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver",
        ) -> "CylindricalGearShaver":
            return self._parent

        def __getattr__(
            self: "CylindricalGearShaver._Cast_CylindricalGearShaver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearShaver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

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
    def normal_tip_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def root_form_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RootFormDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @root_form_diameter.setter
    @enforce_parameter_types
    def root_form_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RootFormDiameter = value

    @property
    def tip_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @tip_diameter.setter
    @enforce_parameter_types
    def tip_diameter(self: Self, value: "float"):
        self.wrapped.TipDiameter = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "CylindricalGearShaver._Cast_CylindricalGearShaver":
        return self._Cast_CylindricalGearShaver(self)
