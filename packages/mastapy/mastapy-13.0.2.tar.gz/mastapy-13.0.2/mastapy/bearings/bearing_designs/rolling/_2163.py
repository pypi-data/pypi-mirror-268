"""GeometricConstantsForRollingFrictionalMoments"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRIC_CONSTANTS_FOR_ROLLING_FRICTIONAL_MOMENTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling",
    "GeometricConstantsForRollingFrictionalMoments",
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometricConstantsForRollingFrictionalMoments",)


Self = TypeVar("Self", bound="GeometricConstantsForRollingFrictionalMoments")


class GeometricConstantsForRollingFrictionalMoments(_0.APIBase):
    """GeometricConstantsForRollingFrictionalMoments

    This is a mastapy class.
    """

    TYPE = _GEOMETRIC_CONSTANTS_FOR_ROLLING_FRICTIONAL_MOMENTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GeometricConstantsForRollingFrictionalMoments"
    )

    class _Cast_GeometricConstantsForRollingFrictionalMoments:
        """Special nested class for casting GeometricConstantsForRollingFrictionalMoments to subclasses."""

        def __init__(
            self: "GeometricConstantsForRollingFrictionalMoments._Cast_GeometricConstantsForRollingFrictionalMoments",
            parent: "GeometricConstantsForRollingFrictionalMoments",
        ):
            self._parent = parent

        @property
        def geometric_constants_for_rolling_frictional_moments(
            self: "GeometricConstantsForRollingFrictionalMoments._Cast_GeometricConstantsForRollingFrictionalMoments",
        ) -> "GeometricConstantsForRollingFrictionalMoments":
            return self._parent

        def __getattr__(
            self: "GeometricConstantsForRollingFrictionalMoments._Cast_GeometricConstantsForRollingFrictionalMoments",
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
        instance_to_wrap: "GeometricConstantsForRollingFrictionalMoments.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def r1(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.R1

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @r1.setter
    @enforce_parameter_types
    def r1(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.R1 = value

    @property
    def r2(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.R2

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @r2.setter
    @enforce_parameter_types
    def r2(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.R2 = value

    @property
    def r3(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.R3

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @r3.setter
    @enforce_parameter_types
    def r3(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.R3 = value

    @property
    def r4(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.R4

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @r4.setter
    @enforce_parameter_types
    def r4(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.R4 = value

    @property
    def cast_to(
        self: Self,
    ) -> "GeometricConstantsForRollingFrictionalMoments._Cast_GeometricConstantsForRollingFrictionalMoments":
        return self._Cast_GeometricConstantsForRollingFrictionalMoments(self)
