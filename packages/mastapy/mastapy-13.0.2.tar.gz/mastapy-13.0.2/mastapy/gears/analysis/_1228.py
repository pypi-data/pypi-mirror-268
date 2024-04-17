"""GearMeshDesignAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshDesignAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1224, _1232, _1229, _1230, _1231
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
__all__ = ("GearMeshDesignAnalysis",)


Self = TypeVar("Self", bound="GearMeshDesignAnalysis")


class GearMeshDesignAnalysis(_1222.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDesignAnalysis")

    class _Cast_GearMeshDesignAnalysis:
        """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

        def __init__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
            parent: "GearMeshDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1222.AbstractGearMeshAnalysis":
            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_621.CylindricalManufacturedGearMeshDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _621

            return self._parent._cast(_621.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_622.CylindricalManufacturedGearMeshLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_625.CylindricalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _625

            return self._parent._cast(_625.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_787.ConicalMeshManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_788.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_789.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_790.ConicalMeshMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_844.GearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca import _844

            return self._parent._cast(_844.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_860.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_873.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _873

            return self._parent._cast(_873.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_878.MeshLoadCase":
            from mastapy.gears.load_case import _878

            return self._parent._cast(_878.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_881.WormMeshLoadCase":
            from mastapy.gears.load_case.worm import _881

            return self._parent._cast(_881.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_884.FaceMeshLoadCase":
            from mastapy.gears.load_case.face import _884

            return self._parent._cast(_884.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_887.CylindricalMeshLoadCase":
            from mastapy.gears.load_case.cylindrical import _887

            return self._parent._cast(_887.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_890.ConicalMeshLoadCase":
            from mastapy.gears.load_case.conical import _890

            return self._parent._cast(_890.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_893.ConceptMeshLoadCase":
            from mastapy.gears.load_case.concept import _893

            return self._parent._cast(_893.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_895.BevelMeshLoadCase":
            from mastapy.gears.load_case.bevel import _895

            return self._parent._cast(_895.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_897.CylindricalGearMeshTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _897

            return self._parent._cast(_897.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_898.CylindricalGearMeshTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _898

            return self._parent._cast(_898.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_996.FaceGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.face import _996

            return self._parent._cast(_996.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1104.CylindricalGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104

            return self._parent._cast(_1104.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1105.CylindricalGearMeshMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1105

            return self._parent._cast(_1105.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1204.GearMeshFEModel":
            from mastapy.gears.fe_model import _1204

            return self._parent._cast(_1204.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1208.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1208

            return self._parent._cast(_1208.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1211.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1211

            return self._parent._cast(_1211.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1229.GearMeshImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1230.GearMeshImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1231.GearMeshImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "GearMeshDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self: Self) -> "_1224.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1224.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set(self: Self) -> "_1232.GearSetDesignAnalysis":
        """mastapy.gears.analysis.GearSetDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis":
        return self._Cast_GearMeshDesignAnalysis(self)
