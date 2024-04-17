"""helpers.py

This is the main utility module for the Masta Python API. This module is
required to be imported by users to interact with Masta.

Examples:
    The following code demonstrates how to initialise Masta for use with
    external Python scripts:

        >>> import mastapy
        >>> mastapy.init('my_path_to_dll_folder')

    The following code demonstrates how to define a Masta property:

        >>> from mastapy import masta_property
        >>> from mastapy.system_model import Design
        >>> @masta_property(name='my_masta_property')
            def my_function(design: Design) -> int:
                return 0
"""

from __future__ import annotations

import inspect
import itertools
import functools
import sys
import os
import importlib
import warnings
import types
import typing

from typing import Optional, Union, Tuple
from enum import Enum, auto
from contextlib import suppress

from packaging import version
from packaging.specifiers import SpecifierSet
from PIL import Image

from mastapy._internal.measurement_type import (
    MeasurementType,
    convert_measurement_to_str,
)
from mastapy._internal.mastapy_version_exception import MastapyVersionException
from mastapy._internal.python_net import (
    python_net_import,
    initialise_python_net_importing,
    python_net_add_reference,
)
from mastapy._internal.deprecation import deprecated
from mastapy._internal.version import __api_version__


__all__ = (
    "masta_property",
    "masta_before",
    "masta_after",
    "init",
    "start_debugging",
    "DebugEnvironment",
)


_MASTA_PROPERTIES = dict()
_MASTA_SETTERS = dict()
_hook_name_to_method_dict = dict()
_has_attempted_mastafile_load = False
_has_initialised_with_environment_variable = False
_warned_about_environment_variable = False

_is_initialised = False
_int32 = None

warnings.formatwarning = lambda m, c, f, n, line=None: "{}:{}:\n{}: {}\n".format(
    f, n, c.__name__, m
)


class DebugEnvironment(Enum):
    """Environment used for debugging."""

    VSCODE = (auto(),)
    PYCHARM = (auto(),)


class MastaInitWarning(Warning):
    """Warning for issues to do with initialisation."""


class MastaInitException(Exception):
    """MastaInitException

    Exception raised when there is an issue with initialising mastapy.
    """


class MastaPropertyException(Exception):
    """MastaPropertyException

    Exception raised when there is an issue with a defined Masta property.
    """


class MastaPropertyTypeException(Exception):
    """MastaPropertyTypeException

    Exception raised when there is an issue with the type of a defined Masta
    property.
    """


class MastaPropertyMultiMethod(dict):
    """MastaPropertyMultiMethod

    Class that enables multiple-dispatch of Masta properties. This allows a
    user to call both the getter and setter methods from within their code.
    """

    def __new__(cls, func, types):
        namespace = inspect.currentframe().f_back.f_locals
        self = functools.update_wrapper(dict.__new__(cls), func)
        return namespace.get(func.__name__, self)

    def __init__(self, func, types):
        self[types] = func

    def __missing__(self, types):
        raise MastaPropertyException(
            "Failed to find method with parameters of type: {}".format(types)
        )

    def __call__(self, *args, **kwargs):
        subs = map(lambda x: x.__class__.__mro__, args)
        arg_combos = itertools.product(*subs)

        for combo in arg_combos:
            try:
                func = self[tuple(map(type, args))]
                value = func(*args, **kwargs)

                expected_return = typing.get_type_hints()["return"]
                if not isinstance(value, expected_return):
                    raise MastaPropertyTypeException(
                        (
                            "Return value is of an unexpected type. Make sure the"
                            " type matches the property's annotated return type."
                            "\n\nExpected: {}\nGot: {}"
                        ).format(expected_return, value)
                    )

                return value
            except MastaPropertyException:
                pass

        self.__missing__(args)

    def setter(self, func):
        """Setter for the MASTA property.

        Args:
            func: Wrapped function.
        """
        func_spec = inspect.getfullargspec(func)
        annotations = func_spec.annotations
        arg_names = func_spec.args
        num_arguments = len(arg_names)
        num_typed_parameters = len(list(filter(lambda x: x != "return", annotations)))

        if func.__name__ not in _MASTA_PROPERTIES:
            raise MastaPropertyException(
                (
                    "MASTA property setters must share the same name as their "
                    "accompanying getter. No getter found called '{}'."
                ).format(func.__name__)
            )

        if num_arguments != 2:
            end = "was" if num_arguments == 1 else "were"
            raise MastaPropertyException(
                (
                    "MASTA property setters require 2 " "arguments, but {} {} found."
                ).format(num_arguments, end)
            )

        if num_typed_parameters != 2:
            raise MastaPropertyException(
                "Both MASTA property setter parameters must be typed."
            )

        setter_type = annotations[arg_names[0]]
        getter_type = _MASTA_PROPERTIES[func.__name__][1]
        if setter_type != getter_type:
            raise MastaPropertyException(
                (
                    "MASTA property setters and getters must have their first "
                    "parameters defined with the same type.\n"
                    "Got: {}\nExpected: {}"
                ).format(setter_type.__qualname__, getter_type.__qualname__)
            )

        setter_value_type = annotations[arg_names[1]]
        getter_value_type = _MASTA_PROPERTIES[func.__name__][6]

        if using_pythonnet3 and setter_value_type == int:

            _int32 = python_net_import("System", "Int32")
            setter_value_type = _int32

        if not getter_value_type:
            raise MastaPropertyException(
                (
                    "MASTA property getter does not have a specified "
                    "return type. Setter not expected."
                )
            )

        if setter_value_type != getter_value_type:
            raise MastaPropertyException(
                (
                    "MASTA property setters and getters must match their setting "
                    "and returning types.\nGot: {}\nExpected: {}"
                ).format(setter_value_type.__qualname__, getter_value_type.__qualname__)
            )

        _MASTA_SETTERS[func.__name__] = func

        args = tuple(map(annotations.get, arg_names))
        self.__init__(func, args)

        return self if self.__name__ == func.__name__ else func


def masta_property(
    name: str,
    *,
    description: Optional[str] = "",
    symbol: Optional[str] = "",
    measurement: Optional[Union[str, MeasurementType]] = "",
):
    """Define a MASTA Property. This is a decorator function.

    Args:
        name (str): The name of the property displayed in MASTA.
        description (str, optional): The description of what the property does.
        symbol (str, optional): The symbol for the property displayed in Masta.
        measurement (str|MeasurementType, optional): Unit the property
            displayed in, in Masta.
    """

    def _masta_property_decorator(func):
        global _int32

        func_spec = inspect.getfullargspec(func)
        args = func_spec.args
        annotations = func_spec.annotations
        any_typed_parameters = any(filter(lambda x: x != "return", annotations))

        len_args = len(args)

        if len_args < 1 or not any_typed_parameters:
            raise MastaPropertyException(
                (
                    "MASTA property found without a typed parameter. "
                    "MASTA properties must include one typed parameter."
                )
            )

        if len_args > 1:
            raise MastaPropertyException(
                (
                    "Too many parameters found in MASTA property description. "
                    "Only one is supported."
                )
            )

        parameter = annotations.get(args[0], None)
        returns = annotations.get("return", None)

        if parameter:
            is_old_type = not parameter.__module__.startswith("mastapy")
            m = (
                convert_measurement_to_str(measurement)
                if isinstance(measurement, MeasurementType)
                else measurement
            )

            frame = sys._getframe(1)
            filename = inspect.getsourcefile(frame) or inspect.getfile(frame)

            final_func = func

            if hasattr(returns, "__mro__") and Image.Image in returns.__mro__:
                from mastapy._internal.conversion import mp_to_pn_smt_bitmap

                def _proxy(f):
                    return mp_to_pn_smt_bitmap(func(f))

                final_func = _proxy
            elif using_pythonnet3 and returns == int:

                _int32 = python_net_import("System", "Int32")
                returns = _int32

            _MASTA_PROPERTIES[func.__name__] = (
                final_func,
                parameter,
                name,
                description,
                symbol,
                m,
                returns,
                is_old_type,
                filename,
            )

        return MastaPropertyMultiMethod(func, (parameter,))

    return _masta_property_decorator


def _mastafile_hook():
    """Executes a mastafile.py file from the local directory if found."""
    global _has_attempted_mastafile_load, _hook_name_to_method_dict
    global _has_initialised_with_environment_variable

    if os.environ.get("MASTAFILE_DISABLED", False):
        return

    masta_directory = os.environ.get("MASTA_DIRECTORY", None)

    if masta_directory is not None and _init(masta_directory):
        _has_initialised_with_environment_variable = True

    if "mastafile" not in sys.modules and not _has_attempted_mastafile_load:
        _has_attempted_mastafile_load = True

        with suppress(IOError, OSError, TypeError):
            path_to_mastafile = os.path.realpath("mastafile.py")

            if not os.path.exists(path_to_mastafile):
                sys_paths = map(lambda x: os.path.join(x, "mastafile.py"), sys.path)
                sys_paths = filter(lambda x: os.path.exists(x), sys_paths)
                path_to_mastafile = next(sys_paths, None)

            os.chdir(os.path.dirname(path_to_mastafile))
            mastafile_loader = importlib.machinery.SourceFileLoader(
                "mastafile_module", path_to_mastafile
            )
            mastafile_module = types.ModuleType(mastafile_loader.name)
            mastafile_loader.exec_module(mastafile_module)
            _hook_name_to_method_dict = dict(
                inspect.getmembers(mastafile_module, predicate=inspect.isfunction)
            )


def masta_before(name: str):
    """Decorator method for adding hooks to properties that are called before
    the property is called. Hooking methods must be defined in a mastafile.py
    file.

    Args:
        name (str): The name of the hooking method in mastafile.py
    """

    def _masta_before_decorator(func):

        def _decorator(*args, **kwargs):
            hook = _hook_name_to_method_dict.get(name, None)

            if not hook:
                raise MastaPropertyException(
                    "Failed to find hooking method '{}'.".format(name)
                )

            hook(*args, **kwargs)
            return func(*args, **kwargs)

        return _decorator

    return _masta_before_decorator


def masta_after(name: str):
    """Decorator method for adding hooks to properties that are called after
    the property is called. Hooking methods must be defined in a mastafile.py
    file.

    Args:
        name (str): The name of the hooking method in mastafile.py
    """

    def _masta_after_decorator(func):

        def _decorator(*args, **kwargs):
            hook = _hook_name_to_method_dict.get(name, None)

            if not hook:
                raise MastaPropertyException(
                    "Failed to find hooking  method '{}'.".format(name)
                )

            x = func(*args, **kwargs)
            hook(*args, **kwargs)
            return x

        return _decorator

    return _masta_after_decorator


def _strip_pre_release(value: str) -> str:
    letters = ["a", "b", "rc", "post"]
    letter = next(filter(lambda x: x in value, letters), None)

    if letter:
        i = value.index(letter)
        value = value[:i]
        return value if value else "0"
    else:
        return value


def _convert_version_to_tuple(version: Optional[Union[str, Tuple[int]]]) -> Tuple[int]:
    if isinstance(version, str):
        version = tuple(map(lambda x: int(_strip_pre_release(x)), version.split(".")))

    v_len = len(version)
    if v_len < 3:
        version += (0,) * (3 - v_len)

    return version


def _match_versions():
    versioning = python_net_import("SMT.MastaAPI", "UtilityMethods")

    if hasattr(versioning, "ReleaseVersionString"):
        release_version_str = versioning.ReleaseVersionString
    else:
        versioning = python_net_import("SMT.MastaAPI", "Versioning")
        release_version_str = versioning.APIReleaseVersionString

    api_version = release_version_str.split(" ")[0]

    current_version = _convert_version_to_tuple(api_version)
    backwards_version = (10, 3, 0)
    no_backwards_compatibility = current_version < backwards_version

    if no_backwards_compatibility and api_version != __api_version__:
        message = (
            f"This version of mastapy ({api_version}) is not supported "
            "by the version of MASTA you are trying to initialise it "
            "with.\n\n"
            f"You must use either MASTA {api_version} or newer.\n"
        )
        raise MastapyVersionException(message) from None


def _load_patch(runtime_path: str, runtime=None, **params: str) -> None:
    """Load Python.NET in the specified runtime.

    The same parameters as for `set_runtime` can be used. By default,
    `set_default_runtime` is called if no environment has been set yet and no
    parameters are passed.
    """
    import pythonnet

    if pythonnet._LOADED:
        return

    if pythonnet._RUNTIME is None:
        if runtime is None:
            pythonnet.set_runtime_from_env()
        else:
            pythonnet.set_runtime(runtime, **params)

    if pythonnet._RUNTIME is None:
        raise RuntimeError("No valid runtime selected")

    pythonnet._LOADER_ASSEMBLY = assembly = pythonnet._RUNTIME.get_assembly(
        runtime_path
    )
    func = assembly.get_function("Python.Runtime.Loader.Initialize")

    if func(b"") != 0:
        raise RuntimeError("Failed to initialize Python.Runtime.dll")

    import atexit

    atexit.register(pythonnet.unload)


@functools.lru_cache(maxsize=None)
def get_python_version() -> version.Version:
    version_tuple = sys.version_info[:2]
    version_str = ".".join(map(str, version_tuple))
    return version.parse(version_str)


@functools.lru_cache(maxsize=None)
def get_pythonnet_version() -> version.Version:
    try:
        from importlib import metadata

        pythonnet_str = metadata.version("pythonnet")
    except ImportError:
        import pkg_resources

        pythonnet_str = pkg_resources.get_distribution("pythonnet").version

    return version.parse(pythonnet_str)


@functools.lru_cache(maxsize=None)
def using_pythonnet3() -> bool:
    return get_pythonnet_version() in SpecifierSet(">=3.0.0")


def _init_runtime_setup(path_to_dll_folder: str) -> str:
    python_version = get_python_version()

    if python_version in SpecifierSet(">=3.9"):
        python_runtime_dll = "Python.Runtime.dll"
    else:
        version_identifier = "".join(map(str, python_version.release))
        python_runtime_dll = "Python.Runtime{}.dll".format(version_identifier)

    python_runtime_path = os.path.join(path_to_dll_folder, python_runtime_dll)

    if not os.path.exists(python_runtime_path):
        raise MastaInitException(
            ("Failed to load Python runtime environment " "at path '{}'.").format(
                python_runtime_path
            )
        )

    return python_runtime_path


def _init_runtime_legacy(python_runtime_path: str):
    assembly = python_net_add_reference(python_runtime_path)

    binding_flags = python_net_import("System.Reflection", "BindingFlags")
    assembly_manager = assembly.GetType("Python.Runtime.AssemblyManager")

    bf = binding_flags.Public | binding_flags.Static | binding_flags.InvokeMethod
    method = assembly_manager.GetMethod("Initialize", bf)

    if method:
        method.Invoke(None, None)


def _init_runtime(path_to_dll_folder: str):
    python_runtime_path = _init_runtime_setup(path_to_dll_folder)

    if using_pythonnet3():
        import pythonnet

        pythonnet.load = functools.partial(_load_patch, python_runtime_path)
    else:
        _init_runtime_legacy(python_runtime_path)


def _init_dotnet_core_if_required(path_to_dll_folder: str):
    path_to_deps = os.path.join(path_to_dll_folder, "SMT.Utility.Tests.deps.json")
    is_dotnet_core = os.path.isfile(path_to_deps)

    if is_dotnet_core:
        try:
            from pythonnet import load

            load("coreclr")
        except ModuleNotFoundError:
            message = (
                "Attempted to initialise mastapy using a .NET Core "
                "environment with an outdated Python.NET installation. "
                "To use .NET Core, install Python>=3.9 and "
                "pythonnet>=3.0.0"
            )
            raise MastaInitException(message)


def _init(path_to_dll_folder: str, initialise_api_access: bool = True) -> bool:
    global _is_initialised, _warned_about_environment_variable

    if _is_initialised:
        if (
            _has_initialised_with_environment_variable
            and not _warned_about_environment_variable
        ):
            warnings.warn(
                "Mastapy has already been automatically initialised "
                "using the MASTA_DIRECTORY environment variable. If "
                "this behaviour was unintended, either remove the "
                "MASTA_DIRECTORY environment variable or override "
                "it using os.environ.",
                MastaInitWarning,
                stacklevel=2,
            )
            _warned_about_environment_variable = True

        return False

    full_path = path_to_dll_folder

    if not os.path.isdir(full_path):
        raise MastaInitException(
            (
                "Failed to initialise mastapy. Provided "
                "path '{}' is not a directory."
            ).format(full_path)
        )

    api_name = "SMT.MastaAPI.{}.dll".format(__api_version__)
    utility_api_name = "SMT.MastaAPIUtility.{}.dll".format(__api_version__)
    full_path = os.path.join(path_to_dll_folder, api_name)
    utility_full_path = os.path.join(path_to_dll_folder, utility_api_name)

    is_legacy_naming = False

    if not os.path.exists(full_path):
        if not __api_version__.startswith("10.2.3"):
            message = (
                "Failed to initialise mastapy. The version of MASTA is "
                "outdated for this version of mastapy. Please consider "
                f"updating MASTA to version {__api_version__} or "
                "installing an older version of mastapy."
            )
            raise MastapyVersionException(message)

        api_name = "MastaAPI.dll"
        utility_api_name = "MastaAPIUtility.dll"
        full_path = os.path.join(path_to_dll_folder, api_name)
        utility_full_path = os.path.join(path_to_dll_folder, utility_api_name)

        if not os.path.exists(full_path):
            raise MastaInitException(
                (
                    "Failed to initialise mastapy. Failed to find API DLL of "
                    "expected version {}. Do you have the correct version of "
                    "mastapy installed?"
                ).format(__api_version__)
            )

        is_legacy_naming = True

    initialise_python_net_importing(utility_full_path)
    _init_runtime(path_to_dll_folder)
    _init_dotnet_core_if_required(path_to_dll_folder)

    python_net_add_reference(os.path.join(path_to_dll_folder, "Utility.dll"))
    python_net_add_reference(full_path)
    python_net_add_reference(utility_full_path)

    if initialise_api_access:
        utility_methods = python_net_import("SMT.MastaAPI", "UtilityMethods")
        utility_methods.InitialiseApiAccess(path_to_dll_folder)

    if path_to_dll_folder not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + path_to_dll_folder

    if is_legacy_naming:
        _match_versions()

    _is_initialised = True
    return True


def init(path_to_dll_folder: str):
    """Initialise the Python to MASTA API interop.

    Args:
        path_to_dll_folder (str): Path to your MASTA folder that includes the
            SMT.MastaAPI.dll file
    """
    _init(path_to_dll_folder)


def _init_no_api_access(path_to_dll_folder: str):
    _init(path_to_dll_folder, initialise_api_access=False)


@deprecated(
    alternative="Use the debug button built into MASTA. You can find "
    "it next to the calculate button on scripted "
    "properties."
)
def start_debugging(
    host: Optional[str] = "localhost",
    port: Optional[int] = 5678,
    timeout: Optional[int] = 10,
    *,
    environment: Optional[DebugEnvironment] = (DebugEnvironment.VSCODE),
):
    """Start Python debugging using PTVSD.

    Args:
        host (str, optional): Debug server IP address. Default is 'localhost'.
        port (int, optional): Debug server port. Default is 5678.
        timeout (int, optional): How long the program will wait for a debugger
            to attach in seconds. Default is 10.
        environment (DebugEnvironment, optional): The debug environment. If
            set to DebugEnvironment.ANY this will be automatically detected.
            Default is DebugEnvironment.ANY.

    Note:
        Execution will pause until either a debugger is attached to the Python
        process, or the timout expires.
    """
    message = (
        f"Waiting for debugger to attach at {host}:{port} (execution "
        f"will time out in {timeout} seconds)..."
    )
    print(message)

    if environment == DebugEnvironment.VSCODE:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            import ptvsd

        ptvsd.enable_attach(address=(host, port), redirect_output=True)
        ptvsd.wait_for_attach(timeout)
    elif environment == DebugEnvironment.PYCHARM:
        try:
            import pydevd_pycharm
        except ModuleNotFoundError:
            message = (
                "PyCharm debugging was detected but the "
                "'pydevd_pycharm' package was not found. To use "
                "remote debugging in PyCharm, you must first install "
                "the correct version of the 'pydevd_pycharm' "
                "package.\n\n"
                "e.g. if your PyCharm version is 191.3490: "
                "'pip install pydevd_pycharm~=191.3490')\n\n"
                "For more information on this subject, visit "
                "https://www.jetbrains.com/help/pycharm/remote-"
                "debugging-with-product.html"
            )
            raise ModuleNotFoundError(message)
        else:
            pydevd_pycharm.settrace(host, port)
    else:
        message = (
            "The debug environment could not be identified. This could "
            "be because the debugger is not supported."
        )
        raise RuntimeError(message)
