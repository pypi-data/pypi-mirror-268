"""CylindricalPlanetGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4913,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CylindricalPlanetGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4925,
        _4944,
        _4890,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalPlanetGearModalAnalysisAtAStiffness")


class CylindricalPlanetGearModalAnalysisAtAStiffness(
    _4913.CylindricalGearModalAnalysisAtAStiffness
):
    """CylindricalPlanetGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearModalAnalysisAtAStiffness"
    )

    class _Cast_CylindricalPlanetGearModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalPlanetGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
            parent: "CylindricalPlanetGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4913.CylindricalGearModalAnalysisAtAStiffness":
            return self._parent._cast(_4913.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4925.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(_4925.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4944.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4890.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "CylindricalPlanetGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CylindricalPlanetGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness":
        return self._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness(self)
