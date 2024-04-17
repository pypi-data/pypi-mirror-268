"""CylindricalGearMeshTIFFAnalysisDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_TIFF_ANALYSIS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "CylindricalGearMeshTIFFAnalysisDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshTIFFAnalysisDutyCycle",)


Self = TypeVar("Self", bound="CylindricalGearMeshTIFFAnalysisDutyCycle")


class CylindricalGearMeshTIFFAnalysisDutyCycle(_1228.GearMeshDesignAnalysis):
    """CylindricalGearMeshTIFFAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_TIFF_ANALYSIS_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshTIFFAnalysisDutyCycle"
    )

    class _Cast_CylindricalGearMeshTIFFAnalysisDutyCycle:
        """Special nested class for casting CylindricalGearMeshTIFFAnalysisDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalGearMeshTIFFAnalysisDutyCycle._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle",
            parent: "CylindricalGearMeshTIFFAnalysisDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalGearMeshTIFFAnalysisDutyCycle._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle",
        ) -> "_1228.GearMeshDesignAnalysis":
            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalGearMeshTIFFAnalysisDutyCycle._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "CylindricalGearMeshTIFFAnalysisDutyCycle._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle",
        ) -> "CylindricalGearMeshTIFFAnalysisDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshTIFFAnalysisDutyCycle._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshTIFFAnalysisDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshTIFFAnalysisDutyCycle._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle":
        return self._Cast_CylindricalGearMeshTIFFAnalysisDutyCycle(self)
