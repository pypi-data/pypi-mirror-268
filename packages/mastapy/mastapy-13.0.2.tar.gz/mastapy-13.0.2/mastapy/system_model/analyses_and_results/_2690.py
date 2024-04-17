"""CompoundTorsionalSystemDeflectionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundTorsionalSystemDeflectionAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundTorsionalSystemDeflectionAnalysis",)


Self = TypeVar("Self", bound="CompoundTorsionalSystemDeflectionAnalysis")


class CompoundTorsionalSystemDeflectionAnalysis(_2627.CompoundAnalysis):
    """CompoundTorsionalSystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundTorsionalSystemDeflectionAnalysis"
    )

    class _Cast_CompoundTorsionalSystemDeflectionAnalysis:
        """Special nested class for casting CompoundTorsionalSystemDeflectionAnalysis to subclasses."""

        def __init__(
            self: "CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis",
            parent: "CompoundTorsionalSystemDeflectionAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_torsional_system_deflection_analysis(
            self: "CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis",
        ) -> "CompoundTorsionalSystemDeflectionAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis",
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
        self: Self, instance_to_wrap: "CompoundTorsionalSystemDeflectionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis":
        return self._Cast_CompoundTorsionalSystemDeflectionAnalysis(self)
