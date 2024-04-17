"""TwoDimensionalFEModelForAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_DIMENSIONAL_FE_MODEL_FOR_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "TwoDimensionalFEModelForAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1272


__docformat__ = "restructuredtext en"
__all__ = ("TwoDimensionalFEModelForAnalysis",)


Self = TypeVar("Self", bound="TwoDimensionalFEModelForAnalysis")
T = TypeVar("T", bound="_1272.ElectricMachineMeshingOptionsBase")


class TwoDimensionalFEModelForAnalysis(_0.APIBase, Generic[T]):
    """TwoDimensionalFEModelForAnalysis

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _TWO_DIMENSIONAL_FE_MODEL_FOR_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TwoDimensionalFEModelForAnalysis")

    class _Cast_TwoDimensionalFEModelForAnalysis:
        """Special nested class for casting TwoDimensionalFEModelForAnalysis to subclasses."""

        def __init__(
            self: "TwoDimensionalFEModelForAnalysis._Cast_TwoDimensionalFEModelForAnalysis",
            parent: "TwoDimensionalFEModelForAnalysis",
        ):
            self._parent = parent

        @property
        def two_dimensional_fe_model_for_analysis(
            self: "TwoDimensionalFEModelForAnalysis._Cast_TwoDimensionalFEModelForAnalysis",
        ) -> "TwoDimensionalFEModelForAnalysis":
            return self._parent

        def __getattr__(
            self: "TwoDimensionalFEModelForAnalysis._Cast_TwoDimensionalFEModelForAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TwoDimensionalFEModelForAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_elements(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfElements

        if temp is None:
            return 0

        return temp

    @property
    def number_of_nodes(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @property
    def meshing_options(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshingOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TwoDimensionalFEModelForAnalysis._Cast_TwoDimensionalFEModelForAnalysis":
        return self._Cast_TwoDimensionalFEModelForAnalysis(self)
