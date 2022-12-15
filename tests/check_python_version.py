import sys

from utils import constants

__all__ = ("check_python_version",)


def check_python_version():
    major: int = constants.MIN_MAJOR_PYTHON_VER
    minor: int = constants.MIN_MINOR_PYTHON_VER
    if (
            sys.version_info.major < major
            or sys.version_info.minor < minor
    ):
        raise Exception(f"Please use python version >= {major}.{minor}")
