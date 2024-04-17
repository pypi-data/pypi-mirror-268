"""CylindricalGearWormGrinderShape"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_WORM_GRINDER_SHAPE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles",
    "CylindricalGearWormGrinderShape",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _711
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearWormGrinderShape",)


Self = TypeVar("Self", bound="CylindricalGearWormGrinderShape")


class CylindricalGearWormGrinderShape(_733.RackShape):
    """CylindricalGearWormGrinderShape

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_WORM_GRINDER_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearWormGrinderShape")

    class _Cast_CylindricalGearWormGrinderShape:
        """Special nested class for casting CylindricalGearWormGrinderShape to subclasses."""

        def __init__(
            self: "CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape",
            parent: "CylindricalGearWormGrinderShape",
        ):
            self._parent = parent

        @property
        def rack_shape(
            self: "CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape",
        ) -> "_733.RackShape":
            return self._parent._cast(_733.RackShape)

        @property
        def cutter_shape_definition(
            self: "CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape",
        ) -> "_726.CutterShapeDefinition":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726

            return self._parent._cast(_726.CutterShapeDefinition)

        @property
        def cylindrical_gear_worm_grinder_shape(
            self: "CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape",
        ) -> "CylindricalGearWormGrinderShape":
            return self._parent

        def __getattr__(
            self: "CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearWormGrinderShape.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self: Self) -> "_711.CylindricalGearGrindingWorm":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearGrindingWorm

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
    ) -> "CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape":
        return self._Cast_CylindricalGearWormGrinderShape(self)
