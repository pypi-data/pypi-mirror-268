"""GeneralPeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERAL_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GeneralPeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800, _5687


__docformat__ = "restructuredtext en"
__all__ = ("GeneralPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="GeneralPeriodicExcitationDetail")


class GeneralPeriodicExcitationDetail(
    _5817.SingleNodePeriodicExcitationWithReferenceShaft
):
    """GeneralPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GENERAL_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeneralPeriodicExcitationDetail")

    class _Cast_GeneralPeriodicExcitationDetail:
        """Special nested class for casting GeneralPeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail",
            parent: "GeneralPeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail",
        ) -> "_5817.SingleNodePeriodicExcitationWithReferenceShaft":
            return self._parent._cast(
                _5817.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def periodic_excitation_with_reference_shaft(
            self: "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail",
        ) -> "GeneralPeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeneralPeriodicExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail":
        return self._Cast_GeneralPeriodicExcitationDetail(self)
