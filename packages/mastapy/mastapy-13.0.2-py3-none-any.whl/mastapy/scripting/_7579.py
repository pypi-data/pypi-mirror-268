"""ApiVersioning"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_API_VERSIONING = python_net_import("SMT.MastaAPIUtility.Scripting", "ApiVersioning")

if TYPE_CHECKING:
    from mastapy.scripting import _7571


__docformat__ = "restructuredtext en"
__all__ = ("ApiVersioning",)


Self = TypeVar("Self", bound="ApiVersioning")


class ApiVersioning:
    """ApiVersioning

    This is a mastapy class.
    """

    TYPE = _API_VERSIONING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ApiVersioning")

    class _Cast_ApiVersioning:
        """Special nested class for casting ApiVersioning to subclasses."""

        def __init__(
            self: "ApiVersioning._Cast_ApiVersioning", parent: "ApiVersioning"
        ):
            self._parent = parent

        @property
        def api_versioning(
            self: "ApiVersioning._Cast_ApiVersioning",
        ) -> "ApiVersioning":
            return self._parent

        def __getattr__(self: "ApiVersioning._Cast_ApiVersioning", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ApiVersioning.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    @enforce_parameter_types
    def get_available_api_versions(folder: "str") -> "Iterable[_7571.ApiVersion]":
        """Iterable[mastapy.scripting.ApiVersion]

        Args:
            folder (str)
        """
        folder = str(folder)
        return conversion.pn_to_mp_objects_in_iterable(
            ApiVersioning.TYPE.GetAvailableApiVersions(folder if folder else "")
        )

    @staticmethod
    @enforce_parameter_types
    def get_available_api_utility_versions(
        folder: "str",
    ) -> "Iterable[_7571.ApiVersion]":
        """Iterable[mastapy.scripting.ApiVersion]

        Args:
            folder (str)
        """
        folder = str(folder)
        return conversion.pn_to_mp_objects_in_iterable(
            ApiVersioning.TYPE.GetAvailableApiUtilityVersions(folder if folder else "")
        )

    @staticmethod
    @enforce_parameter_types
    def get_api_version_for_assembly(
        api_library_search_folder: "str", assembly_path: "str"
    ) -> "_7571.ApiVersion":
        """mastapy.scripting.ApiVersion

        Args:
            api_library_search_folder (str)
            assembly_path (str)
        """
        api_library_search_folder = str(api_library_search_folder)
        assembly_path = str(assembly_path)
        method_result = ApiVersioning.TYPE.GetApiVersionForAssembly(
            api_library_search_folder if api_library_search_folder else "",
            assembly_path if assembly_path else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ApiVersioning._Cast_ApiVersioning":
        return self._Cast_ApiVersioning(self)
