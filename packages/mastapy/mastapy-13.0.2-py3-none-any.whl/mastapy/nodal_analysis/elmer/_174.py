"""ElmerResultsFromElectroMagneticAnalysis"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.elmer import _173
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELMER_RESULTS_FROM_ELECTRO_MAGNETIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.Elmer", "ElmerResultsFromElectroMagneticAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElmerResultsFromElectroMagneticAnalysis",)


Self = TypeVar("Self", bound="ElmerResultsFromElectroMagneticAnalysis")


class ElmerResultsFromElectroMagneticAnalysis(_173.ElmerResults):
    """ElmerResultsFromElectroMagneticAnalysis

    This is a mastapy class.
    """

    TYPE = _ELMER_RESULTS_FROM_ELECTRO_MAGNETIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElmerResultsFromElectroMagneticAnalysis"
    )

    class _Cast_ElmerResultsFromElectroMagneticAnalysis:
        """Special nested class for casting ElmerResultsFromElectroMagneticAnalysis to subclasses."""

        def __init__(
            self: "ElmerResultsFromElectroMagneticAnalysis._Cast_ElmerResultsFromElectroMagneticAnalysis",
            parent: "ElmerResultsFromElectroMagneticAnalysis",
        ):
            self._parent = parent

        @property
        def elmer_results(
            self: "ElmerResultsFromElectroMagneticAnalysis._Cast_ElmerResultsFromElectroMagneticAnalysis",
        ) -> "_173.ElmerResults":
            return self._parent._cast(_173.ElmerResults)

        @property
        def elmer_results_from_electro_magnetic_analysis(
            self: "ElmerResultsFromElectroMagneticAnalysis._Cast_ElmerResultsFromElectroMagneticAnalysis",
        ) -> "ElmerResultsFromElectroMagneticAnalysis":
            return self._parent

        def __getattr__(
            self: "ElmerResultsFromElectroMagneticAnalysis._Cast_ElmerResultsFromElectroMagneticAnalysis",
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
        self: Self, instance_to_wrap: "ElmerResultsFromElectroMagneticAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElmerResultsFromElectroMagneticAnalysis._Cast_ElmerResultsFromElectroMagneticAnalysis":
        return self._Cast_ElmerResultsFromElectroMagneticAnalysis(self)
