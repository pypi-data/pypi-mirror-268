"""CylindricalGearMeshTIFFAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_TIFF_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "CylindricalGearMeshTIFFAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshTIFFAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMeshTIFFAnalysis")


class CylindricalGearMeshTIFFAnalysis(_1228.GearMeshDesignAnalysis):
    """CylindricalGearMeshTIFFAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_TIFF_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshTIFFAnalysis")

    class _Cast_CylindricalGearMeshTIFFAnalysis:
        """Special nested class for casting CylindricalGearMeshTIFFAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis",
            parent: "CylindricalGearMeshTIFFAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis",
        ) -> "_1228.GearMeshDesignAnalysis":
            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis",
        ) -> "CylindricalGearMeshTIFFAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshTIFFAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis":
        return self._Cast_CylindricalGearMeshTIFFAnalysis(self)
