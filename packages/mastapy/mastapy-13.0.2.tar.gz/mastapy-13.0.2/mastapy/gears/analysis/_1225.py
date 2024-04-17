"""GearImplementationAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _620
    from mastapy.gears.manufacturing.bevel import _778
    from mastapy.gears.ltca import _843
    from mastapy.gears.ltca.cylindrical import _859
    from mastapy.gears.ltca.conical import _870
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationAnalysis",)


Self = TypeVar("Self", bound="GearImplementationAnalysis")


class GearImplementationAnalysis(_1224.GearDesignAnalysis):
    """GearImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationAnalysis")

    class _Cast_GearImplementationAnalysis:
        """Special nested class for casting GearImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
            parent: "GearImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_1224.GearDesignAnalysis":
            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_620.CylindricalManufacturedGearLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_778.ConicalGearManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _778

            return self._parent._cast(_778.ConicalGearManufacturingAnalysis)

        @property
        def gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_843.GearLoadDistributionAnalysis":
            from mastapy.gears.ltca import _843

            return self._parent._cast(_843.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_859.CylindricalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _859

            return self._parent._cast(_859.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "_870.ConicalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _870

            return self._parent._cast(_870.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "GearImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationAnalysis._Cast_GearImplementationAnalysis":
        return self._Cast_GearImplementationAnalysis(self)
