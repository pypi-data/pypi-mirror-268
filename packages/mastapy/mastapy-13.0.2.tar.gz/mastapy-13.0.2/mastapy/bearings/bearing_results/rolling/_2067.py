"""MaximumStaticContactStress"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2069
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAXIMUM_STATIC_CONTACT_STRESS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "MaximumStaticContactStress"
)


__docformat__ = "restructuredtext en"
__all__ = ("MaximumStaticContactStress",)


Self = TypeVar("Self", bound="MaximumStaticContactStress")


class MaximumStaticContactStress(_2069.MaximumStaticContactStressResultsAbstract):
    """MaximumStaticContactStress

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_STATIC_CONTACT_STRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaximumStaticContactStress")

    class _Cast_MaximumStaticContactStress:
        """Special nested class for casting MaximumStaticContactStress to subclasses."""

        def __init__(
            self: "MaximumStaticContactStress._Cast_MaximumStaticContactStress",
            parent: "MaximumStaticContactStress",
        ):
            self._parent = parent

        @property
        def maximum_static_contact_stress_results_abstract(
            self: "MaximumStaticContactStress._Cast_MaximumStaticContactStress",
        ) -> "_2069.MaximumStaticContactStressResultsAbstract":
            return self._parent._cast(_2069.MaximumStaticContactStressResultsAbstract)

        @property
        def maximum_static_contact_stress(
            self: "MaximumStaticContactStress._Cast_MaximumStaticContactStress",
        ) -> "MaximumStaticContactStress":
            return self._parent

        def __getattr__(
            self: "MaximumStaticContactStress._Cast_MaximumStaticContactStress",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaximumStaticContactStress.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MaximumStaticContactStress._Cast_MaximumStaticContactStress":
        return self._Cast_MaximumStaticContactStress(self)
