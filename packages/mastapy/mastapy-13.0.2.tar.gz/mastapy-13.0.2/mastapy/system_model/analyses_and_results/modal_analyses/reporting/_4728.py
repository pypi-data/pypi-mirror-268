"""ModalCMSResultsForModeAndFE"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_CMS_RESULTS_FOR_MODE_AND_FE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "ModalCMSResultsForModeAndFE",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _234


__docformat__ = "restructuredtext en"
__all__ = ("ModalCMSResultsForModeAndFE",)


Self = TypeVar("Self", bound="ModalCMSResultsForModeAndFE")


class ModalCMSResultsForModeAndFE(_0.APIBase):
    """ModalCMSResultsForModeAndFE

    This is a mastapy class.
    """

    TYPE = _MODAL_CMS_RESULTS_FOR_MODE_AND_FE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalCMSResultsForModeAndFE")

    class _Cast_ModalCMSResultsForModeAndFE:
        """Special nested class for casting ModalCMSResultsForModeAndFE to subclasses."""

        def __init__(
            self: "ModalCMSResultsForModeAndFE._Cast_ModalCMSResultsForModeAndFE",
            parent: "ModalCMSResultsForModeAndFE",
        ):
            self._parent = parent

        @property
        def modal_cms_results_for_mode_and_fe(
            self: "ModalCMSResultsForModeAndFE._Cast_ModalCMSResultsForModeAndFE",
        ) -> "ModalCMSResultsForModeAndFE":
            return self._parent

        def __getattr__(
            self: "ModalCMSResultsForModeAndFE._Cast_ModalCMSResultsForModeAndFE",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalCMSResultsForModeAndFE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEName

        if temp is None:
            return ""

        return temp

    @property
    def modal_full_fe_results(self: Self) -> "_234.ModalCMSResults":
        """mastapy.nodal_analysis.component_mode_synthesis.ModalCMSResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalFullFEResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ModalCMSResultsForModeAndFE._Cast_ModalCMSResultsForModeAndFE":
        return self._Cast_ModalCMSResultsForModeAndFE(self)
