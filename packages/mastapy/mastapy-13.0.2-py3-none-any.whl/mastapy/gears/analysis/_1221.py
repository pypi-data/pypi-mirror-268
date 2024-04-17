"""AbstractGearAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _357, _361, _364
    from mastapy.gears.rating.zerol_bevel import _373
    from mastapy.gears.rating.worm import _375, _377
    from mastapy.gears.rating.straight_bevel import _399
    from mastapy.gears.rating.straight_bevel_diff import _402
    from mastapy.gears.rating.spiral_bevel import _406
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
    from mastapy.gears.rating.klingelnberg_hypoid import _412
    from mastapy.gears.rating.klingelnberg_conical import _415
    from mastapy.gears.rating.hypoid import _442
    from mastapy.gears.rating.face import _448, _451
    from mastapy.gears.rating.cylindrical import _458, _463
    from mastapy.gears.rating.conical import _541, _543
    from mastapy.gears.rating.concept import _551, _554
    from mastapy.gears.rating.bevel import _558
    from mastapy.gears.rating.agma_gleason_conical import _569
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
    from mastapy.gears.analysis import _1224, _1225, _1226, _1227


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearAnalysis",)


Self = TypeVar("Self", bound="AbstractGearAnalysis")


class AbstractGearAnalysis(_0.APIBase):
    """AbstractGearAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearAnalysis")

    class _Cast_AbstractGearAnalysis:
        """Special nested class for casting AbstractGearAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
            parent: "AbstractGearAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_361.GearDutyCycleRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearDutyCycleRating)

        @property
        def gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_364.GearRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearRating)

        @property
        def zerol_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_373.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _373

            return self._parent._cast(_373.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_375.WormGearDutyCycleRating":
            from mastapy.gears.rating.worm import _375

            return self._parent._cast(_375.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_377.WormGearRating":
            from mastapy.gears.rating.worm import _377

            return self._parent._cast(_377.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_399.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _399

            return self._parent._cast(_399.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_402.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _402

            return self._parent._cast(_402.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_406.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _406

            return self._parent._cast(_406.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_409.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _409

            return self._parent._cast(
                _409.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_412.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _412

            return self._parent._cast(_412.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_415.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _415

            return self._parent._cast(_415.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_442.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _442

            return self._parent._cast(_442.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_448.FaceGearDutyCycleRating":
            from mastapy.gears.rating.face import _448

            return self._parent._cast(_448.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_451.FaceGearRating":
            from mastapy.gears.rating.face import _451

            return self._parent._cast(_451.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_458.CylindricalGearDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _458

            return self._parent._cast(_458.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_463.CylindricalGearRating":
            from mastapy.gears.rating.cylindrical import _463

            return self._parent._cast(_463.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_541.ConicalGearDutyCycleRating":
            from mastapy.gears.rating.conical import _541

            return self._parent._cast(_541.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_543.ConicalGearRating":
            from mastapy.gears.rating.conical import _543

            return self._parent._cast(_543.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_551.ConceptGearDutyCycleRating":
            from mastapy.gears.rating.concept import _551

            return self._parent._cast(_551.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_554.ConceptGearRating":
            from mastapy.gears.rating.concept import _554

            return self._parent._cast(_554.ConceptGearRating)

        @property
        def bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_558.BevelGearRating":
            from mastapy.gears.rating.bevel import _558

            return self._parent._cast(_558.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_569.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _569

            return self._parent._cast(_569.AGMAGleasonConicalGearRating)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_615.CylindricalGearManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_619.CylindricalManufacturedGearDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_620.CylindricalManufacturedGearLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_778.ConicalGearManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _778

            return self._parent._cast(_778.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_779.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _779

            return self._parent._cast(_779.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_780.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _780

            return self._parent._cast(_780.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_781.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _781

            return self._parent._cast(_781.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_791.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_792.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_797.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_843.GearLoadDistributionAnalysis":
            from mastapy.gears.ltca import _843

            return self._parent._cast(_843.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_859.CylindricalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _859

            return self._parent._cast(_859.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_870.ConicalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _870

            return self._parent._cast(_870.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_876.GearLoadCaseBase":
            from mastapy.gears.load_case import _876

            return self._parent._cast(_876.GearLoadCaseBase)

        @property
        def worm_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_879.WormGearLoadCase":
            from mastapy.gears.load_case.worm import _879

            return self._parent._cast(_879.WormGearLoadCase)

        @property
        def face_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_882.FaceGearLoadCase":
            from mastapy.gears.load_case.face import _882

            return self._parent._cast(_882.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_885.CylindricalGearLoadCase":
            from mastapy.gears.load_case.cylindrical import _885

            return self._parent._cast(_885.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_888.ConicalGearLoadCase":
            from mastapy.gears.load_case.conical import _888

            return self._parent._cast(_888.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_891.ConceptGearLoadCase":
            from mastapy.gears.load_case.concept import _891

            return self._parent._cast(_891.ConceptGearLoadCase)

        @property
        def bevel_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_894.BevelLoadCase":
            from mastapy.gears.load_case.bevel import _894

            return self._parent._cast(_894.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_901.CylindricalGearTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _901

            return self._parent._cast(_901.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_902.CylindricalGearTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _902

            return self._parent._cast(_902.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_997.FaceGearMicroGeometry":
            from mastapy.gears.gear_designs.face import _997

            return self._parent._cast(_997.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1106.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106

            return self._parent._cast(_1106.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1107.CylindricalGearMicroGeometryBase":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107

            return self._parent._cast(_1107.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1108.CylindricalGearMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108

            return self._parent._cast(_1108.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1110.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110

            return self._parent._cast(_1110.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1203.GearFEModel":
            from mastapy.gears.fe_model import _1203

            return self._parent._cast(_1203.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1207.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1207

            return self._parent._cast(_1207.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1210.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1210

            return self._parent._cast(_1210.ConicalGearFEModel)

        @property
        def gear_design_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def gear_implementation_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1225.GearImplementationAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1226.GearImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1227.GearImplementationDetail":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def abstract_gear_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "AbstractGearAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def name_with_gear_set_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NameWithGearSetName

        if temp is None:
            return ""

        return temp

    @property
    def planet_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PlanetIndex

        if temp is None:
            return 0

        return temp

    @planet_index.setter
    @enforce_parameter_types
    def planet_index(self: Self, value: "int"):
        self.wrapped.PlanetIndex = int(value) if value is not None else 0

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
    def cast_to(self: Self) -> "AbstractGearAnalysis._Cast_AbstractGearAnalysis":
        return self._Cast_AbstractGearAnalysis(self)
