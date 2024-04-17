"""ConicalGearManufacturingAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearManufacturingAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearManufacturingAnalysis",)


Self = TypeVar("Self", bound="ConicalGearManufacturingAnalysis")


class ConicalGearManufacturingAnalysis(_1225.GearImplementationAnalysis):
    """ConicalGearManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearManufacturingAnalysis")

    class _Cast_ConicalGearManufacturingAnalysis:
        """Special nested class for casting ConicalGearManufacturingAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis",
            parent: "ConicalGearManufacturingAnalysis",
        ):
            self._parent = parent

        @property
        def gear_implementation_analysis(
            self: "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis",
        ) -> "_1225.GearImplementationAnalysis":
            return self._parent._cast(_1225.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def conical_gear_manufacturing_analysis(
            self: "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis",
        ) -> "ConicalGearManufacturingAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearManufacturingAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis":
        return self._Cast_ConicalGearManufacturingAnalysis(self)
