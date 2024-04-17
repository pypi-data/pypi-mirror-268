"""python_net.py

Utility module for importing python net modules.
"""

from __future__ import annotations

import os
import warnings
from typing import Optional, Any


utility_dll = None
FileNotFoundException = None
FileLoadException = None


class AssemblyLoadError(Exception):
    """Exception raised if there is a problem loading an assembly."""


def initialise_python_net_importing(utility_dll_path: str):
    """Initialise the Python.NET importing.

    By providing the path to the MASTA API Utility assembly, we can ensure
    we are importing from the correct assembly.

    Args:
        utility_dll_path (str): Path to the MASTA API Utility assembly
    """
    global utility_dll

    if not os.path.exists(utility_dll_path):
        raise FileNotFoundError("Failed to find the MASTA API Utility assembly.")

    utility_dll = utility_dll_path


def python_net_add_reference(path: str) -> Any:
    """Add a reference to a .NET assembly and return the assembly.

    Args:
        path (str): Path to the assembly.

    Returns:
        Any
    """
    global FileNotFoundException, FileLoadException
    import clr

    if FileNotFoundException is None or FileLoadException is None:
        FileNotFoundException = python_net_import("System.IO", "FileNotFoundException")
        FileLoadException = python_net_import("System.IO", "FileLoadException")

    try:
        return clr.AddReference(path)
    except (FileNotFoundException, FileLoadException) as e:
        message = (
            f'Failed to load the assembly "{path}" or one of its '
            "dependencies. If you are on Windows and using a portable "
            "version of MASTA it is possible that files are being "
            "blocked. If you are distributing a portable version of "
            "MASTA locally from one computer to another, ensure that "
            "it is distributed as a single archive file (such as "
            ".zip) and unpacked on the target computer.\n\n"
            f"{e.message}"
        )
        raise AssemblyLoadError(message) from None


def python_net_import(module: str, class_name: Optional[str] = None):
    """Dynamically import a Python.NET module.

    Args:
        module (str): Module path
        class_name (str, optional): class name
    """
    try:

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)

            path = list(filter(None, module.split(".")))
            m = __import__(path[0])

            for p in path[1:]:
                m = getattr(m, p)

            if class_name:
                m = getattr(m, class_name)
    except ImportError:
        raise ImportError(
            (
                "\"mastapy\" has not been initialised. Call 'mastapy.init()' "
                "with the path to your SMT.MastaAPI.dll file."
            )
        ) from None
    except Exception:
        raise ImportError(
            "Failed to load {} from {}.".format(class_name, module)
        ) from None

    return m
