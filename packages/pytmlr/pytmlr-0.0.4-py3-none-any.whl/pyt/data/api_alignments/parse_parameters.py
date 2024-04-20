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


def get_all_functions(module, required_names=None):
    functions = []
    for name in dir(module):
        if name in ["array", "Tensor", "tensor", "load", "save", "candidate", "wait", "obj", "arange"]:
            continue
        if "copy" in name and name != "copy":
            continue
        if name.startswith("_") or name.endswith("_"):
            continue
        if "Warning" in name or "Error" in name:
            continue
        if name.lower() != name:
            continue
        if name.startswith("set_") or name.startswith("get_") or name.startswith("is_") or "autocast" in name:
            continue
        if required_names is not None and name not in required_names:
            continue
        if not callable(getattr(module, name)):
            continue
        if inspect.isclass(getattr(module, name)):
            continue
        functions.append(name)
    
    return functions


def parse_module_functions(module=np, required_names=None):
    functions = get_all_functions(module, required_names=required_names)
    print("Total functions", len(functions))
    
    func_args = {}
    func_infos = {}
    
    for i, name in enumerate(functions):
        print(f"Process {i}-th function", name)
        func = getattr(module, name)
        doc_str = func.__doc__
        if doc_str is not None:
            doc_str = doc_str.strip()
            
            if "is deprecated" in doc_str:
                continue
        try:
            arguments = get_default_args(func)
            func_args[name] = arguments
            func_infos[name] = {"arguments": arguments, "from_doc_str": False}
        except Exception as e:
            if doc_str is not None:
                func_args[name] = get_default_args_from_doc(doc_str, name, is_np=module is np)
                func_infos[name] = {"arguments": arguments, "from_doc_str": True, "doc_str": doc_str}
    return func_args, func_infos


if __name__ == '__main__':
    print("Process torch functions")
    torch_functions, torch_func_infos = parse_module_functions(torch)
    dump(torch_functions, "torch_functions.json", indent=4)
    
    print("Process numpy functions")
    SPECIAL_FUNC_NAME = {
        "repeat": "tile",
        "repeat_interleave": "repeat",
    }
    torch_keys = [SPECIAL_FUNC_NAME.get(_, _) for _ in torch_functions.keys()]
    np_functions = parse_module_functions(np, torch_keys)
    dump(torch_functions, "numpy_functions.json", indent=4)
