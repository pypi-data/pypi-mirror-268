"""
Try to load a SoftIOC object from an SoftIOC IOC script

The script has to have some function that can be called to produce a SoftIOC

The function parses command line arguments and passes any args after '--' to the ioc build function
"""
import sys
from argparse import ArgumentParser, Namespace
from typing import TYPE_CHECKING, Optional, List
from importlib.util import spec_from_file_location, module_from_spec
import os.path as path
from inspect import signature

if TYPE_CHECKING:
    from .soft_ioc import SoftIOC

def load_ioc_commandline(parser: Optional[ArgumentParser]=None,
                         commandline_args: Optional[List[str]]=None) -> "SoftIOC":
    """
    :param parser: if None, create new parser
    :param commandline_args: if None, use sys.argv.  A zeroeth value is added automatically when not None.
    :return:
    """
    if parser is None:
        _parser = ArgumentParser()
    else:
        _parser = parser

    if commandline_args is None:
        cmd_args = sys.argv[:]
    else:
        cmd_args = [None] + commandline_args

    _parser = ArgumentParser()
    _parser.add_argument("ioc_path", help="a path to an IOC module that uses SoftIOC")
    _parser.add_argument("build_function", nargs='?', default="build_ioc",
                        help="call <ioc_name>.<build_function> to build the IOC")


    try:
        i = cmd_args.index('--')
        left = cmd_args[1:i]
        right = cmd_args[i+1:]
    except ValueError:
        left = cmd_args[1:]
        right = []

    args = _parser.parse_args(left)

    return load_ioc(args.ioc_path, args.build_function, right)


def load_ioc(mod_fname: str, func_name: str, args: List[str]) -> "SoftIOC":
    if not path.exists(mod_fname):
        raise ModuleNotFoundError(f"{mod_fname} doesn't exist")
    ioc_spec = spec_from_file_location("ioc", mod_fname)
    if ioc_spec is None:
        raise ModuleNotFoundError(f"Couldn't load a module from {mod_fname}.")
    ioc_mod = module_from_spec(ioc_spec)
    if ioc_mod.__loader__ is not None:
        ioc_mod.__loader__.exec_module(ioc_mod)
    else:
        raise ModuleNotFoundError(f"importing {mod_fname} created an empty loader")

    try:
        build_func = getattr(ioc_mod, func_name)
    except AttributeError:
        raise AttributeError(f"Could not find an ioc build function named {func_name} in {mod_fname}.")

    # build argument list
    params = signature(build_func).parameters

    arg_list = []
    for i in range(len(args)):
        arg = args[i]
        value = arg
        if i < len(params):
            param = list(params.values())[i]
            if param.kind in [param.POSITIONAL_OR_KEYWORD, param.POSITIONAL_ONLY]:
                try:
                    value = param.annotation(value)
                except ValueError as e:
                    raise ValueError(f"Couldn't coerce type for argument '{param.name}' in {func_name}: {str(e)}")
                except TypeError:
                    pass
        arg_list.append(value)

    try:
        return build_func(*arg_list)
    except TypeError as e:
        if len(arg_list) == 0:
            raise TypeError(str(e) + f".  Add ' -- ' followed by function argument(s) to the command line.")
        else:
            raise e
