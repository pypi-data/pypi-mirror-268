"""FlexiblePinAnalysisManufactureLevel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_MANUFACTURE_LEVEL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysisManufactureLevel",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6276


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysisManufactureLevel",)


Self = TypeVar("Self", bound="FlexiblePinAnalysisManufactureLevel")


class FlexiblePinAnalysisManufactureLevel(_6277.FlexiblePinAnalysis):
    """FlexiblePinAnalysisManufactureLevel

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_MANUFACTURE_LEVEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAnalysisManufactureLevel")

    class _Cast_FlexiblePinAnalysisManufactureLevel:
        """Special nested class for casting FlexiblePinAnalysisManufactureLevel to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel",
            parent: "FlexiblePinAnalysisManufactureLevel",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel",
        ) -> "_6277.FlexiblePinAnalysis":
            return self._parent._cast(_6277.FlexiblePinAnalysis)

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel",
        ) -> "_6276.CombinationAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6276,
            )

            return self._parent._cast(_6276.CombinationAnalysis)

        @property
        def flexible_pin_analysis_manufacture_level(
            self: "FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel",
        ) -> "FlexiblePinAnalysisManufactureLevel":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel",
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
        self: Self, instance_to_wrap: "FlexiblePinAnalysisManufactureLevel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_sharing_factors(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactors

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def planetary_mesh_analysis(
        self: Self,
    ) -> "_4351.CylindricalGearMeshParametricStudyTool":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearMeshParametricStudyTool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryMeshAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel"
    ):
        return self._Cast_FlexiblePinAnalysisManufactureLevel(self)
