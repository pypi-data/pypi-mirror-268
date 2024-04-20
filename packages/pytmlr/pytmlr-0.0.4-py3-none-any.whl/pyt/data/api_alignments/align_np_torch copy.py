import inspect, numpy as np, torch, os, os.path as osp, types, re, sys, ast
from typing import Type
from IPython import embed
from pathlib import Path
from pyt import load, dump

np_path = Path(np.__file__).parent
torch_path = Path(torch.__file__).parent
torch_pyi = torch_path / "_C/__init__.pyi"

torch_ast_obj = ast.parse(load(torch_pyi, file_format="txt"))


def dfs_node(node, name=None):
    if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
        if node.name == name:
            return node
    for child in ast.iter_child_nodes(node):
        ret = dfs_node(child, name)
        if ret is not None:
            return ret
    return None


def get_default_args_from_doc(doc, name=None):
    doc = doc.strip().split("\n")[0].strip()
    if name is not None:
        groups = re.findall(rf"({name}\(.*\))")
        assert len(groups) == 1
        doc = groups[0]
    
    
    print(doc)
    exit(0)


def get_default_args_from_ast(node):
    doc_str = func.__doc__.strip()


def get_default_args(func):
    signature = inspect.signature(func)
    ret = {}
    for k, v in signature.parameters.items():
        if v.default is not inspect.Parameter.empty:
            ret[k] = v.default
        else:
            ret[k] = "__None__"
    return ret


def get_module_functions(module=np):
    functions = []
    for name in dir(module):
        if name.startswith("_") or name.endswith("_"):
            continue
        if not callable(getattr(module, name)):
            continue
        if "Warning" in name or "Error" in name:
            continue
        if inspect.isclass(getattr(module, name)):
            continue
        if name[0].lower() != name[0]:
            continue
        functions.append(name)
    print(f"#functions: {len(functions)}")
    func_args = {}
    failed_funcs = []
    deprecated_funcs = []
    for name in functions:
        func = getattr(module, name)
        doc_str = func.__doc__
        if doc_str is not None and "is deprecated" in doc_str:
            deprecated_funcs.append(name)
            continue
        try:
            arguments = get_default_args(func)
            func_args[name] = arguments
        except:
            failed_funcs.append(name)
            if func.__doc__ is None:
                assert module is torch, f"{module}.{name} has no doc"
                node = dfs_node(torch_ast_obj, name)
                func_args[name] = node
            else:
                func_args[name] = get_default_args_from_doc(doc_str, name)
    func_type = []
    for name in failed_funcs:
        named_type = type(getattr(module, name))
        # print(func, getattr(module, name), type(getattr(module, name)))
        
        if named_type not in func_type:
            func_type.append(named_type)
    print(func_type)
    

def align_array():
    np_array = np.random.rand(10, 10)
    torch_tensor = torch.from_numpy(np_array)
    np_funcs = [
        name
        for name in dir(np_array)
        if not (name.startswith("_") or name.endswith("_"))
        and callable(getattr(np_array, name))
    ]
    torch_funcs = [
        name
        for name in dir(torch_tensor)
        if not (name.startswith("_") or name.endswith("_"))
        and callable(getattr(torch_tensor, name))
    ]
    shared_funcs = set(np_funcs) & set(torch_funcs)
    extra_np_funcs = set(np_funcs) - shared_funcs
    extra_torch_funcs = set(torch_funcs) - shared_funcs
    print(f"shared: {len(shared_funcs)}")
    print(f"extra_np: {len(extra_np_funcs)}")
    print(f"extra_torch: {len(extra_torch_funcs)}")


def align_func():
    np_funcs = [
        name
        for name in dir(np)
        if not (name.startswith("_") or name.endswith("_"))
        and callable(getattr(np, name))
    ]
    # print(type(torch.sum))
    # exit(0)
    torch_funcs = [
        name
        for name in dir(torch)
        if not (name.startswith("_") or name.endswith("_"))
        and callable(getattr(torch, name))
    ]
    shared_funcs = set(np_funcs) & set(torch_funcs)
    extra_np_funcs = set(np_funcs) - shared_funcs
    extra_torch_funcs = set(torch_funcs) - shared_funcs
    ufuncs = sorted(
        [name for name in shared_funcs if isinstance(getattr(np, name), np.ufunc)]
    )
    other_shared_funcs = sorted(shared_funcs - set(ufuncs))

    print(f"other_shared_funcs: {len(other_shared_funcs)}")
    print(f"shared: {len(other_shared_funcs) + len(ufuncs)}")
    print(f"extra_np: {len(extra_np_funcs)}")
    print(f"extra_torch: {len(extra_torch_funcs)}")
    """
    for func in extra_np_funcs:
        print(func)
    print("===========")
    print("extra_torch_funcs:")
    for func in extra_torch_funcs:
        print(func)
    exit(0)
    """
    # print(os.path.abspath(inspect.getfile(inspect.unwrap(np.dot))))
    # exit(0)

    count = 0
    funcs = other_shared_funcs
    for name in other_shared_funcs:
        np_func = getattr(np, name)
        torch_func = getattr(torch, name)
        
        # print(np_func)

        # if inspect.ismethodwrapper(np_func):
        #     np_func = inspect.unwrap(np_func)
        # if inspect.ismethodwrapper(torch_func):
        #     torch_func = inspect.unwrap(torch_func)

        # torch.all
        # from varname import argname

        # np.dot
        # print(name, np_func)
        
        try:
            arguments = get_default_args(np_func)
            arguments = {key: str(value) for key, value in arguments.items()}
        except:
            print(f"Failed {name}")
            count += 1
            continue
        
        print(name, arguments)
        embed()
        exit(0)
        print(inspect.getargspec(torch_func))
        # exit(0)
        torch_code = inspect.getsource(torch_func)
        exit(0)
        """
        # np.transpose()
        # print(np_func, np_func.signature)
        print(np_func.__code__.co_varnames)
        )
        print(torch_func)
        exit(0)
        print(inspect.getargspec(np_func))
        exit(0)

        np_names = np_func.__code__.co_varnames
        torch_names = torch_func.__code__.co_varnames
        print(np_names, torch_names)
        exit(0)
        """
    print(count, len(funcs))


# get_parameter_count(np.zeros)
# exit(0)


# parse_torch_pyi()
# exit(0)
get_module_functions(np)
# get_module_functions(torch)
