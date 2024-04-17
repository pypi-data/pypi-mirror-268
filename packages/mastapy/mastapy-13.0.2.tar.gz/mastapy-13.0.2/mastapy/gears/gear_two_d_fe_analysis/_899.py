"""CylindricalGearSetTIFFAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.analysis import _1232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "CylindricalGearSetTIFFAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_two_d_fe_analysis import _901
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetTIFFAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetTIFFAnalysis")


class CylindricalGearSetTIFFAnalysis(_1232.GearSetDesignAnalysis):
    """CylindricalGearSetTIFFAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetTIFFAnalysis")

    class _Cast_CylindricalGearSetTIFFAnalysis:
        """Special nested class for casting CylindricalGearSetTIFFAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis",
            parent: "CylindricalGearSetTIFFAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis",
        ) -> "_1232.GearSetDesignAnalysis":
            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis",
        ) -> "CylindricalGearSetTIFFAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetTIFFAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self: Self) -> "List[_901.CylindricalGearTIFFAnalysis]":
        """List[mastapy.gears.gear_two_d_fe_analysis.CylindricalGearTIFFAnalysis]

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
    ) -> "CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis":
        return self._Cast_CylindricalGearSetTIFFAnalysis(self)
