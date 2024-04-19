# -*- coding: utf-8 -*-
import pkgutil
import importlib
import inspect

from types import ModuleType
from typing import Any, List, Type


def import_object(obj_path: str) -> Type[Any]:
    """
    Helper function for importing a single object from another module.

    :obj_path: String
        Full path to the object (e.g. "coppyr.errors.CoppyrError").
    :return: Object
        The imported object.
    """
    path_parts = obj_path.split(".")
    module_name, obj_name = ".".join(path_parts[:-1]), path_parts[0]
    module = import_module(module_name)
    return getattr(module, obj_name)


def import_module(mod_path: str) -> ModuleType:
    """
    Just a local wrapper for `importlib.import_module`

    :mod_path: String
        Full path to the module (e.g. "piston.errors").
    :return: Module
    """
    return importlib.import_module(mod_path)


def import_subclasses(
    module, baseclass: Type[Any],
    recursive: bool=False,
    include_base: bool=False
) -> List[ModuleType]:
    """
    Function to import all classes from a module that are subclasses of a
    desired class.

    This is useful when designing an extension system where extension objects
    inherit from a common base.  This function allows dynamic loading by the
    runtime rather than imperative registration of extensions.

    :module: String/Module
        Target module either qualfied string name or an already imported module
        object.
    :baseclass: Class
        Class definition to use as a a base class.
    :recursive: Boolean
        Whether or not to check and load from all sub-modules.
    :include_base: Boolean
        Whether or not to include instances of the baseclass itself in the
        result.
    """
    results = []

    module = import_module(module) if isinstance(module, str) else module
    prefix = module.__name__ + "."  # "piston.errors."

    for _, name, ispkg in pkgutil.iter_modules(module.__path__):
        location = prefix + name

        if ispkg:
            # if it is another module...
            if recursive:
                # ...and recursive is enabled, then recurse
                results += import_subclasses(
                    name,
                    baseclass=baseclass,
                    recursive=recursive,
                    include_base=include_base
                )
        else:
            # load the module (python file)
            module = import_module(location)

            # Walk the objects in the module
            for obj in module.__dict__.values():
                # If it is a class definition
                if inspect.isclass(obj):
                    # If it is a subclass of the baseclass
                    if issubclass(obj, baseclass):
                        # If we are supposed to ignore base and this obj has
                        # the same __name__, ignore it.
                        if not include_base \
                                and obj.__name__ == baseclass.__name__:
                            continue

                        # otherwise add the found class defintion
                        results.append(obj)

    return results
