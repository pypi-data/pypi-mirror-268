"""MaximumStaticContactStressDutyCycle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2069
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAXIMUM_STATIC_CONTACT_STRESS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "MaximumStaticContactStressDutyCycle",
)


__docformat__ = "restructuredtext en"
__all__ = ("MaximumStaticContactStressDutyCycle",)


Self = TypeVar("Self", bound="MaximumStaticContactStressDutyCycle")


class MaximumStaticContactStressDutyCycle(
    _2069.MaximumStaticContactStressResultsAbstract
):
    """MaximumStaticContactStressDutyCycle

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_STATIC_CONTACT_STRESS_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaximumStaticContactStressDutyCycle")

    class _Cast_MaximumStaticContactStressDutyCycle:
        """Special nested class for casting MaximumStaticContactStressDutyCycle to subclasses."""

        def __init__(
            self: "MaximumStaticContactStressDutyCycle._Cast_MaximumStaticContactStressDutyCycle",
            parent: "MaximumStaticContactStressDutyCycle",
        ):
            self._parent = parent

        @property
        def maximum_static_contact_stress_results_abstract(
            self: "MaximumStaticContactStressDutyCycle._Cast_MaximumStaticContactStressDutyCycle",
        ) -> "_2069.MaximumStaticContactStressResultsAbstract":
            return self._parent._cast(_2069.MaximumStaticContactStressResultsAbstract)

        @property
        def maximum_static_contact_stress_duty_cycle(
            self: "MaximumStaticContactStressDutyCycle._Cast_MaximumStaticContactStressDutyCycle",
        ) -> "MaximumStaticContactStressDutyCycle":
            return self._parent

        def __getattr__(
            self: "MaximumStaticContactStressDutyCycle._Cast_MaximumStaticContactStressDutyCycle",
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
        self: Self, instance_to_wrap: "MaximumStaticContactStressDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "MaximumStaticContactStressDutyCycle._Cast_MaximumStaticContactStressDutyCycle"
    ):
        return self._Cast_MaximumStaticContactStressDutyCycle(self)
