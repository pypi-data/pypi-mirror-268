"""PlanetaryGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PlanetaryGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4371,
        _4420,
        _4304,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetaryGearSetParametricStudyTool")


class PlanetaryGearSetParametricStudyTool(_4353.CylindricalGearSetParametricStudyTool):
    """PlanetaryGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetParametricStudyTool")

    class _Cast_PlanetaryGearSetParametricStudyTool:
        """Special nested class for casting PlanetaryGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
            parent: "PlanetaryGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4353.CylindricalGearSetParametricStudyTool":
            return self._parent._cast(_4353.CylindricalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4371.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(_4371.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4420.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4304.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "PlanetaryGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2549.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
        "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool"
    ):
        return self._Cast_PlanetaryGearSetParametricStudyTool(self)
