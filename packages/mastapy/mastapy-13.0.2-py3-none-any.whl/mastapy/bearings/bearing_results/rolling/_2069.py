"""MaximumStaticContactStressResultsAbstract"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAXIMUM_STATIC_CONTACT_STRESS_RESULTS_ABSTRACT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "MaximumStaticContactStressResultsAbstract",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2067, _2068


__docformat__ = "restructuredtext en"
__all__ = ("MaximumStaticContactStressResultsAbstract",)


Self = TypeVar("Self", bound="MaximumStaticContactStressResultsAbstract")


class MaximumStaticContactStressResultsAbstract(_0.APIBase):
    """MaximumStaticContactStressResultsAbstract

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_STATIC_CONTACT_STRESS_RESULTS_ABSTRACT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MaximumStaticContactStressResultsAbstract"
    )

    class _Cast_MaximumStaticContactStressResultsAbstract:
        """Special nested class for casting MaximumStaticContactStressResultsAbstract to subclasses."""

        def __init__(
            self: "MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract",
            parent: "MaximumStaticContactStressResultsAbstract",
        ):
            self._parent = parent

        @property
        def maximum_static_contact_stress(
            self: "MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract",
        ) -> "_2067.MaximumStaticContactStress":
            from mastapy.bearings.bearing_results.rolling import _2067

            return self._parent._cast(_2067.MaximumStaticContactStress)

        @property
        def maximum_static_contact_stress_duty_cycle(
            self: "MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract",
        ) -> "_2068.MaximumStaticContactStressDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2068

            return self._parent._cast(_2068.MaximumStaticContactStressDutyCycle)

        @property
        def maximum_static_contact_stress_results_abstract(
            self: "MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract",
        ) -> "MaximumStaticContactStressResultsAbstract":
            return self._parent

        def __getattr__(
            self: "MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract",
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
        self: Self, instance_to_wrap: "MaximumStaticContactStressResultsAbstract.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def safety_factor_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorInner

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_ratio_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressRatioInner

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_ratio_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressRatioOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract":
        return self._Cast_MaximumStaticContactStressResultsAbstract(self)
