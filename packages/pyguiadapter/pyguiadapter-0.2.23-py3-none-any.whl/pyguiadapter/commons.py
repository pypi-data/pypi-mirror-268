import enum
import importlib.resources
import os
import warnings
from typing import TypeVar, Optional

from function2widgets.factory import ParameterWidgetFactory
from function2widgets.parser.function_parser import FunctionInfoParser

T = TypeVar("T")


ICON_FILE_EXT = ".svg"

__func_parser = FunctionInfoParser()
__widget_factory = ParameterWidgetFactory()


class DocumentFormat(enum.Enum):
    HTML = "html"
    MARKDOWN = "markdown"
    PLAIN = "plain"


def get_function_parser() -> FunctionInfoParser:
    global __func_parser
    return __func_parser


def get_param_widget_factory() -> ParameterWidgetFactory:
    global __widget_factory
    return __widget_factory


def get_res_dir() -> str:
    with importlib.resources.path("pyguiadapter", "res") as res_dir:
        return str(res_dir)


def get_icon_file(icon_name: str):
    if os.path.isfile(icon_name):
        return icon_name
    res_dir = get_res_dir()
    icons_dir = os.path.join(res_dir, "icons")
    icon_file = os.path.join(icons_dir, f"{icon_name}{ICON_FILE_EXT}")
    return icon_file


def safe_read(filename: str, encoding: str = "utf-8") -> Optional[str]:
    if not os.path.isfile(filename):
        return None
    try:
        with open(filename, "r", encoding=encoding) as f:
            return f.read()
    except BaseException as e:
        warnings.warn(f"failed to read file '{filename}': {e}")
        return None
