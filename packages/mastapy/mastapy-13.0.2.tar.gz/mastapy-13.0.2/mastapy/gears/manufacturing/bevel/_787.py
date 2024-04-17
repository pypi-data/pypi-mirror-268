"""ConicalMeshManufacturingAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshManufacturingAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case.conical import _890
    from mastapy.gears.manufacturing.bevel import _798, _782
    from mastapy.gears.analysis import _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshManufacturingAnalysis",)


Self = TypeVar("Self", bound="ConicalMeshManufacturingAnalysis")


class ConicalMeshManufacturingAnalysis(_1229.GearMeshImplementationAnalysis):
    """ConicalMeshManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshManufacturingAnalysis")

    class _Cast_ConicalMeshManufacturingAnalysis:
        """Special nested class for casting ConicalMeshManufacturingAnalysis to subclasses."""

        def __init__(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
            parent: "ConicalMeshManufacturingAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ) -> "_1229.GearMeshImplementationAnalysis":
            return self._parent._cast(_1229.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ) -> "ConicalMeshManufacturingAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshManufacturingAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_load_case(self: Self) -> "_890.ConicalMeshLoadCase":
        """mastapy.gears.load_case.conical.ConicalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tca(self: Self) -> "_798.EaseOffBasedTCA":
        """mastapy.gears.manufacturing.bevel.EaseOffBasedTCA

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(self: Self) -> "List[_782.ConicalMeshedGearManufacturingAnalysis]":
        """List[mastapy.gears.manufacturing.bevel.ConicalMeshedGearManufacturingAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis":
        return self._Cast_ConicalMeshManufacturingAnalysis(self)
