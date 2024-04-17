"""This package provides functionality for inspecting Python object structures.

Functions
---------
what(obj, max_depth=4, obj_name="", thresh_iter_list=1, thresh_iter_dict=3, thresh_repr_obj=100)
    Inspect the structure of an object and print it.

Examples
--------
Usage examples:
    >>> import inspect_recursive as ipr
    >>> simple_dict = {"a": 1, "b": 2, "c": 3}
    >>> ipr.what(simple_dict)
    inspector<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    -  : <class 'dict'>
      - a : <class 'int'>
      - b : <class 'int'>
      - c : <class 'int'>
    
    >>> nested_dict = {"a": {"x": 1, "y": 2}, "b": {"z": 3}}
    >>> ipr.what(nested_dict)
    inspector<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    -  : <class 'dict'>
      - a : <class 'dict'>
        - x : <class 'int'>
        - y : <class 'int'>
      - b : <class 'dict'>
        - z : <class 'int'>
    
    >>> list_of_strings = ["apple", "banana", "cherry"]
    >>> ipr.what(list_of_strings)
    inspector<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    -  : <class 'list'>
      >len=3 content-type=<class 'str'> vals=['apple', 'banana', 'cherry']
"""

from .inspect_object_structure import inspect_object_structure as what

all = ["what"]
