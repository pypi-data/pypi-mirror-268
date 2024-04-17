"""BevelDifferentialPlanetGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelDifferentialPlanetGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4321,
        _4309,
        _4337,
        _4370,
        _4389,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearParametricStudyTool")


class BevelDifferentialPlanetGearParametricStudyTool(
    _4316.BevelDifferentialGearParametricStudyTool
):
    """BevelDifferentialPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearParametricStudyTool"
    )

    class _Cast_BevelDifferentialPlanetGearParametricStudyTool:
        """Special nested class for casting BevelDifferentialPlanetGearParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
            parent: "BevelDifferentialPlanetGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4316.BevelDifferentialGearParametricStudyTool":
            return self._parent._cast(_4316.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4321.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4309.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4337.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4370.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(_4370.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
        ) -> "BevelDifferentialPlanetGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialPlanetGearParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2524.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool":
        return self._Cast_BevelDifferentialPlanetGearParametricStudyTool(self)
