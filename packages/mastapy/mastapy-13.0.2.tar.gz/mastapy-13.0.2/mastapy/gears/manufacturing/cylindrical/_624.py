"""CylindricalManufacturedGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1234
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _628
    from mastapy.gears.rating.cylindrical import _467
    from mastapy.gears.analysis import _1235, _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearSetLoadCase",)


Self = TypeVar("Self", bound="CylindricalManufacturedGearSetLoadCase")


class CylindricalManufacturedGearSetLoadCase(_1234.GearSetImplementationAnalysis):
    """CylindricalManufacturedGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalManufacturedGearSetLoadCase"
    )

    class _Cast_CylindricalManufacturedGearSetLoadCase:
        """Special nested class for casting CylindricalManufacturedGearSetLoadCase to subclasses."""

        def __init__(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
            parent: "CylindricalManufacturedGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
        ) -> "_1234.GearSetImplementationAnalysis":
            return self._parent._cast(_1234.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
        ) -> "_1235.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
        ) -> "CylindricalManufacturedGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedGearSetLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(
        self: Self,
    ) -> "_628.CylindricalSetManufacturingConfig":
        """mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_467.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase":
        return self._Cast_CylindricalManufacturedGearSetLoadCase(self)
