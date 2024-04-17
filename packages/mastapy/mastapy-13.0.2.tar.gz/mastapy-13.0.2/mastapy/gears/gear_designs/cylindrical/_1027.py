"""CylindricalGearPinionTypeCutter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PINION_TYPE_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearPinionTypeCutter"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1028


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPinionTypeCutter",)


Self = TypeVar("Self", bound="CylindricalGearPinionTypeCutter")


class CylindricalGearPinionTypeCutter(_1010.CylindricalGearAbstractRack):
    """CylindricalGearPinionTypeCutter

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PINION_TYPE_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearPinionTypeCutter")

    class _Cast_CylindricalGearPinionTypeCutter:
        """Special nested class for casting CylindricalGearPinionTypeCutter to subclasses."""

        def __init__(
            self: "CylindricalGearPinionTypeCutter._Cast_CylindricalGearPinionTypeCutter",
            parent: "CylindricalGearPinionTypeCutter",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack(
            self: "CylindricalGearPinionTypeCutter._Cast_CylindricalGearPinionTypeCutter",
        ) -> "_1010.CylindricalGearAbstractRack":
            return self._parent._cast(_1010.CylindricalGearAbstractRack)

        @property
        def cylindrical_gear_pinion_type_cutter(
            self: "CylindricalGearPinionTypeCutter._Cast_CylindricalGearPinionTypeCutter",
        ) -> "CylindricalGearPinionTypeCutter":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPinionTypeCutter._Cast_CylindricalGearPinionTypeCutter",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearPinionTypeCutter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nominal_addendum_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NominalAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @nominal_addendum_factor.setter
    @enforce_parameter_types
    def nominal_addendum_factor(self: Self, value: "float"):
        self.wrapped.NominalAddendumFactor = float(value) if value is not None else 0.0

    @property
    def nominal_dedendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "int"):
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def profile_shift_coefficient(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @profile_shift_coefficient.setter
    @enforce_parameter_types
    def profile_shift_coefficient(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ProfileShiftCoefficient = value

    @property
    def left_flank(self: Self) -> "_1028.CylindricalGearPinionTypeCutterFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearPinionTypeCutterFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1028.CylindricalGearPinionTypeCutterFlank":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearPinionTypeCutterFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearPinionTypeCutter._Cast_CylindricalGearPinionTypeCutter":
        return self._Cast_CylindricalGearPinionTypeCutter(self)
