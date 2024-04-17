"""CylindricalGearFormedWheelGrinderTangible"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FORMED_WHEEL_GRINDER_TANGIBLE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles",
    "CylindricalGearFormedWheelGrinderTangible",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _710


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFormedWheelGrinderTangible",)


Self = TypeVar("Self", bound="CylindricalGearFormedWheelGrinderTangible")


class CylindricalGearFormedWheelGrinderTangible(_726.CutterShapeDefinition):
    """CylindricalGearFormedWheelGrinderTangible

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FORMED_WHEEL_GRINDER_TANGIBLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearFormedWheelGrinderTangible"
    )

    class _Cast_CylindricalGearFormedWheelGrinderTangible:
        """Special nested class for casting CylindricalGearFormedWheelGrinderTangible to subclasses."""

        def __init__(
            self: "CylindricalGearFormedWheelGrinderTangible._Cast_CylindricalGearFormedWheelGrinderTangible",
            parent: "CylindricalGearFormedWheelGrinderTangible",
        ):
            self._parent = parent

        @property
        def cutter_shape_definition(
            self: "CylindricalGearFormedWheelGrinderTangible._Cast_CylindricalGearFormedWheelGrinderTangible",
        ) -> "_726.CutterShapeDefinition":
            return self._parent._cast(_726.CutterShapeDefinition)

        @property
        def cylindrical_gear_formed_wheel_grinder_tangible(
            self: "CylindricalGearFormedWheelGrinderTangible._Cast_CylindricalGearFormedWheelGrinderTangible",
        ) -> "CylindricalGearFormedWheelGrinderTangible":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFormedWheelGrinderTangible._Cast_CylindricalGearFormedWheelGrinderTangible",
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
        self: Self, instance_to_wrap: "CylindricalGearFormedWheelGrinderTangible.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self: Self) -> "_710.CylindricalGearFormGrindingWheel":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearFormGrindingWheel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFormedWheelGrinderTangible._Cast_CylindricalGearFormedWheelGrinderTangible":
        return self._Cast_CylindricalGearFormedWheelGrinderTangible(self)
