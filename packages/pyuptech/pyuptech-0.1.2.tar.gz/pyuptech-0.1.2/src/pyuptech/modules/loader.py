import ctypes
from functools import lru_cache

from .logger import _logger


@lru_cache(maxsize=None)
def load_lib(lib_file_path: str) -> ctypes.CDLL | None:
    """
    Load a dynamic library from the given file path and return a ctypes.CDLL object.

    Args:
        lib_file_path (str): The file path of the dynamic library to load.

    Returns: ctypes.CDLL | None: A ctypes.CDLL object representing the loaded library, or None if the library could
    not be loaded.

    Raises:
        Exception: If there is an error loading the library.

    Note: This function uses the lru_cache decorator to cache the loaded libraries, so subsequent calls with the same
    file path will return the cached library object.

    """

    try:
        obj = ctypes.cdll.LoadLibrary(lib_file_path)
    except Exception as e:
        _logger.critical(f"Can't load lib [{lib_file_path}],{e}")
        return None
    _logger.info(f"Lib [{lib_file_path}] loaded")
    return obj


if __name__ == "__main__":
    pass
