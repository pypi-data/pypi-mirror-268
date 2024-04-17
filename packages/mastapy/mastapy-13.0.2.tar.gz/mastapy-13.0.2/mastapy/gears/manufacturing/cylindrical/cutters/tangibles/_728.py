"""CylindricalGearHobShape"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_HOB_SHAPE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles",
    "CylindricalGearHobShape",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _712
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearHobShape",)


Self = TypeVar("Self", bound="CylindricalGearHobShape")


class CylindricalGearHobShape(_733.RackShape):
    """CylindricalGearHobShape

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_HOB_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearHobShape")

    class _Cast_CylindricalGearHobShape:
        """Special nested class for casting CylindricalGearHobShape to subclasses."""

        def __init__(
            self: "CylindricalGearHobShape._Cast_CylindricalGearHobShape",
            parent: "CylindricalGearHobShape",
        ):
            self._parent = parent

        @property
        def rack_shape(
            self: "CylindricalGearHobShape._Cast_CylindricalGearHobShape",
        ) -> "_733.RackShape":
            return self._parent._cast(_733.RackShape)

        @property
        def cutter_shape_definition(
            self: "CylindricalGearHobShape._Cast_CylindricalGearHobShape",
        ) -> "_726.CutterShapeDefinition":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726

            return self._parent._cast(_726.CutterShapeDefinition)

        @property
        def cylindrical_gear_hob_shape(
            self: "CylindricalGearHobShape._Cast_CylindricalGearHobShape",
        ) -> "CylindricalGearHobShape":
            return self._parent

        def __getattr__(
            self: "CylindricalGearHobShape._Cast_CylindricalGearHobShape", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearHobShape.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edge_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_blade_control_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumBladeControlDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tip_control_distance_for_zero_protuberance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTipControlDistanceForZeroProtuberance

        if temp is None:
            return 0.0

        return temp

    @property
    def protuberance_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProtuberanceLength

        if temp is None:
            return 0.0

        return temp

    @property
    def protuberance_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProtuberancePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def design(self: Self) -> "_712.CylindricalGearHobDesign":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearHobDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CylindricalGearHobShape._Cast_CylindricalGearHobShape":
        return self._Cast_CylindricalGearHobShape(self)
