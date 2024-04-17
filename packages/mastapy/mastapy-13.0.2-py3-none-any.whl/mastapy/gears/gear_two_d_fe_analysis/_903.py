"""CylindricalGearTwoDimensionalFEAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TWO_DIMENSIONAL_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "CylindricalGearTwoDimensionalFEAnalysis"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _187
    from mastapy.gears.gear_two_d_fe_analysis import _904
    from mastapy.nodal_analysis.states import _127


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTwoDimensionalFEAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearTwoDimensionalFEAnalysis")


class CylindricalGearTwoDimensionalFEAnalysis(_0.APIBase):
    """CylindricalGearTwoDimensionalFEAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TWO_DIMENSIONAL_FE_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearTwoDimensionalFEAnalysis"
    )

    class _Cast_CylindricalGearTwoDimensionalFEAnalysis:
        """Special nested class for casting CylindricalGearTwoDimensionalFEAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearTwoDimensionalFEAnalysis._Cast_CylindricalGearTwoDimensionalFEAnalysis",
            parent: "CylindricalGearTwoDimensionalFEAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_two_dimensional_fe_analysis(
            self: "CylindricalGearTwoDimensionalFEAnalysis._Cast_CylindricalGearTwoDimensionalFEAnalysis",
        ) -> "CylindricalGearTwoDimensionalFEAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearTwoDimensionalFEAnalysis._Cast_CylindricalGearTwoDimensionalFEAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearTwoDimensionalFEAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_stress_states(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfStressStates

        if temp is None:
            return 0

        return temp

    @property
    def fe_model(self: Self) -> "_187.FEModel":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def findley_critical_plane_analysis(
        self: Self,
    ) -> "_904.FindleyCriticalPlaneAnalysis":
        """mastapy.gears.gear_two_d_fe_analysis.FindleyCriticalPlaneAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FindleyCriticalPlaneAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def get_stress_states(self: Self, index: "int") -> "_127.NodeVectorState":
        """mastapy.nodal_analysis.states.NodeVectorState

        Args:
            index (int)
        """
        index = int(index)
        method_result = self.wrapped.GetStressStates(index if index else 0)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def perform(self: Self):
        """Method does not return."""
        self.wrapped.Perform()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearTwoDimensionalFEAnalysis._Cast_CylindricalGearTwoDimensionalFEAnalysis":
        return self._Cast_CylindricalGearTwoDimensionalFEAnalysis(self)
