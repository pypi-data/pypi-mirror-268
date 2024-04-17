"""GearMeshImplementationAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _622
    from mastapy.gears.manufacturing.bevel import _787
    from mastapy.gears.ltca import _844
    from mastapy.gears.ltca.cylindrical import _860
    from mastapy.gears.ltca.conical import _873
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationAnalysis",)


Self = TypeVar("Self", bound="GearMeshImplementationAnalysis")


class GearMeshImplementationAnalysis(_1228.GearMeshDesignAnalysis):
    """GearMeshImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshImplementationAnalysis")

    class _Cast_GearMeshImplementationAnalysis:
        """Special nested class for casting GearMeshImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
            parent: "GearMeshImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_1228.GearMeshDesignAnalysis":
            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_622.CylindricalManufacturedGearMeshLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalManufacturedGearMeshLoadCase)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_787.ConicalMeshManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalMeshManufacturingAnalysis)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_844.GearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca import _844

            return self._parent._cast(_844.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_860.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_873.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _873

            return self._parent._cast(_873.ConicalMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "GearMeshImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis":
        return self._Cast_GearMeshImplementationAnalysis(self)
