"""CutterShapeDefinition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUTTER_SHAPE_DEFINITION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles",
    "CutterShapeDefinition",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _716
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import (
        _732,
        _727,
        _728,
        _729,
        _730,
        _731,
        _733,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CutterShapeDefinition",)


Self = TypeVar("Self", bound="CutterShapeDefinition")


class CutterShapeDefinition(_0.APIBase):
    """CutterShapeDefinition

    This is a mastapy class.
    """

    TYPE = _CUTTER_SHAPE_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CutterShapeDefinition")

    class _Cast_CutterShapeDefinition:
        """Special nested class for casting CutterShapeDefinition to subclasses."""

        def __init__(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
            parent: "CutterShapeDefinition",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_formed_wheel_grinder_tangible(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "_727.CylindricalGearFormedWheelGrinderTangible":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _727

            return self._parent._cast(_727.CylindricalGearFormedWheelGrinderTangible)

        @property
        def cylindrical_gear_hob_shape(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "_728.CylindricalGearHobShape":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _728

            return self._parent._cast(_728.CylindricalGearHobShape)

        @property
        def cylindrical_gear_shaper_tangible(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "_729.CylindricalGearShaperTangible":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _729

            return self._parent._cast(_729.CylindricalGearShaperTangible)

        @property
        def cylindrical_gear_shaver_tangible(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "_730.CylindricalGearShaverTangible":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _730

            return self._parent._cast(_730.CylindricalGearShaverTangible)

        @property
        def cylindrical_gear_worm_grinder_shape(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "_731.CylindricalGearWormGrinderShape":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _731

            return self._parent._cast(_731.CylindricalGearWormGrinderShape)

        @property
        def rack_shape(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "_733.RackShape":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _733

            return self._parent._cast(_733.RackShape)

        @property
        def cutter_shape_definition(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition",
        ) -> "CutterShapeDefinition":
            return self._parent

        def __getattr__(
            self: "CutterShapeDefinition._Cast_CutterShapeDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CutterShapeDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModule

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
    def normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def design(self: Self) -> "_716.CylindricalGearRealCutterDesign":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearRealCutterDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fillet_points(self: Self) -> "List[_732.NamedPoint]":
        """List[mastapy.gears.manufacturing.cylindrical.cutters.tangibles.NamedPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def main_blade_points(self: Self) -> "List[_732.NamedPoint]":
        """List[mastapy.gears.manufacturing.cylindrical.cutters.tangibles.NamedPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MainBladePoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CutterShapeDefinition._Cast_CutterShapeDefinition":
        return self._Cast_CutterShapeDefinition(self)
