"""AbstractAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4310,
        _4311,
        _4314,
        _4317,
        _4322,
        _4323,
        _4327,
        _4332,
        _4335,
        _4338,
        _4343,
        _4345,
        _4347,
        _4353,
        _4366,
        _4368,
        _4371,
        _4375,
        _4379,
        _4382,
        _4385,
        _4404,
        _4406,
        _4413,
        _4416,
        _4420,
        _4423,
        _4426,
        _4429,
        _4432,
        _4436,
        _4440,
        _4447,
        _4450,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractAssemblyParametricStudyTool")


class AbstractAssemblyParametricStudyTool(_4401.PartParametricStudyTool):
    """AbstractAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyParametricStudyTool")

    class _Cast_AbstractAssemblyParametricStudyTool:
        """Special nested class for casting AbstractAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
            parent: "AbstractAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4310.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(
                _4310.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4311.AssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.AssemblyParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4314.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4317.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4322.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4323.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4327.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4332.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4335.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4338.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4343.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4345.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4347.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4347,
            )

            return self._parent._cast(_4347.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4353.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4366.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4368.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(_4368.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4371.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(_4371.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4375.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4379.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(
                _4379.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4382.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4382,
            )

            return self._parent._cast(
                _4382.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4385.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(
                _4385.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4404.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4406.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4413.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.RollingRingAssemblyParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4416.RootAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.RootAssemblyParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4420.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4423.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4426.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4429.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4432.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4436.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4440.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4447.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4450.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4450,
            )

            return self._parent._cast(_4450.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "AbstractAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractAssemblyParametricStudyTool.TYPE"
    ):
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
    ) -> (
        "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool"
    ):
        return self._Cast_AbstractAssemblyParametricStudyTool(self)
