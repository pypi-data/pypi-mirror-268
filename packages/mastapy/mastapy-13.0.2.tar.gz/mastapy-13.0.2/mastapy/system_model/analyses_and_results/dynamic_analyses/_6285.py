"""AbstractAssemblyDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6291,
        _6292,
        _6295,
        _6298,
        _6303,
        _6305,
        _6307,
        _6312,
        _6316,
        _6319,
        _6323,
        _6326,
        _6328,
        _6334,
        _6342,
        _6344,
        _6347,
        _6351,
        _6355,
        _6358,
        _6361,
        _6368,
        _6371,
        _6378,
        _6381,
        _6385,
        _6388,
        _6390,
        _6394,
        _6397,
        _6400,
        _6405,
        _6412,
        _6415,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyDynamicAnalysis")


class AbstractAssemblyDynamicAnalysis(_6366.PartDynamicAnalysis):
    """AbstractAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyDynamicAnalysis")

    class _Cast_AbstractAssemblyDynamicAnalysis:
        """Special nested class for casting AbstractAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            parent: "AbstractAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6291.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6292.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.AssemblyDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6295.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6298.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6303.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.BevelGearSetDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6305.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6307.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6312.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConceptCouplingDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6316.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6319.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.ConicalGearSetDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6323.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CouplingDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6326.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CVTDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6328.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.CycloidalAssemblyDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6334.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6342.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.FaceGearSetDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6344.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6347.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(_6347.GearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6351.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(
                _6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6358.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(
                _6358.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6361.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(
                _6361.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6368.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.PartToPartShearCouplingDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6371.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.PlanetaryGearSetDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6378.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.RollingRingAssemblyDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6381.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.RootAssemblyDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6388.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6390.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SpringDamperDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6394.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6397.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.StraightBevelGearSetDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6400.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.SynchroniserDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6405.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.TorqueConverterDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6412.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "_6415.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "AbstractAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis":
        return self._Cast_AbstractAssemblyDynamicAnalysis(self)
