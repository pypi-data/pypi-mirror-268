"""ModalCMSResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.component_mode_synthesis import _235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_CMS_RESULTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "ModalCMSResults"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _232


__docformat__ = "restructuredtext en"
__all__ = ("ModalCMSResults",)


Self = TypeVar("Self", bound="ModalCMSResults")


class ModalCMSResults(_235.RealCMSResults):
    """ModalCMSResults

    This is a mastapy class.
    """

    TYPE = _MODAL_CMS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalCMSResults")

    class _Cast_ModalCMSResults:
        """Special nested class for casting ModalCMSResults to subclasses."""

        def __init__(
            self: "ModalCMSResults._Cast_ModalCMSResults", parent: "ModalCMSResults"
        ):
            self._parent = parent

        @property
        def real_cms_results(
            self: "ModalCMSResults._Cast_ModalCMSResults",
        ) -> "_235.RealCMSResults":
            return self._parent._cast(_235.RealCMSResults)

        @property
        def cms_results(
            self: "ModalCMSResults._Cast_ModalCMSResults",
        ) -> "_232.CMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _232

            return self._parent._cast(_232.CMSResults)

        @property
        def modal_cms_results(
            self: "ModalCMSResults._Cast_ModalCMSResults",
        ) -> "ModalCMSResults":
            return self._parent

        def __getattr__(self: "ModalCMSResults._Cast_ModalCMSResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalCMSResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculate_results(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CalculateResults

        if temp is None:
            return False

        return temp

    @calculate_results.setter
    @enforce_parameter_types
    def calculate_results(self: Self, value: "bool"):
        self.wrapped.CalculateResults = bool(value) if value is not None else False

    @property
    def frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeID

        if temp is None:
            return 0

        return temp

    def calculate_strain_and_kinetic_energy(self: Self):
        """Method does not return."""
        self.wrapped.CalculateStrainAndKineticEnergy()

    @property
    def cast_to(self: Self) -> "ModalCMSResults._Cast_ModalCMSResults":
        return self._Cast_ModalCMSResults(self)
