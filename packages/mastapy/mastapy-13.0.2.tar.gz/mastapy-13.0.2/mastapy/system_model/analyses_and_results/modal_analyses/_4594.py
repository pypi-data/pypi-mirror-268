"""BevelDifferentialPlanetGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelDifferentialPlanetGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.system_deflections import _2712
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4597,
        _4585,
        _4613,
        _4644,
        _4666,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearModalAnalysis")


class BevelDifferentialPlanetGearModalAnalysis(
    _4592.BevelDifferentialGearModalAnalysis
):
    """BevelDifferentialPlanetGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearModalAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearModalAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
            parent: "BevelDifferentialPlanetGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4592.BevelDifferentialGearModalAnalysis":
            return self._parent._cast(_4592.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4597.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4585.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4613.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4644.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "BevelDifferentialPlanetGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialPlanetGearModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2712.BevelDifferentialPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis":
        return self._Cast_BevelDifferentialPlanetGearModalAnalysis(self)
