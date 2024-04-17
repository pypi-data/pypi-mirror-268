"""CylindricalGearTIFFAnalysisDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TIFF_ANALYSIS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "CylindricalGearTIFFAnalysisDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_two_d_fe_analysis import _903
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTIFFAnalysisDutyCycle",)


Self = TypeVar("Self", bound="CylindricalGearTIFFAnalysisDutyCycle")


class CylindricalGearTIFFAnalysisDutyCycle(_1224.GearDesignAnalysis):
    """CylindricalGearTIFFAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TIFF_ANALYSIS_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearTIFFAnalysisDutyCycle")

    class _Cast_CylindricalGearTIFFAnalysisDutyCycle:
        """Special nested class for casting CylindricalGearTIFFAnalysisDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle",
            parent: "CylindricalGearTIFFAnalysisDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle",
        ) -> "_1224.GearDesignAnalysis":
            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle",
        ) -> "CylindricalGearTIFFAnalysisDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalGearTIFFAnalysisDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis(self: Self) -> "_903.CylindricalGearTwoDimensionalFEAnalysis":
        """mastapy.gears.gear_two_d_fe_analysis.CylindricalGearTwoDimensionalFEAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Analysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle":
        return self._Cast_CylindricalGearTIFFAnalysisDutyCycle(self)
