import inspect, numpy as np, torch, os, os.path as osp, types, re, sys, ast
from typing import Type
from IPython import embed
from pathlib import Path
from pyt import load, dump
from copy import deepcopy
from collections import OrderedDict

__folder__ = Path(__file__).parent
np_path = Path(np.__file__).parent
torch_path = Path(torch.__file__).parent
torch_pyi = torch_path / "_C/__init__.pyi"

torch_ast_obj = ast.parse(load(torch_pyi, file_format="txt"))


def dfs_node(node, name=None):
    if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
        if node.name == name:
            print(f"Find! {name}")
            return node
        else:
            return None
        
    for child in ast.iter_child_nodes(node):
        ret = dfs_node(child, name)
        if ret is not None:
            return ret
    return None


def get_default_args_from_doc(doc, name=None, is_np=True):
    line = "".join([_.strip() for _ in doc.strip().split("\n")[:2]])
    full_doc = doc.strip()
    doc = line
    if "(a1, a2, ...)" in doc:
        doc = doc.replace("(a1, a2, ...),", "arys, /,")
    if len(re.findall(rf"{name}\((.*)\)", doc)) == 0:
        if not ("," in doc or "Tensor" in doc):
            assert "Parameters" in full_doc or "Args" in full_doc, f"{name}, {full_doc}"
            doc = re.split(r"Return|Returns", full_doc)[0]
            doc = re.split(r"Parameters|Args", doc)[-1].strip(": \n\\")
            # args = re.split(r", ", doc)
            lines = doc.split("\n")
            # if "---" in full_doc:
            #     print(full_doc)
            
            flag = 1
            
            def clean_up(lines):
                for i, line in enumerate(lines):
                    print(line)
                    if ":" not in line:
                        lines[i] = ""
                        continue
                    line = re.split(r":", re.split(r"->", line)[0])[0]
                    for key in ["(torch.Size.*)", "(torch.Tensor.*)", "(torch.Tensor.*)"]:
                        line = re.sub(key, "", line)
                    lines[i] = line.replace("`", "")
                lines = [_.strip() for _ in lines if len(_.strip()) > 0 and  "---" not in _]
                return lines
            
            lines = clean_up(lines)
            doc = ",".join(lines)
            # if "---" in full_doc:
            #     print("??", doc)
            #     exit(0)
        elif len(re.findall(rf"\((.*)\)", doc)) > 0:
            doc = re.findall(rf"\((.*)\)", doc)[0]
            flag = 2
            pass
        else:
            embed()
            assert False, f"{name}: {doc}"
    else:
        flag = 3
        doc = re.split(r"->", doc)[0]
        groups = re.findall(r"\((.*)\)", doc)
        assert len(groups) == 1, f"{name}: {line}"
        doc = groups[0]
    print(f"func {name}", flag, doc)
        
    
    # We only use args for those that can only passed by position
    if "/" in doc:
        assert is_np
        splits = doc.split("/")
        assert len(splits) <= 2
        args = splits[0]
        kwargs = splits[1]
    elif "=" not in doc:
        args = doc
        kwargs = ""
    else:
        args = ""
        kwargs = doc
    
    # groups = re.findall(rf"\[(.*)\]", kwargs)
    # assert len(groups) <= 1
    # if len(groups) == 1:
    #     # We will not support optional arguments
    #     kwargs = kwargs.replace(f"[{groups[0]}]", "")
    if "*," in kwargs:
        
        splits = list(re.split(r"\*,", kwargs))
        assert len(splits) == 2, f"{splits}"
        
        for i, split in enumerate(splits):
            if not (i == 0 and "/" in doc):
                continue
            groups = re.findall(rf"\[(.*)\]", split)
            assert len(groups) <= 1
            for group in groups:
                # We will not support optional arguments
                split = split.replace(f"[{group}]", "")
            splits[i] = split
        
        if is_np:
            splits[0] = splits[0].replace("[", "").replace("]", "")
            kwargs = ", ".join(splits)
            kwargs = kwargs.replace("[", "").replace("]", "")
        else:
            args = splits[0]
            kwargs = splits[1]
        # print(args, kwargs)
    # else:
    #     kwargs = ""
    if name not in ["rot90"]:
        args = args.replace("[", "").replace("]", "")
    args = re.split(r", ", args)
    tmp_args = []
    for arg_i in args:
        if (arg_i.count("=") > 1 or name == "clip") and "," in arg_i:
            tmp_args += list(arg_i.split(","))
        else:
            tmp_args.append(arg_i)
    args = tmp_args
    
    kwargs = re.split(r", ", kwargs)
    tmp_kwargs = []
    for arg_i in kwargs:
        if arg_i.count("=") > 1 and "," in arg_i:
            tmp_kwargs += list(arg_i.split(","))
        else:
            tmp_kwargs.append(arg_i)
    kwargs = tmp_kwargs
    
    args = [_.strip() for _ in args if len(_.strip()) > 0 and _.strip() != "*" and not _.startswith("..")]
    kwargs = [_.strip() for _ in kwargs if len(_.strip()) > 0  and _.strip() != "*"]
    
    args = [_.split("=") for _ in args]
    for i, arg_i in enumerate(args):
        assert len(arg_i) == 1 or len(arg_i) == 2
        if len(arg_i) == 1:
            args[i] = [arg_i[0], "__None__"]
        else:
            args[i] = [arg_i[0], eval(arg_i[1])]
    
    kwargs = [_.split("=") for _ in kwargs]
    ret_kwargs = OrderedDict()
    for i, kwargs_i in enumerate(kwargs):
        assert len(kwargs_i) == 1 or len(kwargs_i) == 2
        if len(kwargs_i) == 1:
            ret_kwargs[kwargs_i[0]] = "__None__"
        else:
            ret_kwargs[kwargs_i[0]] = eval(kwargs_i[1])
    return args, ret_kwargs


def get_default_args(func):
    signature = inspect.signature(func)
    full_str = str(signature)
    if "/" in full_str:
        splits = full_str.split("/")
        assert len(splits) == 2
        args_str = splits[0]
    else:
        args_str = ""
        
    args = []
    kwargs = OrderedDict()
    for k, v in signature.parameters.items():
        if k in ["args", "kwargs"]:
            print("Error", func, k)
            raise NameError
        value = "__None__"
        if v.default is not inspect.Parameter.empty:
            value = v.default
        if isinstance(value, np._globals._NoValueType):
            value = "__None__"
        if f"*{k}" in full_str:
            k = f"*{k}"
        if f"{k}" in args_str or k.startswith("*"):
            args.append([k, value])
        else:
            kwargs[k] = value
    # print(args, kwargs)
    return args, kwargs


def get_module_functions(module=np, required_names=None):
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
        if name.lower() != name:
            continue
        if required_names is not None and name not in required_names:
            continue
        if name.startswith("set_") or name.startswith("get_") or name.startswith("is_") or "autocast" in name:
            continue
        if "copy" in name and name != "copy":
            continue
        if name in ["array", "Tensor", "tensor", "load", "save", "candidate", "wait", "obj", "arange"]:
            continue
        functions.append(name)
    print(f"#functions: {len(functions)}")
    func_args = {}
    failed_funcs = []
    deprecated_funcs = []
    
    # print(get_default_args(torch.zeros_like))
    # get_default_args_from_doc(torch.zeros_like.__doc__, "zeros_like")
    # exit(0)
    
    
    for i, name in enumerate(functions):
        # if name != "arange":
        #     continue
        print(f"Process {i}-th function", name)
        
        # np.repeat
        
        # if name == "repeat":
        #     print("!", name, module, doc_str)
        
        func = getattr(module, name)
        doc_str = func.__doc__
        if doc_str is not None:
            doc_str = doc_str.strip()
            if "is deprecated" in doc_str:
                deprecated_funcs.append(name)
                continue
        
        try:
            arguments = get_default_args(func)
            func_args[name] = (True, arguments)
        except Exception as e:
            if doc_str is not None:
                func_args[name] = (False, get_default_args_from_doc(doc_str, name, is_np=module is np))
                print(func_args[name])
            else:
                failed_funcs.append(name)
        # print(func_args[name])
        # exit(0)
    print("Final function", len(func_args))
    return func_args


IDENTITY = ["axis", "keepdims", "a", "b", "end", "atol", "rtol", "equal_nan", "start", "step", "dtype", "out", "device", "requires_grad", "copy", "layout", "minlength", "weights", "to", "from", "rounding_mode", "shape", "memory_format", "pin_memory", "buffer", "count", "offset", "type1", "type2", "n", "m", "condition", "*shapes", "a_min", "a_max", "rowvar", "bias", "ddof", "fweights", "aweights", "correction", "axisa", "axisb", "axisc", "diagonal", "prepend", "append", "indices_or_sections", "equation", "*operands", "optimize"]

# numpy -> unifie
UNIFIED_API_NP = {
    "array": "a",
    "ary": "a",
    "subscripts": "equation",
    "x": "a",
    "m": "a",
    "z": "a",
    "v": "a",
    "x1": "a",
    "prototype": "a",
    "x2": "b",
    "y": "b",
    "k": "diagonal",
    "arys": "arrays",
    "stop": "end",
    "from_": "from",
    "*arys": "*arrays",
    "*args": "*shapes",
    "tup": "arrays",
}

# torch -> unifie
UNIFIED_API_TORCH = {
    "Tensor": "a",
    "obj": "a",
    "input": "a",
    "dividend": "a",
    "other": "b",
    "exponent": "b",
    "values": "b",
    "divisor": "b",
    "row": "n",
    "col": "m",
    "keepdim": "keepdims",
    "dim": "axis",
    "tensors": "arrays",
    "*tensors": "*arrays",
    "*size": "shape",
    "min": "a_min",
    "max": "a_max",
}

# torch -> numpy
"""
repeat() behaves differently from numpy.repeat, but is more similar to numpy.tile. For the operator similar to numpy.repeat, see torch.repeat_interleave().
"""
SPECIAL_FUNC_NAME = {
    "repeat": "tile",
    "repeat_interleave": "repeat",
}

INVERSE_SPECIAL_FUNC_NAME = {v: k for k, v in SPECIAL_FUNC_NAME.items()}


def check_function(ret, name):
    # {"np name": np_name_mapping, "torch name": torch_name_mapping, "default value": default_value, "np required args": np_required_args, "torch required args": torch_required_args}
    
    np_name_mapping = ret[name]["np_name"]
    torch_name_mapping = ret[name]["torch_name"]
    default_value = ret[name]["default_value"]
    np_required_args = ret[name]["np_required_args"]
    torch_required_args = ret[name]["torch_required_args"]
    
    if "cum" in name and "axis" in default_value:
        default_value["axis"] = 0
    
    
    if name in ["frombuffer"]:
        return
    
    np_func = getattr(np, name)
    torch_func = getattr(torch, SPECIAL_FUNC_NAME.get(name, name))
    np.random.seed(0)
    
    np_kwargs = deepcopy(default_value)
    torch_kwargs = deepcopy(default_value)
    value_range = [-1, 1]
    
    size = (1, 10)
    dtype = np.float64
    if name == "arcsinh":
        value_range = [-10, 10]
    elif name in ["arccosh", "float_power", "log", "log10", "log2", "sqrt"]:
        value_range = [1, 10]
    elif name == "bincount" or "bitwise" in name:
        value_range = [0, 100]
        size = (10, )
        dtype = np.int64
    elif name in ["dot", "vdot"]:
        size = (10, )
    elif name in ["dsplit"]:
        size = (10, 10, 10)
    elif name in ["cross"]:
        size = (10, 3)
    elif name in ["gcd", "lcm"]:
        value_range = [0, 1000]
        dtype = np.int64
    elif name == "ldexp":
        value_range = [0, 10]
        dtype = np.int64
    
    contain_multi = False
    for key in default_value:
        if default_value[key] == "__None__":
            if key in ["a", "b"]:
                np_kwargs[key] = dtype(np.random.rand(*size) * (value_range[1] - value_range[0]) + value_range[0])
                torch_kwargs[key] = torch.from_numpy(np_kwargs[key]).clone()
            elif key == "start":
                np_kwargs[key] = 0
                torch_kwargs[key] = 0
            elif key == "end":
                np_kwargs[key] = 10
                torch_kwargs[key] = 10
            elif key == "from":
                np_kwargs[key] = np.float32
                torch_kwargs[key] = torch.float32
            elif key == "to":
                np_kwargs[key] = np.float64
                torch_kwargs[key] = torch.float64
            elif key in ["arrays", "*arrays", "*operands"]:
                arrays = [np.random.rand(10, 10), np.random.rand(10, 10)]
                np_kwargs[key] = arrays
                torch_kwargs[key] = [torch.from_numpy(_).clone() for _ in arrays]
            elif key == "shape":
                np_kwargs[key] = (10, 10)
                torch_kwargs[key] = (10, 10)
            elif key == "dtype":
                np_kwargs[key] = np.float32
                torch_kwargs[key] = torch.float32
            elif key == "type1":
                np_kwargs[key] = np.float32
                torch_kwargs[key] = torch.float32
            elif key == "type2":
                np_kwargs[key] = np.float64
                torch_kwargs[key] = torch.float64
            elif key == "*shapes":
                np_kwargs[key] = torch_kwargs[key] = ((1, 2), (3, 1), (3, 2))
            elif key == "condition":
                np_kwargs[key] = np.random.rand(*size) > 0.5
                torch_kwargs[key] = torch.from_numpy(np_kwargs[key]).clone()
            elif key == "indices_or_sections":
                np_kwargs[key] = torch_kwargs[key] = 2
            elif key == "equation":
                np_kwargs[key] = torch_kwargs[key] = "ij,jk->ik"
            else:
                assert False, f"We do not support {key} for function {name}!"
            if "*" in key:
                assert len(default_value) == 1
                args_only = True
        else:
            if key == "a_min":
                np_kwargs[key] = 0
                torch_kwargs[key] = 0
            elif key == "a_max":
                np_kwargs[key] = 0.5
                torch_kwargs[key] = 0.5
                
    np_kwargs = {_: np_kwargs[_] for _ in np_kwargs}
    num_args = len(np_required_args)
    np_args = []
    if num_args > 0:
        np_args = [None for i in range(num_args)]
        for key, idx in np_required_args.items():
            np_args[idx] = np_kwargs.pop(key)
        for i in range(len(np_required_args)):
            if i not in np_required_args.values():
                raise ValueError
    np_kwargs = {np_name_mapping[_]: np_kwargs[_] for _ in np_kwargs}
    
    extra_np_keys = ["device", "requires_grad", "copy", "pin_memory", "memory_format"]
    np_kwargs = {key: np_kwargs[key] for key in np_kwargs if key not in extra_np_keys and np_kwargs[key] is not None}
            
    print("Run np with", np_args, np_kwargs)
    if args_only:
        assert len(np_kwargs) + len(np_args) == 1
        if len(np_kwargs) == 1:
            x = np_func(*np_kwargs[list(np_kwargs.keys())[0]])
        else:
            x = np_func(*np_args[0])
    else:
        x = np_func(*np_args, **np_kwargs)
    
    num_args = len(torch_required_args)
    torch_args = []
    if num_args > 0:
        torch_args = [None for i in range(num_args)]
        for key, idx in torch_required_args.items():
            torch_args[idx] = torch_kwargs.pop(key)
        for i in range(len(torch_required_args)):
            if i not in torch_required_args.values():
                raise ValueError
    print("Run torch with", torch_args, torch_kwargs)
    
    for key in ["memory_format"]:
        if key in torch_kwargs:
            torch_kwargs[key] = eval(torch_kwargs[key])
    
    torch_kwargs = {torch_name_mapping[_]: torch_kwargs[_] for _ in torch_kwargs if torch_kwargs[_] is not None}
    
    if args_only:
        y = torch_func(*torch_kwargs[list(torch_kwargs.keys())[0]])
    else:
        y = torch_func(*torch_args, **torch_kwargs)
    if isinstance(y, torch.Tensor):
        y = y.cpu().numpy()
    
    if name in ["empty", "empty_like"]:
        assert tuple(x.shape) == tuple(y.shape)
    elif isinstance(x, (tuple, list)):
        for xi, yi in zip(x, y):
            assert np.allclose(xi, yi), f"Test {name} failed: {x}, {y}"
    else:
        assert np.allclose(x, y), f"Test {name} failed: {x}, {y}"
    

def align_np_torch_functions(np_funcs, torch_funcs):
    torch_keys = [SPECIAL_FUNC_NAME.get(_, _) for _ in torch_funcs.keys()]
    shared_funcs = sorted(set(np_funcs.keys()) & set(torch_keys))
    
    print("shared funcs", len(shared_funcs))
    np_funcs = {k: v for k, v in np_funcs.items() if k in shared_funcs}
    torch_funcs = {k: v for k, v in torch_funcs.items() if k in shared_funcs}
    # handled_torch_keys = ["input", "other", "dim", "keepdim", "alpha", "out", "layout", "end"]
    extra_np_keys = ["device", "requires_grad", "copy", "pin_memory", "memory_format"]
    ignored_np_keys = ["casting", "order", "where", "subok", "initial", "deg", "like", "signature", "subok", "extobj"] + extra_np_keys + IDENTITY + list(UNIFIED_API_NP.keys())
    ignore_torch_keys = ["alpha"] + IDENTITY + list(UNIFIED_API_TORCH.keys()) + list(UNIFIED_API_NP.values())
    
    skip_funcs = ["argsort"]
    ret = {}
    for i, name in enumerate(shared_funcs):
        sign, torch_params = torch_funcs[INVERSE_SPECIAL_FUNC_NAME.get(name, name)]
        sign, np_params = np_funcs[name]
        if name in skip_funcs:
            continue
        
        torch_args = [_[0] for _ in torch_params[0]]
        torch_kwargs = list(torch_params[1].keys())
        torch_keys = torch_args + torch_kwargs
        
        for key in extra_np_keys:
            if key in torch_keys:
                np_params[1][key] = "__None__"
        
        np_args = [_[0] for _ in np_params[0]]
        np_kwargs = list(np_params[1].keys())
        np_keys = np_args + np_kwargs
        
        # assert len(torch_args) == 0, f"{name}: {torch_args}"
        
        mapped_np_args = [UNIFIED_API_NP.get(_, _) for _ in np_args]
        mapped_np_kwargs = [UNIFIED_API_NP.get(_, _) for _ in np_kwargs]
        
        mapped_torch_args = [UNIFIED_API_TORCH.get(_, _) for _ in torch_args]
        mapped_torch_kwargs = [UNIFIED_API_TORCH.get(_, _) for _ in torch_kwargs]
        
        mapped_np_keys = mapped_np_args + mapped_np_kwargs
        mapped_torch_keys = mapped_torch_args + mapped_torch_kwargs
        shared_keys = [_ for _ in mapped_np_keys if _ in mapped_torch_keys]
        print(f"Function {i}/{len(shared_funcs)}:", name)
        print("numpy ", np_params)
        print("torch", torch_params)
        print("shared", shared_keys)
        
        for key in np_keys:
            if key not in ignored_np_keys:
                print("Unhandled np keys", key)
                exit(0)
            if "*" in key and key not in torch_keys and key.replace("*", "") in torch_keys:
                print("Unhandled np * keys", key)
                exit(0)
            
        
        for j, key in enumerate(torch_keys):
            if "*" in key:
                assert j == 0, "Only the first torch argument can be *"
            
            if key not in ignore_torch_keys:
                print("Unhandled torch keys", key)
                exit(0)
            if "*" in key and key not in np_keys and key.replace("*", "") in np_keys:
                print("Unhandled torch * keys", key)
                exit(0)
        
        np_name_mapping = {}
        torch_name_mapping = {}
        np_required_args = {}
        torch_required_args = {}
        default_value = {}
        
        for key in shared_keys:
            # np_key = params_torch_to_np[key]
            # unified_key = UNIFIED_API_NAME.get(np_key, np_key)
            np_key = np_name_mapping[key] = np_keys[mapped_np_keys.index(key)]
            torch_key = torch_name_mapping[key] = torch_keys[mapped_torch_keys.index(key)]
            
            if np_key in np_args:
                idx = np_args.index(np_key)
                np_value = np_params[0][idx][1]
                np_required_args[key] = idx
            else:
                np_value = np_params[1][np_key]
            if np_value is float:
                np_value = "np.float64"
            
            if torch_key in torch_args:
                idx = torch_args.index(torch_key)
                torch_value = torch_params[0][idx][1]
                torch_required_args[key] = idx
            else:
                torch_value = torch_params[1][torch_key]
            if key == "memory_format":
                torch_value = str(torch_value)
            
            if key == "dtype":
                np_value = torch_value = '__None__' # Use default dtype
                        
            if np_value != torch_value:
                if np_value == "__None__":
                    np_value = torch_value
                elif torch_value == "__None__":
                        torch_value = np_value
                else:
                    if key != "dtype":
                        print("Error", name, key, np_value, torch_value)
                        exit(0)
                # print(key, np_value, torch_value)
                # exit(0)
            default_value[key] = np_value
        print(np_name_mapping)
        print(torch_name_mapping)
        print(default_value)
        ret[name] = {"np_name": np_name_mapping, "torch_name": torch_name_mapping, "default_value": default_value, "np_required_args": np_required_args, "torch_required_args": torch_required_args}
        # if "arc" in name:
        check_function(ret, name)
        print("=====================================")
    
    print(f"#np funcs: {len(np_funcs)}, #torch funcs: {len(torch_funcs)}")
    
    dump(ret, __folder__ / "funcs.json", indent=2)
    # dump(np_funcs, __folder__ / "np_funcs.json", indent=2)

def test(*a):
    pass

# print(get_default_args(test))
# exit(0)

# np_funcs = get_module_functions(np)
print("Process torch functions")
torch_funcs = get_module_functions(torch)
print("Process numpy functions")
torch_keys = [SPECIAL_FUNC_NAME.get(_, _) for _ in torch_funcs.keys()]
np_funcs = get_module_functions(np, torch_keys)
# exit(0)

align_np_torch_functions(np_funcs, torch_funcs)



