"""This module provides functions for inspecting the structure of Python objects.

Functions
---------
repr_truncated(obj, length)
    Return a truncated string representation of the object.

inspect_object_structure_as_tree(obj, depth=0, obj_name="", **kwargs)
    Recursively inspect the structure of an object and print it as a tree.

inspect_object_structure(obj, max_depth=4, obj_name="", thresh_iter_list=1, thresh_iter_dict=3, thresh_repr_obj=100)
    Inspect the structure of an object and print it.
"""

import inspect
from typing import Iterable

# Handle specific types if pandas and numpy are installed
IS_NUMPY_INSTALLED = False
IS_PANDAS_INSTALLED = False

try:
    import numpy as np

    IS_NUMPY_INSTALLED = True
except ImportError:
    pass

try:
    import pandas as pd

    IS_PANDAS_INSTALLED = True
except ImportError:
    pass

__all__ = ["inspect_object_structure"]


def repr_truncated(obj: object, length: int):
    """Return a truncated string representation of the object.

    Parameters
    ----------
    obj : object
        The object to represent.
    length : int
        The maximum length of the representation.

    Returns
    -------
    str
        Truncated string representation of the object.

    Examples
    --------
    >>> repr_truncated("This is a long string", 10)
    "'This i[...]string'"
    >>> repr_truncated([1, 2, 3, 4, 5], 8)
    "[1, 2, [...], 5]"
    """
    text = repr(obj)
    length = length // 2
    assert length > 0
    if len(text) < 2 * length:
        return text
    return text[:length] + "[...]" + text[-length:]


def inspect_object_structure_as_tree(obj, depth=0, obj_name="", **kwargs):
    """Recursively inspect the structure of an object and print it as a tree.

    Parameters
    ----------
    obj : object
        The object to inspect.
    depth : int, optional
        The current depth in the object hierarchy. (default is 0)
    obj_name : str, optional
        The name of the object. (default is "")
    **kwargs : dict
        Additional keyword arguments for customization.

    Examples
    --------
    >>> data = {'a': 1, 'b': {'c': [1, 2, 3]}}
    >>> inspect_object_structure_as_tree(data)
    -  : <class 'dict'>
      - a : <class 'int'>
      - b : <class 'dict'>
        - c : <class 'list'>
          >len=3 content-type=<class 'int'> vals=[1, 2, 3]
    >>> inspect_object_structure_as_tree([1, 2, 3, 4, 5], obj_name="example_list")
    - example_list : <class 'list'>
      >len=5 content-type=<class 'int'> vals=[1, 2, 3, 4, 5]
    """
    max_depth = kwargs.get("max_depth", 4)
    thresh_iter_list = kwargs.get("thresh_iter_list", 1)
    thresh_iter_dict = kwargs.get("thresh_iter_dict", 3)
    thresh_repr_obj = kwargs.get("thresh_repr_obj", 100)

    if depth > max_depth:
        return

    inspect_object_structure_recursive = (
        lambda obj_, name_: inspect_object_structure_as_tree(
            obj=obj_, depth=depth + 1, obj_name=name_, **kwargs
        )
    )

    print("  " * depth + f"- {obj_name} : {type(obj)}")

    _is_builtin_or_method = isinstance(obj, type(print))
    _is_class_method = inspect.ismethod(obj)
    _is_function = inspect.isfunction(obj)

    if _is_builtin_or_method or _is_function or _is_class_method:
        try:
            print(
                "  " * (depth + 1)
                + f"Arguments: {inspect.signature(obj).parameters.keys()}"
            )
        except ValueError as e:
            if "no signature found for builtin" in str(e):
                pass  # print("  "*(n+1) + "no signature found for builtin")

        if _is_function:
            annotations = obj.__annotations__
            if annotations:
                print("  " * (depth + 1) + f"Annotations: {annotations}")
        return

    if IS_NUMPY_INSTALLED and isinstance(obj, np.ndarray):
        print(
            "  " * (depth + 1) + f">ndim={obj.ndim} shape={obj.shape} dtype={obj.dtype}"
        )

    if IS_PANDAS_INSTALLED and isinstance(obj, pd.DataFrame):
        print(
            "  " * (depth + 1)
            + f">shape={obj.shape} columns={repr_truncated(obj.columns,thresh_repr_obj)}"
        )

    if inspect.isgenerator(obj):
        obj = list(obj)

    elif isinstance(obj, (int, float, bool, str)):
        obj = repr(obj)

    elif isinstance(obj, (Iterable,)):
        obj = list(obj)

    if isinstance(obj, dict):
        _ = "  " * (depth + 1) + f">len={len(obj)}"
        _ += f" keys={repr_truncated(repr(obj.keys()),thresh_repr_obj)}"
        print(_)
        for idx, (key_, val_) in enumerate(obj.items()):
            if idx > thresh_iter_dict:
                break
            # if ctd_(n+1): print("  "*(n+1) + f">key={key_} content-type={type(val_)}")
            inspect_object_structure_recursive(val_, f"key{idx}: {key_}")
        return

    elif isinstance(obj, str):
        print("  " * (depth + 1) + f">val={repr_truncated(obj, thresh_repr_obj)}")
        return

    elif isinstance(obj, (list,)):
        if not obj:
            return
        _ = "  " * (depth + 1) + f">len={len(obj)}"
        _ += f" content-type={type(obj[0])} vals={repr_truncated(repr(obj),thresh_repr_obj)}"
        print(_)
        for idx, val_ in enumerate(obj):
            if idx > thresh_iter_list:
                break
            inspect_object_structure_recursive(val_, f"idx{idx}")
        return

    for key in dir(obj):
        if key.startswith("_"):
            continue
        try:
            att = getattr(obj, key)
            inspect_object_structure_recursive(att, key)
        except Exception as e:
            continue


def inspect_object_structure(
    obj,
    max_depth=4,
    obj_name="",
    thresh_iter_list=1,
    thresh_iter_dict=3,
    thresh_repr_obj=100,
):
    """Inspect the structure of an object and print it.

    Parameters
    ----------
    obj : object
        The object to inspect.
    max_depth : int, optional
        The maximum depth to traverse while inspecting. (default is 4)
    obj_name : str, optional
        The name of the object. (default is "")
    thresh_iter_list : int, optional
        Threshold for iteration on lists. (default is 1)
    thresh_iter_dict : int, optional
        Threshold for iteration on dictionaries. (default is 3)
    thresh_repr_obj : int, optional
        Threshold for object representation length. (default is 100)

    Examples
    --------
    >>> data = {'a': 1, 'b': {'c': [1, 2, 3]}}
    >>> inspect_object_structure(data)
    inspector<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    -  : <class 'dict'>
      - a : <class 'int'>
      - b : <class 'dict'>
        - c : <class 'list'>
          >len=3 content-type=<class 'int'> vals=[1, 2, 3]
    >>> inspect_object_structure([1, 2, 3, 4, 5], obj_name="example_list")
    inspector<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    - example_list : <class 'list'>
      >len=5 content-type=<class 'int'> vals=[1, 2, 3, 4, 5]
    """
    print("inspector".center(50, "<"))
    max_depth = int(max_depth)
    obj_name = str(obj_name) or "object"
    kwargs = {
        "max_depth": max_depth,
        "obj_name": obj_name,
        "depth": 0,
        "thresh_iter_list": thresh_iter_list,
        "thresh_iter_dict": thresh_iter_dict,
        "thresh_repr_obj": thresh_repr_obj,
    }
    inspect_object_structure_as_tree(obj, **kwargs)
    print(25 * "> ", "\n")
