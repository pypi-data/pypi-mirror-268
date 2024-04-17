"""FourierSeries"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FOURIER_SERIES = python_net_import("SMT.MastaAPI.MathUtility", "FourierSeries")

if TYPE_CHECKING:
    from mastapy.math_utility import _1523


__docformat__ = "restructuredtext en"
__all__ = ("FourierSeries",)


Self = TypeVar("Self", bound="FourierSeries")


class FourierSeries(_0.APIBase):
    """FourierSeries

    This is a mastapy class.
    """

    TYPE = _FOURIER_SERIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FourierSeries")

    class _Cast_FourierSeries:
        """Special nested class for casting FourierSeries to subclasses."""

        def __init__(
            self: "FourierSeries._Cast_FourierSeries", parent: "FourierSeries"
        ):
            self._parent = parent

        @property
        def fourier_series(
            self: "FourierSeries._Cast_FourierSeries",
        ) -> "FourierSeries":
            return self._parent

        def __getattr__(self: "FourierSeries._Cast_FourierSeries", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FourierSeries.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def unit(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unit

        if temp is None:
            return ""

        return temp

    @property
    def mean_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanValue

        if temp is None:
            return 0.0

        return temp

    @mean_value.setter
    @enforce_parameter_types
    def mean_value(self: Self, value: "float"):
        self.wrapped.MeanValue = float(value) if value is not None else 0.0

    @property
    def values(self: Self) -> "List[float]":
        """List[float]"""
        temp = self.wrapped.Values

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @values.setter
    @enforce_parameter_types
    def values(self: Self, value: "List[float]"):
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.Values = value

    @enforce_parameter_types
    def harmonic(self: Self, index: "int") -> "_1523.HarmonicValue":
        """mastapy.math_utility.HarmonicValue

        Args:
            index (int)
        """
        index = int(index)
        method_result = self.wrapped.Harmonic(index if index else 0)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def harmonics_above_cut_off(self: Self) -> "List[_1523.HarmonicValue]":
        """List[mastapy.math_utility.HarmonicValue]"""
        return conversion.pn_to_mp_objects_in_list(self.wrapped.HarmonicsAboveCutOff())

    def harmonics_with_zeros_truncated(self: Self) -> "List[_1523.HarmonicValue]":
        """List[mastapy.math_utility.HarmonicValue]"""
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.HarmonicsWithZerosTruncated()
        )

    def peak_to_peak(self: Self) -> "float":
        """float"""
        method_result = self.wrapped.PeakToPeak()
        return method_result

    @enforce_parameter_types
    def set_amplitude(self: Self, harmonic: "int", amplitude: "float"):
        """Method does not return.

        Args:
            harmonic (int)
            amplitude (float)
        """
        harmonic = int(harmonic)
        amplitude = float(amplitude)
        self.wrapped.SetAmplitude(
            harmonic if harmonic else 0, amplitude if amplitude else 0.0
        )

    @enforce_parameter_types
    def set_amplitude_and_phase(self: Self, harmonic: "int", complex_: "complex"):
        """Method does not return.

        Args:
            harmonic (int)
            complex_ (complex)
        """
        harmonic = int(harmonic)
        complex_ = conversion.mp_to_pn_complex(complex_)
        self.wrapped.SetAmplitudeAndPhase(harmonic if harmonic else 0, complex_)

    @enforce_parameter_types
    def set_phase(self: Self, harmonic: "int", phase: "float"):
        """Method does not return.

        Args:
            harmonic (int)
            phase (float)
        """
        harmonic = int(harmonic)
        phase = float(phase)
        self.wrapped.SetPhase(harmonic if harmonic else 0, phase if phase else 0.0)

    @property
    def cast_to(self: Self) -> "FourierSeries._Cast_FourierSeries":
        return self._Cast_FourierSeries(self)
