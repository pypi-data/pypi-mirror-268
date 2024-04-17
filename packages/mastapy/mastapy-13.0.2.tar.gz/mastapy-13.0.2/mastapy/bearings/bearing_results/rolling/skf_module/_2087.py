"""DynamicAxialLoadCarryingCapacity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_AXIAL_LOAD_CARRYING_CAPACITY = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule",
    "DynamicAxialLoadCarryingCapacity",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2100


__docformat__ = "restructuredtext en"
__all__ = ("DynamicAxialLoadCarryingCapacity",)


Self = TypeVar("Self", bound="DynamicAxialLoadCarryingCapacity")


class DynamicAxialLoadCarryingCapacity(_2103.SKFCalculationResult):
    """DynamicAxialLoadCarryingCapacity

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_AXIAL_LOAD_CARRYING_CAPACITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicAxialLoadCarryingCapacity")

    class _Cast_DynamicAxialLoadCarryingCapacity:
        """Special nested class for casting DynamicAxialLoadCarryingCapacity to subclasses."""

        def __init__(
            self: "DynamicAxialLoadCarryingCapacity._Cast_DynamicAxialLoadCarryingCapacity",
            parent: "DynamicAxialLoadCarryingCapacity",
        ):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "DynamicAxialLoadCarryingCapacity._Cast_DynamicAxialLoadCarryingCapacity",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def dynamic_axial_load_carrying_capacity(
            self: "DynamicAxialLoadCarryingCapacity._Cast_DynamicAxialLoadCarryingCapacity",
        ) -> "DynamicAxialLoadCarryingCapacity":
            return self._parent

        def __getattr__(
            self: "DynamicAxialLoadCarryingCapacity._Cast_DynamicAxialLoadCarryingCapacity",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicAxialLoadCarryingCapacity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permissible_axial_load(self: Self) -> "_2100.PermissibleAxialLoad":
        """mastapy.bearings.bearing_results.rolling.skf_module.PermissibleAxialLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicAxialLoadCarryingCapacity._Cast_DynamicAxialLoadCarryingCapacity":
        return self._Cast_DynamicAxialLoadCarryingCapacity(self)
