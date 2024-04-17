"""ConicalGearBiasModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.micro_geometry import _572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_BIAS_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry",
    "ConicalGearBiasModification",
)

if TYPE_CHECKING:
    from mastapy.gears.micro_geometry import _582


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearBiasModification",)


Self = TypeVar("Self", bound="ConicalGearBiasModification")


class ConicalGearBiasModification(_572.BiasModification):
    """ConicalGearBiasModification

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_BIAS_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearBiasModification")

    class _Cast_ConicalGearBiasModification:
        """Special nested class for casting ConicalGearBiasModification to subclasses."""

        def __init__(
            self: "ConicalGearBiasModification._Cast_ConicalGearBiasModification",
            parent: "ConicalGearBiasModification",
        ):
            self._parent = parent

        @property
        def bias_modification(
            self: "ConicalGearBiasModification._Cast_ConicalGearBiasModification",
        ) -> "_572.BiasModification":
            return self._parent._cast(_572.BiasModification)

        @property
        def modification(
            self: "ConicalGearBiasModification._Cast_ConicalGearBiasModification",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def conical_gear_bias_modification(
            self: "ConicalGearBiasModification._Cast_ConicalGearBiasModification",
        ) -> "ConicalGearBiasModification":
            return self._parent

        def __getattr__(
            self: "ConicalGearBiasModification._Cast_ConicalGearBiasModification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearBiasModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def constant_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ConstantRelief

        if temp is None:
            return 0.0

        return temp

    @constant_relief.setter
    @enforce_parameter_types
    def constant_relief(self: Self, value: "float"):
        self.wrapped.ConstantRelief = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearBiasModification._Cast_ConicalGearBiasModification":
        return self._Cast_ConicalGearBiasModification(self)
