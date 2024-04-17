"""BevelMachineSettingOptimizationResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_MACHINE_SETTING_OPTIMIZATION_RESULT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "BevelMachineSettingOptimizationResult"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _777


__docformat__ = "restructuredtext en"
__all__ = ("BevelMachineSettingOptimizationResult",)


Self = TypeVar("Self", bound="BevelMachineSettingOptimizationResult")


class BevelMachineSettingOptimizationResult(_0.APIBase):
    """BevelMachineSettingOptimizationResult

    This is a mastapy class.
    """

    TYPE = _BEVEL_MACHINE_SETTING_OPTIMIZATION_RESULT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelMachineSettingOptimizationResult"
    )

    class _Cast_BevelMachineSettingOptimizationResult:
        """Special nested class for casting BevelMachineSettingOptimizationResult to subclasses."""

        def __init__(
            self: "BevelMachineSettingOptimizationResult._Cast_BevelMachineSettingOptimizationResult",
            parent: "BevelMachineSettingOptimizationResult",
        ):
            self._parent = parent

        @property
        def bevel_machine_setting_optimization_result(
            self: "BevelMachineSettingOptimizationResult._Cast_BevelMachineSettingOptimizationResult",
        ) -> "BevelMachineSettingOptimizationResult":
            return self._parent

        def __getattr__(
            self: "BevelMachineSettingOptimizationResult._Cast_BevelMachineSettingOptimizationResult",
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
        self: Self, instance_to_wrap: "BevelMachineSettingOptimizationResult.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_absolute_residual(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAbsoluteResidual

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_squared_residuals(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfSquaredResiduals

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_deviations_concave(self: Self) -> "_777.ConicalFlankDeviationsData":
        """mastapy.gears.manufacturing.bevel.ConicalFlankDeviationsData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedDeviationsConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def calculated_deviations_convex(self: Self) -> "_777.ConicalFlankDeviationsData":
        """mastapy.gears.manufacturing.bevel.ConicalFlankDeviationsData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedDeviationsConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def imported_deviations_concave(self: Self) -> "_777.ConicalFlankDeviationsData":
        """mastapy.gears.manufacturing.bevel.ConicalFlankDeviationsData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImportedDeviationsConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def imported_deviations_convex(self: Self) -> "_777.ConicalFlankDeviationsData":
        """mastapy.gears.manufacturing.bevel.ConicalFlankDeviationsData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImportedDeviationsConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelMachineSettingOptimizationResult._Cast_BevelMachineSettingOptimizationResult":
        return self._Cast_BevelMachineSettingOptimizationResult(self)
