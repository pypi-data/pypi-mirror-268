"""UnbalancedMassExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "UnbalancedMassExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800, _5687


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassExcitationDetail",)


Self = TypeVar("Self", bound="UnbalancedMassExcitationDetail")


class UnbalancedMassExcitationDetail(
    _5817.SingleNodePeriodicExcitationWithReferenceShaft
):
    """UnbalancedMassExcitationDetail

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassExcitationDetail")

    class _Cast_UnbalancedMassExcitationDetail:
        """Special nested class for casting UnbalancedMassExcitationDetail to subclasses."""

        def __init__(
            self: "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail",
            parent: "UnbalancedMassExcitationDetail",
        ):
            self._parent = parent

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail",
        ) -> "_5817.SingleNodePeriodicExcitationWithReferenceShaft":
            return self._parent._cast(
                _5817.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def periodic_excitation_with_reference_shaft(
            self: "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def unbalanced_mass_excitation_detail(
            self: "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail",
        ) -> "UnbalancedMassExcitationDetail":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail":
        return self._Cast_UnbalancedMassExcitationDetail(self)
