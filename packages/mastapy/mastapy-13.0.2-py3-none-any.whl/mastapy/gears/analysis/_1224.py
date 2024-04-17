"""GearDesignAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearDesignAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _615, _619, _620
    from mastapy.gears.manufacturing.bevel import (
        _778,
        _779,
        _780,
        _781,
        _791,
        _792,
        _797,
    )
    from mastapy.gears.ltca import _843
    from mastapy.gears.ltca.cylindrical import _859
    from mastapy.gears.ltca.conical import _870
    from mastapy.gears.load_case import _876
    from mastapy.gears.load_case.worm import _879
    from mastapy.gears.load_case.face import _882
    from mastapy.gears.load_case.cylindrical import _885
    from mastapy.gears.load_case.conical import _888
    from mastapy.gears.load_case.concept import _891
    from mastapy.gears.load_case.bevel import _894
    from mastapy.gears.gear_two_d_fe_analysis import _901, _902
    from mastapy.gears.gear_designs.face import _997
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1106,
        _1107,
        _1108,
        _1110,
    )
    from mastapy.gears.fe_model import _1203
    from mastapy.gears.fe_model.cylindrical import _1207
    from mastapy.gears.fe_model.conical import _1210
    from mastapy.gears.analysis import _1225, _1226, _1227


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignAnalysis",)


Self = TypeVar("Self", bound="GearDesignAnalysis")


class GearDesignAnalysis(_1221.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignAnalysis")

    class _Cast_GearDesignAnalysis:
        """Special nested class for casting GearDesignAnalysis to subclasses."""

        def __init__(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
            parent: "GearDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1221.AbstractGearAnalysis":
            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_615.CylindricalGearManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_619.CylindricalManufacturedGearDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_620.CylindricalManufacturedGearLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_778.ConicalGearManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _778

            return self._parent._cast(_778.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_779.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _779

            return self._parent._cast(_779.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_780.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _780

            return self._parent._cast(_780.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_781.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _781

            return self._parent._cast(_781.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_791.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_792.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_797.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_843.GearLoadDistributionAnalysis":
            from mastapy.gears.ltca import _843

            return self._parent._cast(_843.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_859.CylindricalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _859

            return self._parent._cast(_859.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_870.ConicalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _870

            return self._parent._cast(_870.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_876.GearLoadCaseBase":
            from mastapy.gears.load_case import _876

            return self._parent._cast(_876.GearLoadCaseBase)

        @property
        def worm_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_879.WormGearLoadCase":
            from mastapy.gears.load_case.worm import _879

            return self._parent._cast(_879.WormGearLoadCase)

        @property
        def face_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_882.FaceGearLoadCase":
            from mastapy.gears.load_case.face import _882

            return self._parent._cast(_882.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_885.CylindricalGearLoadCase":
            from mastapy.gears.load_case.cylindrical import _885

            return self._parent._cast(_885.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_888.ConicalGearLoadCase":
            from mastapy.gears.load_case.conical import _888

            return self._parent._cast(_888.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_891.ConceptGearLoadCase":
            from mastapy.gears.load_case.concept import _891

            return self._parent._cast(_891.ConceptGearLoadCase)

        @property
        def bevel_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_894.BevelLoadCase":
            from mastapy.gears.load_case.bevel import _894

            return self._parent._cast(_894.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_901.CylindricalGearTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _901

            return self._parent._cast(_901.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_902.CylindricalGearTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _902

            return self._parent._cast(_902.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_997.FaceGearMicroGeometry":
            from mastapy.gears.gear_designs.face import _997

            return self._parent._cast(_997.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1106.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106

            return self._parent._cast(_1106.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1107.CylindricalGearMicroGeometryBase":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107

            return self._parent._cast(_1107.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1108.CylindricalGearMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108

            return self._parent._cast(_1108.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1110.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110

            return self._parent._cast(_1110.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1203.GearFEModel":
            from mastapy.gears.fe_model import _1203

            return self._parent._cast(_1203.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1207.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1207

            return self._parent._cast(_1207.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1210.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1210

            return self._parent._cast(_1210.ConicalGearFEModel)

        @property
        def gear_implementation_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1225.GearImplementationAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1226.GearImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1227.GearImplementationDetail":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "GearDesignAnalysis":
            return self._parent

        def __getattr__(self: "GearDesignAnalysis._Cast_GearDesignAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearDesignAnalysis._Cast_GearDesignAnalysis":
        return self._Cast_GearDesignAnalysis(self)
