"""AbstractGearSetAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearSetAnalysis"
)

if TYPE_CHECKING:
    from mastapy.utility.model_validation import _1801, _1800
    from mastapy.gears.rating import _358, _365, _366
    from mastapy.gears.rating.zerol_bevel import _374
    from mastapy.gears.rating.worm import _378, _379
    from mastapy.gears.rating.straight_bevel import _400
    from mastapy.gears.rating.straight_bevel_diff import _403
    from mastapy.gears.rating.spiral_bevel import _407
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_hypoid import _413
    from mastapy.gears.rating.klingelnberg_conical import _416
    from mastapy.gears.rating.hypoid import _443
    from mastapy.gears.rating.face import _452, _453
    from mastapy.gears.rating.cylindrical import _466, _467, _483
    from mastapy.gears.rating.conical import _544, _545
    from mastapy.gears.rating.concept import _555, _556
    from mastapy.gears.rating.bevel import _559
    from mastapy.gears.rating.agma_gleason_conical import _570
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
    from mastapy.gears.analysis import _1232, _1234, _1235, _1236, _1237


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetAnalysis",)


Self = TypeVar("Self", bound="AbstractGearSetAnalysis")


class AbstractGearSetAnalysis(_0.APIBase):
    """AbstractGearSetAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetAnalysis")

    class _Cast_AbstractGearSetAnalysis:
        """Special nested class for casting AbstractGearSetAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
            parent: "AbstractGearSetAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_365.GearSetDutyCycleRating":
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.GearSetDutyCycleRating)

        @property
        def gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_366.GearSetRating":
            from mastapy.gears.rating import _366

            return self._parent._cast(_366.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_374.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _374

            return self._parent._cast(_374.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_378.WormGearSetDutyCycleRating":
            from mastapy.gears.rating.worm import _378

            return self._parent._cast(_378.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_379.WormGearSetRating":
            from mastapy.gears.rating.worm import _379

            return self._parent._cast(_379.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_400.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _400

            return self._parent._cast(_400.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_403.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _403

            return self._parent._cast(_403.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_407.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _407

            return self._parent._cast(_407.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _410

            return self._parent._cast(
                _410.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_413.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _413

            return self._parent._cast(_413.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_416.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_443.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _443

            return self._parent._cast(_443.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_452.FaceGearSetDutyCycleRating":
            from mastapy.gears.rating.face import _452

            return self._parent._cast(_452.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_453.FaceGearSetRating":
            from mastapy.gears.rating.face import _453

            return self._parent._cast(_453.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_466.CylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _466

            return self._parent._cast(_466.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_467.CylindricalGearSetRating":
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_483.ReducedCylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _483

            return self._parent._cast(_483.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_544.ConicalGearSetDutyCycleRating":
            from mastapy.gears.rating.conical import _544

            return self._parent._cast(_544.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_545.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_555.ConceptGearSetDutyCycleRating":
            from mastapy.gears.rating.concept import _555

            return self._parent._cast(_555.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_556.ConceptGearSetRating":
            from mastapy.gears.rating.concept import _556

            return self._parent._cast(_556.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_559.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _559

            return self._parent._cast(_559.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_570.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _570

            return self._parent._cast(_570.AGMAGleasonConicalGearSetRating)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_623.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_624.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_628.CylindricalSetManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_793.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_794.ConicalSetManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_795.ConicalSetMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _795

            return self._parent._cast(_795.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_796.ConicalSetMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _796

            return self._parent._cast(_796.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_849.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _849

            return self._parent._cast(_849.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_865.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _865

            return self._parent._cast(_865.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_871.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _871

            return self._parent._cast(_871.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_877.GearSetLoadCaseBase":
            from mastapy.gears.load_case import _877

            return self._parent._cast(_877.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_880.WormGearSetLoadCase":
            from mastapy.gears.load_case.worm import _880

            return self._parent._cast(_880.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_883.FaceGearSetLoadCase":
            from mastapy.gears.load_case.face import _883

            return self._parent._cast(_883.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_886.CylindricalGearSetLoadCase":
            from mastapy.gears.load_case.cylindrical import _886

            return self._parent._cast(_886.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_889.ConicalGearSetLoadCase":
            from mastapy.gears.load_case.conical import _889

            return self._parent._cast(_889.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_892.ConceptGearSetLoadCase":
            from mastapy.gears.load_case.concept import _892

            return self._parent._cast(_892.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_896.BevelSetLoadCase":
            from mastapy.gears.load_case.bevel import _896

            return self._parent._cast(_896.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_899.CylindricalGearSetTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _899

            return self._parent._cast(_899.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_900.CylindricalGearSetTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _900

            return self._parent._cast(_900.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1000.FaceGearSetMicroGeometry":
            from mastapy.gears.gear_designs.face import _1000

            return self._parent._cast(_1000.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1113.CylindricalGearSetMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113

            return self._parent._cast(_1113.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1114.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1206.GearSetFEModel":
            from mastapy.gears.fe_model import _1206

            return self._parent._cast(_1206.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1209.CylindricalGearSetFEModel":
            from mastapy.gears.fe_model.cylindrical import _1209

            return self._parent._cast(_1209.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1212.ConicalSetFEModel":
            from mastapy.gears.fe_model.conical import _1212

            return self._parent._cast(_1212.ConicalSetFEModel)

        @property
        def gear_set_design_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1234.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1234

            return self._parent._cast(_1234.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1235.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1236.GearSetImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1237.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1237

            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "AbstractGearSetAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def all_status_errors(self: Self) -> "List[_1801.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1800.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis":
        return self._Cast_AbstractGearSetAnalysis(self)
