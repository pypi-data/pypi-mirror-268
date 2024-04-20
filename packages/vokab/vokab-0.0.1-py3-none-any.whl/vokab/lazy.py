import functools
import importlib
import sys
from typing import Any, Optional, Type

from vokab import logger


@functools.lru_cache(maxsize=None)
def lazy_import(
    library_name: str,
    attr_name: Optional[str] = None,
    return_none_on_error: bool = False,
) -> Any:
    """
    Lazily import a library or a specific attribute from a library.

    Args:
        library_name (str): The name of the library to import.
        attr_name (str, optional): Library attribute to import from library.
        return_none_on_error (bool, optional): Whether to return None if an
            import error occurs. Default is False, which raises an ImportError.

    Returns:
        The imported library or attribute, or None if an import error occurs
        and return_none_on_error is True.

    Raises:
        ImportError: If the library or attribute is not found and
        return_none_on_error is False.
    """
    info = _lib_info.get(library_name, {})

    module_name = info.get("module_name", library_name)
    install_name = info.get("install_name", library_name)
    purpose = info.get("purpose", "")
    license_type = info.get("license", "")
    url = info.get("url", "")
    version = info.get("version", "")

    try:
        module = importlib.import_module(module_name)
        if attr_name:
            return getattr(module, attr_name)
        return module
    except (ModuleNotFoundError, ImportError) as e:  # pragma: no cover
        version_info = f"(version {version})" if version else ""
        install = f"`pip install {install_name}{version_info}`"
        details = ", ".join(list(filter(None, [purpose, url, license_type])))
        details = f" ({details})" if details else ""
        msg = f"Import Failed: {install}{details}"

        if not info:
            additional_msg = (
                f"\nPlease add the library '{library_name}' to "
                f"the '_lib_info' dictionary in the 'fuzzimport' "
                f"module."
            )
            msg += additional_msg

        if return_none_on_error:
            return None
        else:
            logger.error(msg)
            sys.exit(1)


def create(base_type: Type, class_name: str, **kwargs):
    # lazy import class
    class_type: Type
    if class_name and isinstance(class_name, str) and "." in class_name:
        lib_name, klass_name = class_name.rsplit(".", maxsplit=1)
        class_type = lazy_import(
            lib_name, klass_name, return_none_on_error=True
        )

        is_valid = class_type and issubclass(class_type, base_type)
        if not is_valid:  # pragma: no cover
            logger.error(f"Invalid {base_type.__name__}: {class_name}")
            sys.exit(1)

        return class_type(**kwargs)


_lib_info = {
    "sqlite_vss": {
        "module_name": "sqlite_vss",
        "install_name": "sqlite-vss",
        "purpose": "Enables VSS support for SQLite",
        "license": "MIT",
        "url": "https://github.com/asg017/sqlite-vss",
    },
}

__all__ = ("lazy_import",)
