"""CylindricalGearShaverTangible"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAVER_TANGIBLE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles",
    "CylindricalGearShaverTangible",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _718


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearShaverTangible",)


Self = TypeVar("Self", bound="CylindricalGearShaverTangible")


class CylindricalGearShaverTangible(_726.CutterShapeDefinition):
    """CylindricalGearShaverTangible

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAVER_TANGIBLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearShaverTangible")

    class _Cast_CylindricalGearShaverTangible:
        """Special nested class for casting CylindricalGearShaverTangible to subclasses."""

        def __init__(
            self: "CylindricalGearShaverTangible._Cast_CylindricalGearShaverTangible",
            parent: "CylindricalGearShaverTangible",
        ):
            self._parent = parent

        @property
        def cutter_shape_definition(
            self: "CylindricalGearShaverTangible._Cast_CylindricalGearShaverTangible",
        ) -> "_726.CutterShapeDefinition":
            return self._parent._cast(_726.CutterShapeDefinition)

        @property
        def cylindrical_gear_shaver_tangible(
            self: "CylindricalGearShaverTangible._Cast_CylindricalGearShaverTangible",
        ) -> "CylindricalGearShaverTangible":
            return self._parent

        def __getattr__(
            self: "CylindricalGearShaverTangible._Cast_CylindricalGearShaverTangible",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearShaverTangible.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self: Self) -> "_718.CylindricalGearShaver":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaver

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
    ) -> "CylindricalGearShaverTangible._Cast_CylindricalGearShaverTangible":
        return self._Cast_CylindricalGearShaverTangible(self)
