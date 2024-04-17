"""EquivalentLoadFactors"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EQUIVALENT_LOAD_FACTORS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "EquivalentLoadFactors"
)


__docformat__ = "restructuredtext en"
__all__ = ("EquivalentLoadFactors",)


Self = TypeVar("Self", bound="EquivalentLoadFactors")


class EquivalentLoadFactors(
    _1593.IndependentReportablePropertiesBase["EquivalentLoadFactors"]
):
    """EquivalentLoadFactors

    This is a mastapy class.
    """

    TYPE = _EQUIVALENT_LOAD_FACTORS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EquivalentLoadFactors")

    class _Cast_EquivalentLoadFactors:
        """Special nested class for casting EquivalentLoadFactors to subclasses."""

        def __init__(
            self: "EquivalentLoadFactors._Cast_EquivalentLoadFactors",
            parent: "EquivalentLoadFactors",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "EquivalentLoadFactors._Cast_EquivalentLoadFactors",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def equivalent_load_factors(
            self: "EquivalentLoadFactors._Cast_EquivalentLoadFactors",
        ) -> "EquivalentLoadFactors":
            return self._parent

        def __getattr__(
            self: "EquivalentLoadFactors._Cast_EquivalentLoadFactors", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EquivalentLoadFactors.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_load_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_load_factor.setter
    @enforce_parameter_types
    def axial_load_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialLoadFactor = value

    @property
    def radial_load_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_load_factor.setter
    @enforce_parameter_types
    def radial_load_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialLoadFactor = value

    @property
    def cast_to(self: Self) -> "EquivalentLoadFactors._Cast_EquivalentLoadFactors":
        return self._Cast_EquivalentLoadFactors(self)
