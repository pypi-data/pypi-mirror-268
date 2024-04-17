"""CylindricalGearMicroGeometryDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMicroGeometryDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_two_d_fe_analysis import _902
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometryDutyCycle",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometryDutyCycle")


class CylindricalGearMicroGeometryDutyCycle(_1224.GearDesignAnalysis):
    """CylindricalGearMicroGeometryDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMicroGeometryDutyCycle"
    )

    class _Cast_CylindricalGearMicroGeometryDutyCycle:
        """Special nested class for casting CylindricalGearMicroGeometryDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle",
            parent: "CylindricalGearMicroGeometryDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle",
        ) -> "_1224.GearDesignAnalysis":
            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle",
        ) -> "CylindricalGearMicroGeometryDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalGearMicroGeometryDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tiff_analysis(self: Self) -> "_902.CylindricalGearTIFFAnalysisDutyCycle":
        """mastapy.gears.gear_two_d_fe_analysis.CylindricalGearTIFFAnalysisDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle":
        return self._Cast_CylindricalGearMicroGeometryDutyCycle(self)
