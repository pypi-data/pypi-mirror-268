"""LoadedConceptRadialClearanceBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1959
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CONCEPT_RADIAL_CLEARANCE_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedConceptRadialClearanceBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedConceptRadialClearanceBearingResults",)


Self = TypeVar("Self", bound="LoadedConceptRadialClearanceBearingResults")


class LoadedConceptRadialClearanceBearingResults(
    _1959.LoadedConceptClearanceBearingResults
):
    """LoadedConceptRadialClearanceBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CONCEPT_RADIAL_CLEARANCE_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedConceptRadialClearanceBearingResults"
    )

    class _Cast_LoadedConceptRadialClearanceBearingResults:
        """Special nested class for casting LoadedConceptRadialClearanceBearingResults to subclasses."""

        def __init__(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
            parent: "LoadedConceptRadialClearanceBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
        ) -> "_1959.LoadedConceptClearanceBearingResults":
            return self._parent._cast(_1959.LoadedConceptClearanceBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
        ) -> "LoadedConceptRadialClearanceBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults",
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
        self: Self, instance_to_wrap: "LoadedConceptRadialClearanceBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_penetration_in_middle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfacePenetrationInMiddle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults":
        return self._Cast_LoadedConceptRadialClearanceBearingResults(self)
