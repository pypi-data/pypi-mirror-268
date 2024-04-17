"""SKFSealFrictionalMomentConstants"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, overridable_enum_runtime, conversion
from mastapy.bearings import _1905
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_SEAL_FRICTIONAL_MOMENT_CONSTANTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "SKFSealFrictionalMomentConstants"
)


__docformat__ = "restructuredtext en"
__all__ = ("SKFSealFrictionalMomentConstants",)


Self = TypeVar("Self", bound="SKFSealFrictionalMomentConstants")


class SKFSealFrictionalMomentConstants(_0.APIBase):
    """SKFSealFrictionalMomentConstants

    This is a mastapy class.
    """

    TYPE = _SKF_SEAL_FRICTIONAL_MOMENT_CONSTANTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SKFSealFrictionalMomentConstants")

    class _Cast_SKFSealFrictionalMomentConstants:
        """Special nested class for casting SKFSealFrictionalMomentConstants to subclasses."""

        def __init__(
            self: "SKFSealFrictionalMomentConstants._Cast_SKFSealFrictionalMomentConstants",
            parent: "SKFSealFrictionalMomentConstants",
        ):
            self._parent = parent

        @property
        def skf_seal_frictional_moment_constants(
            self: "SKFSealFrictionalMomentConstants._Cast_SKFSealFrictionalMomentConstants",
        ) -> "SKFSealFrictionalMomentConstants":
            return self._parent

        def __getattr__(
            self: "SKFSealFrictionalMomentConstants._Cast_SKFSealFrictionalMomentConstants",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SKFSealFrictionalMomentConstants.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ks1(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.KS1

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ks1.setter
    @enforce_parameter_types
    def ks1(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.KS1 = value

    @property
    def ks2(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.KS2

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ks2.setter
    @enforce_parameter_types
    def ks2(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.KS2 = value

    @property
    def seal_counterface_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SealCounterfaceDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @seal_counterface_diameter.setter
    @enforce_parameter_types
    def seal_counterface_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SealCounterfaceDiameter = value

    @property
    def seal_location(self: Self) -> "overridable.Overridable_SealLocation":
        """Overridable[mastapy.bearings.SealLocation]"""
        temp = self.wrapped.SealLocation

        if temp is None:
            return None

        value = overridable.Overridable_SealLocation.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @seal_location.setter
    @enforce_parameter_types
    def seal_location(
        self: Self, value: "Union[_1905.SealLocation, Tuple[_1905.SealLocation, bool]]"
    ):
        wrapper_type = overridable.Overridable_SealLocation.wrapper_type()
        enclosed_type = overridable.Overridable_SealLocation.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.SealLocation = value

    @property
    def beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Beta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @beta.setter
    @enforce_parameter_types
    def beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Beta = value

    @property
    def cast_to(
        self: Self,
    ) -> "SKFSealFrictionalMomentConstants._Cast_SKFSealFrictionalMomentConstants":
        return self._Cast_SKFSealFrictionalMomentConstants(self)
