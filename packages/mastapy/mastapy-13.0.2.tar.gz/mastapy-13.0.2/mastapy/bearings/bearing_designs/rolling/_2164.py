"""GeometricConstantsForSlidingFrictionalMoments"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRIC_CONSTANTS_FOR_SLIDING_FRICTIONAL_MOMENTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling",
    "GeometricConstantsForSlidingFrictionalMoments",
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometricConstantsForSlidingFrictionalMoments",)


Self = TypeVar("Self", bound="GeometricConstantsForSlidingFrictionalMoments")


class GeometricConstantsForSlidingFrictionalMoments(_0.APIBase):
    """GeometricConstantsForSlidingFrictionalMoments

    This is a mastapy class.
    """

    TYPE = _GEOMETRIC_CONSTANTS_FOR_SLIDING_FRICTIONAL_MOMENTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GeometricConstantsForSlidingFrictionalMoments"
    )

    class _Cast_GeometricConstantsForSlidingFrictionalMoments:
        """Special nested class for casting GeometricConstantsForSlidingFrictionalMoments to subclasses."""

        def __init__(
            self: "GeometricConstantsForSlidingFrictionalMoments._Cast_GeometricConstantsForSlidingFrictionalMoments",
            parent: "GeometricConstantsForSlidingFrictionalMoments",
        ):
            self._parent = parent

        @property
        def geometric_constants_for_sliding_frictional_moments(
            self: "GeometricConstantsForSlidingFrictionalMoments._Cast_GeometricConstantsForSlidingFrictionalMoments",
        ) -> "GeometricConstantsForSlidingFrictionalMoments":
            return self._parent

        def __getattr__(
            self: "GeometricConstantsForSlidingFrictionalMoments._Cast_GeometricConstantsForSlidingFrictionalMoments",
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
        instance_to_wrap: "GeometricConstantsForSlidingFrictionalMoments.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def s1(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.S1

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @s1.setter
    @enforce_parameter_types
    def s1(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.S1 = value

    @property
    def s2(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.S2

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @s2.setter
    @enforce_parameter_types
    def s2(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.S2 = value

    @property
    def s3(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.S3

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @s3.setter
    @enforce_parameter_types
    def s3(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.S3 = value

    @property
    def s4(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.S4

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @s4.setter
    @enforce_parameter_types
    def s4(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.S4 = value

    @property
    def s5(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.S5

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @s5.setter
    @enforce_parameter_types
    def s5(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.S5 = value

    @property
    def cast_to(
        self: Self,
    ) -> "GeometricConstantsForSlidingFrictionalMoments._Cast_GeometricConstantsForSlidingFrictionalMoments":
        return self._Cast_GeometricConstantsForSlidingFrictionalMoments(self)
