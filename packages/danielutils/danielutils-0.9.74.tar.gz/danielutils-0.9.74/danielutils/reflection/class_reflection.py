import inspect
from typing import Any, List as t_list
from .interpreter import get_python_version

if get_python_version() >= (3, 9):
    from builtins import list as t_list  # type:ignore


def get_explicitly_declared_functions(cls: type) -> t_list[str]:
    """
    Returns the names of the functions that are explicitly declared in a class.

    This function does not return inherited functions.

    Args:
        cls (type): The class to inspect.

    Returns:
        list[str]: A list of names of the functions explicitly declared in the class.
    """
    return [func for func, val in inspect.getmembers(cls, predicate=inspect.isfunction)]


def get_mro(obj: Any) -> t_list[type]:
    """returns the mro of an object

    Args:
        obj (Any): any object, instance or class

    Returns:
        list[type]: the resulting mro for the object
    """
    if isinstance(obj, type):
        return obj.mro()
    return get_mro(obj.__class__)


__all__ = [
    "get_explicitly_declared_functions",
    "get_mro"
]
