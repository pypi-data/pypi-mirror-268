"""GearSetImplementationAnalysisAbstract"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysisAbstract"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _623, _624
    from mastapy.gears.manufacturing.bevel import _793
    from mastapy.gears.ltca import _849
    from mastapy.gears.ltca.cylindrical import _863, _865
    from mastapy.gears.ltca.conical import _871
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114
    from mastapy.gears.analysis import _1234, _1236, _1223


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysisAbstract",)


Self = TypeVar("Self", bound="GearSetImplementationAnalysisAbstract")


class GearSetImplementationAnalysisAbstract(_1232.GearSetDesignAnalysis):
    """GearSetImplementationAnalysisAbstract

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetImplementationAnalysisAbstract"
    )

    class _Cast_GearSetImplementationAnalysisAbstract:
        """Special nested class for casting GearSetImplementationAnalysisAbstract to subclasses."""

        def __init__(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
            parent: "GearSetImplementationAnalysisAbstract",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1232.GearSetDesignAnalysis":
            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_623.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_624.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_793.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_849.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _849

            return self._parent._cast(_849.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_865.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _865

            return self._parent._cast(_865.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_871.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _871

            return self._parent._cast(_871.ConicalGearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1114.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1234.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1234

            return self._parent._cast(_1234.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1236.GearSetImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "GearSetImplementationAnalysisAbstract":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
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
        self: Self, instance_to_wrap: "GearSetImplementationAnalysisAbstract.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract":
        return self._Cast_GearSetImplementationAnalysisAbstract(self)
