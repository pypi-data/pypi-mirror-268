"""LoadedConceptAxialClearanceBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1959
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CONCEPT_AXIAL_CLEARANCE_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedConceptAxialClearanceBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedConceptAxialClearanceBearingResults",)


Self = TypeVar("Self", bound="LoadedConceptAxialClearanceBearingResults")


class LoadedConceptAxialClearanceBearingResults(
    _1959.LoadedConceptClearanceBearingResults
):
    """LoadedConceptAxialClearanceBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CONCEPT_AXIAL_CLEARANCE_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedConceptAxialClearanceBearingResults"
    )

    class _Cast_LoadedConceptAxialClearanceBearingResults:
        """Special nested class for casting LoadedConceptAxialClearanceBearingResults to subclasses."""

        def __init__(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
            parent: "LoadedConceptAxialClearanceBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
        ) -> "_1959.LoadedConceptClearanceBearingResults":
            return self._parent._cast(_1959.LoadedConceptClearanceBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
        ) -> "LoadedConceptAxialClearanceBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults",
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
        self: Self, instance_to_wrap: "LoadedConceptAxialClearanceBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lower_angle_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowerAngleOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def upper_angle_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpperAngleOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults":
        return self._Cast_LoadedConceptAxialClearanceBearingResults(self)
