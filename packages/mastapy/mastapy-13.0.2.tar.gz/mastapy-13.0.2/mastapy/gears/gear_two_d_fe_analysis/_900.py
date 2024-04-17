"""CylindricalGearSetTIFFAnalysisDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.analysis import _1232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "CylindricalGearSetTIFFAnalysisDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_two_d_fe_analysis import _902
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetTIFFAnalysisDutyCycle",)


Self = TypeVar("Self", bound="CylindricalGearSetTIFFAnalysisDutyCycle")


class CylindricalGearSetTIFFAnalysisDutyCycle(_1232.GearSetDesignAnalysis):
    """CylindricalGearSetTIFFAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetTIFFAnalysisDutyCycle"
    )

    class _Cast_CylindricalGearSetTIFFAnalysisDutyCycle:
        """Special nested class for casting CylindricalGearSetTIFFAnalysisDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle",
            parent: "CylindricalGearSetTIFFAnalysisDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle",
        ) -> "_1232.GearSetDesignAnalysis":
            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle",
        ) -> "CylindricalGearSetTIFFAnalysisDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalGearSetTIFFAnalysisDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self: Self) -> "List[_902.CylindricalGearTIFFAnalysisDutyCycle]":
        """List[mastapy.gears.gear_two_d_fe_analysis.CylindricalGearTIFFAnalysisDutyCycle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle":
        return self._Cast_CylindricalGearSetTIFFAnalysisDutyCycle(self)
