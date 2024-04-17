"""GearSetDesignAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetDesignAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _623, _624, _628
    from mastapy.gears.manufacturing.bevel import _793, _794, _795, _796
    from mastapy.gears.ltca import _849
    from mastapy.gears.ltca.cylindrical import _863, _865
    from mastapy.gears.ltca.conical import _871
    from mastapy.gears.load_case import _877
    from mastapy.gears.load_case.worm import _880
    from mastapy.gears.load_case.face import _883
    from mastapy.gears.load_case.cylindrical import _886
    from mastapy.gears.load_case.conical import _889
    from mastapy.gears.load_case.concept import _892
    from mastapy.gears.load_case.bevel import _896
    from mastapy.gears.gear_two_d_fe_analysis import _899, _900
    from mastapy.gears.gear_designs.face import _1000
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113, _1114
    from mastapy.gears.fe_model import _1206
    from mastapy.gears.fe_model.cylindrical import _1209
    from mastapy.gears.fe_model.conical import _1212
    from mastapy.gears.analysis import _1234, _1235, _1236, _1237


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesignAnalysis",)


Self = TypeVar("Self", bound="GearSetDesignAnalysis")


class GearSetDesignAnalysis(_1223.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDesignAnalysis")

    class _Cast_GearSetDesignAnalysis:
        """Special nested class for casting GearSetDesignAnalysis to subclasses."""

        def __init__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
            parent: "GearSetDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1223.AbstractGearSetAnalysis":
            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_623.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_624.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_628.CylindricalSetManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_793.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_794.ConicalSetManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_795.ConicalSetMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _795

            return self._parent._cast(_795.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_796.ConicalSetMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _796

            return self._parent._cast(_796.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_849.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _849

            return self._parent._cast(_849.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_865.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _865

            return self._parent._cast(_865.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_871.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _871

            return self._parent._cast(_871.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_877.GearSetLoadCaseBase":
            from mastapy.gears.load_case import _877

            return self._parent._cast(_877.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_880.WormGearSetLoadCase":
            from mastapy.gears.load_case.worm import _880

            return self._parent._cast(_880.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_883.FaceGearSetLoadCase":
            from mastapy.gears.load_case.face import _883

            return self._parent._cast(_883.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_886.CylindricalGearSetLoadCase":
            from mastapy.gears.load_case.cylindrical import _886

            return self._parent._cast(_886.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_889.ConicalGearSetLoadCase":
            from mastapy.gears.load_case.conical import _889

            return self._parent._cast(_889.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_892.ConceptGearSetLoadCase":
            from mastapy.gears.load_case.concept import _892

            return self._parent._cast(_892.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_896.BevelSetLoadCase":
            from mastapy.gears.load_case.bevel import _896

            return self._parent._cast(_896.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_899.CylindricalGearSetTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _899

            return self._parent._cast(_899.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_900.CylindricalGearSetTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _900

            return self._parent._cast(_900.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1000.FaceGearSetMicroGeometry":
            from mastapy.gears.gear_designs.face import _1000

            return self._parent._cast(_1000.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1113.CylindricalGearSetMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113

            return self._parent._cast(_1113.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1114.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1206.GearSetFEModel":
            from mastapy.gears.fe_model import _1206

            return self._parent._cast(_1206.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1209.CylindricalGearSetFEModel":
            from mastapy.gears.fe_model.cylindrical import _1209

            return self._parent._cast(_1209.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1212.ConicalSetFEModel":
            from mastapy.gears.fe_model.conical import _1212

            return self._parent._cast(_1212.ConicalSetFEModel)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1234.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1234

            return self._parent._cast(_1234.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1235.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1236.GearSetImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1237.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1237

            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "GearSetDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis":
        return self._Cast_GearSetDesignAnalysis(self)
