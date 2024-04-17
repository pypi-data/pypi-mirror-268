"""ConicalGearManufacturingControlParameters"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_CONTROL_PARAMETERS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters",
    "ConicalGearManufacturingControlParameters",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel.control_parameters import _821, _822, _823


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearManufacturingControlParameters",)


Self = TypeVar("Self", bound="ConicalGearManufacturingControlParameters")


class ConicalGearManufacturingControlParameters(_0.APIBase):
    """ConicalGearManufacturingControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_CONTROL_PARAMETERS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearManufacturingControlParameters"
    )

    class _Cast_ConicalGearManufacturingControlParameters:
        """Special nested class for casting ConicalGearManufacturingControlParameters to subclasses."""

        def __init__(
            self: "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters",
            parent: "ConicalGearManufacturingControlParameters",
        ):
            self._parent = parent

        @property
        def conical_manufacturing_sgm_control_parameters(
            self: "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters",
        ) -> "_821.ConicalManufacturingSGMControlParameters":
            from mastapy.gears.manufacturing.bevel.control_parameters import _821

            return self._parent._cast(_821.ConicalManufacturingSGMControlParameters)

        @property
        def conical_manufacturing_sgt_control_parameters(
            self: "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters",
        ) -> "_822.ConicalManufacturingSGTControlParameters":
            from mastapy.gears.manufacturing.bevel.control_parameters import _822

            return self._parent._cast(_822.ConicalManufacturingSGTControlParameters)

        @property
        def conical_manufacturing_smt_control_parameters(
            self: "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters",
        ) -> "_823.ConicalManufacturingSMTControlParameters":
            from mastapy.gears.manufacturing.bevel.control_parameters import _823

            return self._parent._cast(_823.ConicalManufacturingSMTControlParameters)

        @property
        def conical_gear_manufacturing_control_parameters(
            self: "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters",
        ) -> "ConicalGearManufacturingControlParameters":
            return self._parent

        def __getattr__(
            self: "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters",
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
        self: Self, instance_to_wrap: "ConicalGearManufacturingControlParameters.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_factor_of_contact_pattern(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LengthFactorOfContactPattern

        if temp is None:
            return 0.0

        return temp

    @length_factor_of_contact_pattern.setter
    @enforce_parameter_types
    def length_factor_of_contact_pattern(self: Self, value: "float"):
        self.wrapped.LengthFactorOfContactPattern = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_root_relief_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionRootReliefLength

        if temp is None:
            return 0.0

        return temp

    @pinion_root_relief_length.setter
    @enforce_parameter_types
    def pinion_root_relief_length(self: Self, value: "float"):
        self.wrapped.PinionRootReliefLength = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters":
        return self._Cast_ConicalGearManufacturingControlParameters(self)
