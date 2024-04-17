"""LoadedConceptClearanceBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1964
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CONCEPT_CLEARANCE_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedConceptClearanceBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1958, _1960, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedConceptClearanceBearingResults",)


Self = TypeVar("Self", bound="LoadedConceptClearanceBearingResults")


class LoadedConceptClearanceBearingResults(_1964.LoadedNonLinearBearingResults):
    """LoadedConceptClearanceBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CONCEPT_CLEARANCE_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedConceptClearanceBearingResults")

    class _Cast_LoadedConceptClearanceBearingResults:
        """Special nested class for casting LoadedConceptClearanceBearingResults to subclasses."""

        def __init__(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
            parent: "LoadedConceptClearanceBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
        ) -> "_1958.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1958

            return self._parent._cast(_1958.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
        ) -> "_1960.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1960

            return self._parent._cast(_1960.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
        ) -> "LoadedConceptClearanceBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults",
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
        self: Self, instance_to_wrap: "LoadedConceptClearanceBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_in_contact(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsInContact

        if temp is None:
            return False

        return temp

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedConceptClearanceBearingResults._Cast_LoadedConceptClearanceBearingResults":
        return self._Cast_LoadedConceptClearanceBearingResults(self)
