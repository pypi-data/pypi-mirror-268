from numbers import Number, Integral
from collections.abc import Sequence
import numpy as np, os


"""  For python basic type  """


def is_none(item):
    return item is None


def is_not_none(item):
    return item is not None


def is_slice(item):
    return isinstance(item, slice)


def is_str(item):
    return isinstance(item, str)


def is_dict(item):
    return isinstance(item, dict)


def is_dict_group(item):
    from h5py import Group
    return isinstance(item, (dict, Group))


def is_num(item):
    return isinstance(item, Number) or np.isscalar(item)


def is_integer(item):
    return isinstance(item, Integral)


def is_type(item):
    return isinstance(item, type)


def get_parent_types(item):
    if not is_type(item):
        item = type(item)
    ret = [item]
    for parent_type in item.__bases__:
        ret.extend(get_parent_types(parent_type))
    return ret


def is_instance(item, classname):
    if isinstance(classname, str):
        classname = [classname]
    types = get_parent_types(item)
    for item in types:
        if item.__name__ in classname:
            return True
    return False


def is_seq_of(seq, expected_type=None, seq_type=None):
    seq_type = Sequence if seq_type is None else seq_type
    assert isinstance(seq_type, type), f"seq_type must be a type, but got {type(seq_type)}!"

    if not isinstance(seq, seq_type):
        return False
    if expected_type is not None:
        for item in seq:
            if not isinstance(item, expected_type):
                return False
    return True


def is_list_of(seq, expected_type=None):
    return is_seq_of(seq, expected_type, seq_type=list)


def is_tuple_of(seq, expected_type=None):
    return is_seq_of(seq, expected_type, seq_type=tuple)


def is_iterable(item):
    return isinstance(item, (dict, tuple, list))


"""  For numpy and torch type  """


def get_dtype(item):
    if isinstance(item, (list, tuple)):
        item = item[0]

    if hasattr(item, "dtype"):
        return str(item.dtype).split(".")[-1]
    elif isinstance(item, (int, float, bytes, str)):
        return type(item)
    else:
        return None


def get_attr(item, name, default=None):
    return getattr(item, name, default)


def is_np(item):
    return isinstance(item, np.ndarray) or is_num(item)


def is_np_arr(item):
    return isinstance(item, np.ndarray)


def is_torch(item):
    if not is_instance(item, "Tensor"):
        return False
    import torch

    return isinstance(item, torch.Tensor)


def is_pcd(item, axis=-1):
    return item.shape[axis] == 3


def is_torch_distribution(item):
    if not is_instance(item, "Distribution"):
        return False
    import torch

    return isinstance(item, torch.distributions.Distribution)


def is_arr(item):
    return is_np_arr(item) or is_torch(item)


def get_arr_type(item):
    if is_np_arr(item):
        return "np"
    elif is_torch(item):
        return "torch"
    return None


def get_type_info(item):
    if is_np_arr(item):
        if item.dtype.kind == "f":
            return np.finfo(item.dtype)
        elif item.dtype.kind == "i":
            return np.iinfo(item.dtype)
    elif is_torch(item):
        import torch

        if item.dtype.is_floating_point:
            return torch.finfo(item.dtype)
        elif item.dtype.is_integral:
            return torch.iinfo(item.dtype)
    return None


"""  For HDF5 type  """


def is_h5(item):
    from h5py import File, Group, Dataset
    return isinstance(item, (File, Group, Dataset))


def get_default_dtype():
    return os.environ.get("DTYPE", "float32")
