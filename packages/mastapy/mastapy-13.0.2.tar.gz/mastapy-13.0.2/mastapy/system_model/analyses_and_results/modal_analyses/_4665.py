"""ModalAnalysisOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "ModalAnalysisOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4642


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisOptions",)


Self = TypeVar("Self", bound="ModalAnalysisOptions")


class ModalAnalysisOptions(_0.APIBase):
    """ModalAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisOptions")

    class _Cast_ModalAnalysisOptions:
        """Special nested class for casting ModalAnalysisOptions to subclasses."""

        def __init__(
            self: "ModalAnalysisOptions._Cast_ModalAnalysisOptions",
            parent: "ModalAnalysisOptions",
        ):
            self._parent = parent

        @property
        def modal_analysis_options(
            self: "ModalAnalysisOptions._Cast_ModalAnalysisOptions",
        ) -> "ModalAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisOptions._Cast_ModalAnalysisOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_mode_frequency(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumModeFrequency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_mode_frequency.setter
    @enforce_parameter_types
    def maximum_mode_frequency(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumModeFrequency = value

    @property
    def number_of_modes(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfModes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_modes.setter
    @enforce_parameter_types
    def number_of_modes(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfModes = value

    @property
    def use_single_pass_eigensolver(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSinglePassEigensolver

        if temp is None:
            return False

        return temp

    @use_single_pass_eigensolver.setter
    @enforce_parameter_types
    def use_single_pass_eigensolver(self: Self, value: "bool"):
        self.wrapped.UseSinglePassEigensolver = (
            bool(value) if value is not None else False
        )

    @property
    def frequency_response_options_for_reports(
        self: Self,
    ) -> "_4642.FrequencyResponseAnalysisOptions":
        """mastapy.system_model.analyses_and_results.modal_analyses.FrequencyResponseAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyResponseOptionsForReports

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ModalAnalysisOptions._Cast_ModalAnalysisOptions":
        return self._Cast_ModalAnalysisOptions(self)
