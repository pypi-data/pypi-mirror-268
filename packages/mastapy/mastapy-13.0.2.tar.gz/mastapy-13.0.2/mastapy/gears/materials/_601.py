"""ISOTR1417912001CoefficientOfFrictionConstants"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTR1417912001_COEFFICIENT_OF_FRICTION_CONSTANTS = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "ISOTR1417912001CoefficientOfFrictionConstants"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISOTR1417912001CoefficientOfFrictionConstants",)


Self = TypeVar("Self", bound="ISOTR1417912001CoefficientOfFrictionConstants")


class ISOTR1417912001CoefficientOfFrictionConstants(_1836.NamedDatabaseItem):
    """ISOTR1417912001CoefficientOfFrictionConstants

    This is a mastapy class.
    """

    TYPE = _ISOTR1417912001_COEFFICIENT_OF_FRICTION_CONSTANTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISOTR1417912001CoefficientOfFrictionConstants"
    )

    class _Cast_ISOTR1417912001CoefficientOfFrictionConstants:
        """Special nested class for casting ISOTR1417912001CoefficientOfFrictionConstants to subclasses."""

        def __init__(
            self: "ISOTR1417912001CoefficientOfFrictionConstants._Cast_ISOTR1417912001CoefficientOfFrictionConstants",
            parent: "ISOTR1417912001CoefficientOfFrictionConstants",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "ISOTR1417912001CoefficientOfFrictionConstants._Cast_ISOTR1417912001CoefficientOfFrictionConstants",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def isotr1417912001_coefficient_of_friction_constants(
            self: "ISOTR1417912001CoefficientOfFrictionConstants._Cast_ISOTR1417912001CoefficientOfFrictionConstants",
        ) -> "ISOTR1417912001CoefficientOfFrictionConstants":
            return self._parent

        def __getattr__(
            self: "ISOTR1417912001CoefficientOfFrictionConstants._Cast_ISOTR1417912001CoefficientOfFrictionConstants",
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
        self: Self,
        instance_to_wrap: "ISOTR1417912001CoefficientOfFrictionConstants.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def constant_c1(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ConstantC1

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @constant_c1.setter
    @enforce_parameter_types
    def constant_c1(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ConstantC1 = value

    @property
    def load_intensity_exponent(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LoadIntensityExponent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @load_intensity_exponent.setter
    @enforce_parameter_types
    def load_intensity_exponent(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LoadIntensityExponent = value

    @property
    def oil_viscosity_exponent(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OilViscosityExponent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @oil_viscosity_exponent.setter
    @enforce_parameter_types
    def oil_viscosity_exponent(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OilViscosityExponent = value

    @property
    def pitch_line_velocity_exponent(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchLineVelocityExponent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_line_velocity_exponent.setter
    @enforce_parameter_types
    def pitch_line_velocity_exponent(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchLineVelocityExponent = value

    @property
    def cast_to(
        self: Self,
    ) -> "ISOTR1417912001CoefficientOfFrictionConstants._Cast_ISOTR1417912001CoefficientOfFrictionConstants":
        return self._Cast_ISOTR1417912001CoefficientOfFrictionConstants(self)
