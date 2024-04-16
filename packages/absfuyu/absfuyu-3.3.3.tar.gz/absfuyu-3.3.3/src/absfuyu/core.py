"""
Absfuyu: Core
-------------
Contain type hints and other stuffs

Version: 2.2.0
Date updated: 14/04/2024 (dd/mm/yyyy)
"""

# Module Package
###########################################################################
__all__ = [
    # color
    "CLITextColor",
    # path
    "CORE_PATH",
    "CONFIG_PATH",
    "DATA_PATH",
]

__package_feature__ = ["beautiful", "extra", "res", "full", "dev"]


from pathlib import Path

# import sys
# from sys import version_info as _python_version

# if sys.version_info.minor >= 10:
#     from importlib.resources import files
# else:
#     try:
#         from importlib_resources import files
#     except:
#         raise ImportError("Please install importlib-resources")


class CLITextColor:
    """Color code for text in terminal"""

    WHITE = "\x1b[37m"
    BLACK = "\x1b[30m"
    BLUE = "\x1b[34m"
    GRAY = "\x1b[90m"
    GREEN = "\x1b[32m"
    RED = "\x1b[91m"
    DARK_RED = "\x1b[31m"
    MAGENTA = "\x1b[35m"
    YELLOW = "\x1b[33m"
    RESET = "\x1b[39m"


CORE_PATH = Path(__file__).parent.absolute()
# CORE_PATH = files("absfuyu")
CONFIG_PATH = CORE_PATH.joinpath("config", "config.json")
DATA_PATH = CORE_PATH.joinpath("pkg_data")
