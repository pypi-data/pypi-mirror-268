"""CylindricalGearPinionTypeCutterFlank"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1011
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PINION_TYPE_CUTTER_FLANK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearPinionTypeCutterFlank"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1027


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPinionTypeCutterFlank",)


Self = TypeVar("Self", bound="CylindricalGearPinionTypeCutterFlank")


class CylindricalGearPinionTypeCutterFlank(_1011.CylindricalGearAbstractRackFlank):
    """CylindricalGearPinionTypeCutterFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PINION_TYPE_CUTTER_FLANK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearPinionTypeCutterFlank")

    class _Cast_CylindricalGearPinionTypeCutterFlank:
        """Special nested class for casting CylindricalGearPinionTypeCutterFlank to subclasses."""

        def __init__(
            self: "CylindricalGearPinionTypeCutterFlank._Cast_CylindricalGearPinionTypeCutterFlank",
            parent: "CylindricalGearPinionTypeCutterFlank",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack_flank(
            self: "CylindricalGearPinionTypeCutterFlank._Cast_CylindricalGearPinionTypeCutterFlank",
        ) -> "_1011.CylindricalGearAbstractRackFlank":
            return self._parent._cast(_1011.CylindricalGearAbstractRackFlank)

        @property
        def cylindrical_gear_pinion_type_cutter_flank(
            self: "CylindricalGearPinionTypeCutterFlank._Cast_CylindricalGearPinionTypeCutterFlank",
        ) -> "CylindricalGearPinionTypeCutterFlank":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPinionTypeCutterFlank._Cast_CylindricalGearPinionTypeCutterFlank",
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
        self: Self, instance_to_wrap: "CylindricalGearPinionTypeCutterFlank.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def residual_fillet_undercut(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualFilletUndercut

        if temp is None:
            return 0.0

        return temp

    @residual_fillet_undercut.setter
    @enforce_parameter_types
    def residual_fillet_undercut(self: Self, value: "float"):
        self.wrapped.ResidualFilletUndercut = float(value) if value is not None else 0.0

    @property
    def cutter(self: Self) -> "_1027.CylindricalGearPinionTypeCutter":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearPinionTypeCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearPinionTypeCutterFlank._Cast_CylindricalGearPinionTypeCutterFlank":
        return self._Cast_CylindricalGearPinionTypeCutterFlank(self)
