# Inspect Recursive

Inspect Recursive is a Python package that provides functionality for inspecting the structure of Python objects recursively.

## Features

- Inspect the structure of Python objects, including nested dictionaries, lists, and other iterable objects.
- Print the structure of objects as a tree, displaying their types and contents.
- Handle specific types like NumPy arrays and pandas DataFrames, if installed.

## Installation

You can install Inspect Recursive using pip:

```bash
pip install inspect-recursive
```

## Usage

### inspect_object_structure

- Example 1: Inspecting a simple dictionary

```python
import inspect_recursive as ipr

simple_dict = {"a": 1, "b": 2, "c": 3}
ipr.what(simple_dict)
```

```output
<<<<<<<<<<<<<<<<<<<<inspector<<<<<<<<<<<<<<<<<<<<<
- object : <class 'dict'>
  >len=3 content-type=<class 'str'> vals="['a', 'b', 'c']"
  - idx0 : <class 'str'>
    >val="'a'"
  - idx1 : <class 'str'>
    >val="'b'"
> > > > > > > > > > > > > > > > > > > > > > > > >
```

- Example 2: Inspecting a nested dictionary

```python
import inspect_recursive as ipr
nested_dict = {"a": {"x": 1, "y": 2}, "b": {"z": 3}}
what(nested_dict)
```

```output
<<<<<<<<<<<<<<<<<<<<inspector<<<<<<<<<<<<<<<<<<<<<
- object : <class 'dict'>
  >len=2 content-type=<class 'str'> vals="['a', 'b']"
  - idx0 : <class 'str'>
    >val="'a'"
  - idx1 : <class 'str'>
    >val="'b'"
> > > > > > > > > > > > > > > > > > > > > > > > >
```

- Example 3: Inspecting a list of strings

```python
list_of_strings = ["apple", "banana", "cherry"]
what(list_of_strings)
```

```output
<<<<<<<<<<<<<<<<<<<<inspector<<<<<<<<<<<<<<<<<<<<<
- object : <class 'list'>
  >len=3 content-type=<class 'str'> vals="['apple', 'banana', 'cherry']"
  - idx0 : <class 'str'>
    >val="'apple'"
  - idx1 : <class 'str'>
    >val="'banana'"
> > > > > > > > > > > > > > > > > > > > > > > > >
```

- Example 4: Inspecting a more complex object

```python
import open3d as o3d

open3d_mesh = o3d.io.read_point_cloud(ply_filepath)

what(open3d_mesh, max_depth=6, thresh_iter_list=5, thresh_iter_dict=5)
```

```output
<<<<<<<<<<<<<<<<<<<<inspector<<<<<<<<<<<<<<<<<<<<<
- object : <class 'open3d.geometry.PointCloud'>
  >len=1000 content-type=<class 'open3d.utility.Vector3dVector'>
  - idx0 : <class 'open3d.utility.Vector3d'>
    >val="Vector3d(0.002537, -0.01984, -0.08411)"
  - idx1 : <class 'open3d.utility.Vector3d'>
    >val="Vector3d(-0.02286, -0.04225, -0.07801)"
  - idx2 : <class 'open3d.utility.Vector3d'>
    >val="Vector3d(-0.03108, -0.04534, -0.0755)"
  ...
  >len=3 content-type=<class 'numpy.ndarray'> ...
  >len=2 content-type=<class 'dict'> ...
  ...
> > > > > > > > > > > > > > > > > > > > > > > > >
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests on [GitHub](https://github.com/yourusername/inspect-recursive).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
