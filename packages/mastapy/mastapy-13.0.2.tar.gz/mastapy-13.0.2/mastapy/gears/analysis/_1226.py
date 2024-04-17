"""GearImplementationAnalysisDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationAnalysisDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _619
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationAnalysisDutyCycle",)


Self = TypeVar("Self", bound="GearImplementationAnalysisDutyCycle")


class GearImplementationAnalysisDutyCycle(_1224.GearDesignAnalysis):
    """GearImplementationAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationAnalysisDutyCycle")

    class _Cast_GearImplementationAnalysisDutyCycle:
        """Special nested class for casting GearImplementationAnalysisDutyCycle to subclasses."""

        def __init__(
            self: "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle",
            parent: "GearImplementationAnalysisDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle",
        ) -> "_1224.GearDesignAnalysis":
            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle",
        ) -> "_619.CylindricalManufacturedGearDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearDutyCycle)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle",
        ) -> "GearImplementationAnalysisDutyCycle":
            return self._parent

        def __getattr__(
            self: "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle",
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
        self: Self, instance_to_wrap: "GearImplementationAnalysisDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle"
    ):
        return self._Cast_GearImplementationAnalysisDutyCycle(self)
