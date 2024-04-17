"""AbstractGearMeshAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearMeshAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1221, _1228, _1229, _1230, _1231
    from mastapy.gears.rating import _356, _363, _368
    from mastapy.gears.rating.zerol_bevel import _372
    from mastapy.gears.rating.worm import _376, _380
    from mastapy.gears.rating.straight_bevel import _398
    from mastapy.gears.rating.straight_bevel_diff import _401
    from mastapy.gears.rating.spiral_bevel import _405
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _408
    from mastapy.gears.rating.klingelnberg_hypoid import _411
    from mastapy.gears.rating.klingelnberg_conical import _414
    from mastapy.gears.rating.hypoid import _441
    from mastapy.gears.rating.face import _449, _450
    from mastapy.gears.rating.cylindrical import _461, _469
    from mastapy.gears.rating.conical import _542, _547
    from mastapy.gears.rating.concept import _552, _553
    from mastapy.gears.rating.bevel import _557
    from mastapy.gears.rating.agma_gleason_conical import _568
    from mastapy.gears.manufacturing.cylindrical import _621, _622, _625
    from mastapy.gears.manufacturing.bevel import _787, _788, _789, _790
    from mastapy.gears.ltca import _844
    from mastapy.gears.ltca.cylindrical import _860
    from mastapy.gears.ltca.conical import _873
    from mastapy.gears.load_case import _878
    from mastapy.gears.load_case.worm import _881
    from mastapy.gears.load_case.face import _884
    from mastapy.gears.load_case.cylindrical import _887
    from mastapy.gears.load_case.conical import _890
    from mastapy.gears.load_case.concept import _893
    from mastapy.gears.load_case.bevel import _895
    from mastapy.gears.gear_two_d_fe_analysis import _897, _898
    from mastapy.gears.gear_designs.face import _996
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104, _1105
    from mastapy.gears.fe_model import _1204
    from mastapy.gears.fe_model.cylindrical import _1208
    from mastapy.gears.fe_model.conical import _1211


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshAnalysis",)


Self = TypeVar("Self", bound="AbstractGearMeshAnalysis")


class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshAnalysis")

    class _Cast_AbstractGearMeshAnalysis:
        """Special nested class for casting AbstractGearMeshAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
            parent: "AbstractGearMeshAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_368.MeshDutyCycleRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_372.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _372

            return self._parent._cast(_372.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_376.WormGearMeshRating":
            from mastapy.gears.rating.worm import _376

            return self._parent._cast(_376.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_380.WormMeshDutyCycleRating":
            from mastapy.gears.rating.worm import _380

            return self._parent._cast(_380.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_398.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _398

            return self._parent._cast(_398.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_401.StraightBevelDiffGearMeshRating":
            from mastapy.gears.rating.straight_bevel_diff import _401

            return self._parent._cast(_401.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_405.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _405

            return self._parent._cast(_405.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _408

            return self._parent._cast(
                _408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_411.KlingelnbergCycloPalloidHypoidGearMeshRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _411

            return self._parent._cast(_411.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_414.KlingelnbergCycloPalloidConicalGearMeshRating":
            from mastapy.gears.rating.klingelnberg_conical import _414

            return self._parent._cast(
                _414.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_441.HypoidGearMeshRating":
            from mastapy.gears.rating.hypoid import _441

            return self._parent._cast(_441.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_449.FaceGearMeshDutyCycleRating":
            from mastapy.gears.rating.face import _449

            return self._parent._cast(_449.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_450.FaceGearMeshRating":
            from mastapy.gears.rating.face import _450

            return self._parent._cast(_450.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_461.CylindricalGearMeshRating":
            from mastapy.gears.rating.cylindrical import _461

            return self._parent._cast(_461.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_469.CylindricalMeshDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _469

            return self._parent._cast(_469.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_542.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_547.ConicalMeshDutyCycleRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_552.ConceptGearMeshDutyCycleRating":
            from mastapy.gears.rating.concept import _552

            return self._parent._cast(_552.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_553.ConceptGearMeshRating":
            from mastapy.gears.rating.concept import _553

            return self._parent._cast(_553.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_557.BevelGearMeshRating":
            from mastapy.gears.rating.bevel import _557

            return self._parent._cast(_557.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_568.AGMAGleasonConicalGearMeshRating":
            from mastapy.gears.rating.agma_gleason_conical import _568

            return self._parent._cast(_568.AGMAGleasonConicalGearMeshRating)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_621.CylindricalManufacturedGearMeshDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _621

            return self._parent._cast(_621.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_622.CylindricalManufacturedGearMeshLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_625.CylindricalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _625

            return self._parent._cast(_625.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_787.ConicalMeshManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_788.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_789.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_790.ConicalMeshMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_844.GearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca import _844

            return self._parent._cast(_844.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_860.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_873.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _873

            return self._parent._cast(_873.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_878.MeshLoadCase":
            from mastapy.gears.load_case import _878

            return self._parent._cast(_878.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_881.WormMeshLoadCase":
            from mastapy.gears.load_case.worm import _881

            return self._parent._cast(_881.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_884.FaceMeshLoadCase":
            from mastapy.gears.load_case.face import _884

            return self._parent._cast(_884.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_887.CylindricalMeshLoadCase":
            from mastapy.gears.load_case.cylindrical import _887

            return self._parent._cast(_887.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_890.ConicalMeshLoadCase":
            from mastapy.gears.load_case.conical import _890

            return self._parent._cast(_890.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_893.ConceptMeshLoadCase":
            from mastapy.gears.load_case.concept import _893

            return self._parent._cast(_893.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_895.BevelMeshLoadCase":
            from mastapy.gears.load_case.bevel import _895

            return self._parent._cast(_895.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_897.CylindricalGearMeshTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _897

            return self._parent._cast(_897.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_898.CylindricalGearMeshTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _898

            return self._parent._cast(_898.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_996.FaceGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.face import _996

            return self._parent._cast(_996.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1104.CylindricalGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104

            return self._parent._cast(_1104.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1105.CylindricalGearMeshMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1105

            return self._parent._cast(_1105.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1204.GearMeshFEModel":
            from mastapy.gears.fe_model import _1204

            return self._parent._cast(_1204.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1208.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1208

            return self._parent._cast(_1208.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1211.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1211

            return self._parent._cast(_1211.ConicalMeshFEModel)

        @property
        def gear_mesh_design_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1229.GearMeshImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1230.GearMeshImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1231.GearMeshImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearMeshImplementationDetail)

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "AbstractGearMeshAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshName

        if temp is None:
            return ""

        return temp

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
    def gear_a(self: Self) -> "_1221.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1221.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

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
    def cast_to(
        self: Self,
    ) -> "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis":
        return self._Cast_AbstractGearMeshAnalysis(self)
