"""CylindricalGearFormGrindingWheel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters import _716
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FORM_GRINDING_WHEEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearFormGrindingWheel",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.gears.manufacturing.cylindrical.cutters import _709
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFormGrindingWheel",)


Self = TypeVar("Self", bound="CylindricalGearFormGrindingWheel")


class CylindricalGearFormGrindingWheel(_716.CylindricalGearRealCutterDesign):
    """CylindricalGearFormGrindingWheel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FORM_GRINDING_WHEEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFormGrindingWheel")

    class _Cast_CylindricalGearFormGrindingWheel:
        """Special nested class for casting CylindricalGearFormGrindingWheel to subclasses."""

        def __init__(
            self: "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel",
            parent: "CylindricalGearFormGrindingWheel",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel",
        ) -> "_716.CylindricalGearRealCutterDesign":
            return self._parent._cast(_716.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel",
        ) -> "_709.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_form_grinding_wheel(
            self: "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel",
        ) -> "CylindricalGearFormGrindingWheel":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearFormGrindingWheel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def right_hand_cutting_edge_shape(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.RightHandCuttingEdgeShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @right_hand_cutting_edge_shape.setter
    @enforce_parameter_types
    def right_hand_cutting_edge_shape(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.RightHandCuttingEdgeShape = value.wrapped

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel":
        return self._Cast_CylindricalGearFormGrindingWheel(self)
