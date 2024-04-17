"""ExternalCADModelLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ExternalCADModelLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.static_loads import _6937
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelLoadCase",)


Self = TypeVar("Self", bound="ExternalCADModelLoadCase")


class ExternalCADModelLoadCase(_6846.ComponentLoadCase):
    """ExternalCADModelLoadCase

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelLoadCase")

    class _Cast_ExternalCADModelLoadCase:
        """Special nested class for casting ExternalCADModelLoadCase to subclasses."""

        def __init__(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
            parent: "ExternalCADModelLoadCase",
        ):
            self._parent = parent

        @property
        def component_load_case(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
        ) -> "_6846.ComponentLoadCase":
            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_load_case(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase",
        ) -> "ExternalCADModelLoadCase":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModelLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "ExternalCADModelLoadCase._Cast_ExternalCADModelLoadCase":
        return self._Cast_ExternalCADModelLoadCase(self)
