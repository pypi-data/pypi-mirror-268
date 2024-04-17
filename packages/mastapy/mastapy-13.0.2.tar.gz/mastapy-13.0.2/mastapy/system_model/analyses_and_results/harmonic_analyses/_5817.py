"""SingleNodePeriodicExcitationWithReferenceShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_NODE_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SingleNodePeriodicExcitationWithReferenceShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5767,
        _5843,
        _5687,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SingleNodePeriodicExcitationWithReferenceShaft",)


Self = TypeVar("Self", bound="SingleNodePeriodicExcitationWithReferenceShaft")


class SingleNodePeriodicExcitationWithReferenceShaft(
    _5800.PeriodicExcitationWithReferenceShaft
):
    """SingleNodePeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE = _SINGLE_NODE_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SingleNodePeriodicExcitationWithReferenceShaft"
    )

    class _Cast_SingleNodePeriodicExcitationWithReferenceShaft:
        """Special nested class for casting SingleNodePeriodicExcitationWithReferenceShaft to subclasses."""

        def __init__(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
            parent: "SingleNodePeriodicExcitationWithReferenceShaft",
        ):
            self._parent = parent

        @property
        def periodic_excitation_with_reference_shaft(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5767.GeneralPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(_5767.GeneralPeriodicExcitationDetail)

        @property
        def unbalanced_mass_excitation_detail(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5843.UnbalancedMassExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.UnbalancedMassExcitationDetail)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "SingleNodePeriodicExcitationWithReferenceShaft":
            return self._parent

        def __getattr__(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
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
        instance_to_wrap: "SingleNodePeriodicExcitationWithReferenceShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft":
        return self._Cast_SingleNodePeriodicExcitationWithReferenceShaft(self)
