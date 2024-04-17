"""DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_POINT_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_AT_A_FREQUENCY_TO_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
)


__docformat__ = "restructuredtext en"
__all__ = ("DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",)


Self = TypeVar(
    "Self", bound="DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"
)


class DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic(_0.APIBase):
    """DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic

    This is a mastapy class.
    """

    TYPE = (
        _DATA_POINT_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_AT_A_FREQUENCY_TO_A_HARMONIC
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    )

    class _Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic:
        """Special nested class for casting DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic to subclasses."""

        def __init__(
            self: "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
            parent: "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
        ):
            self._parent = parent

        @property
        def data_point_for_response_of_a_component_or_surface_at_a_frequency_to_a_harmonic(
            self: "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
        ) -> "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic":
            return self._parent

        def __getattr__(
            self: "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
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
        instance_to_wrap: "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def response(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Response

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic":
        return (
            self._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic(
                self
            )
        )
