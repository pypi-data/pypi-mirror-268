# -*- coding: utf-8 -*-
import inspect

from typing import Any, Iterable, List, Optional, Type, Union


def get_slots(
    slotted_obj: Union[Type[Any], Any],
    ignored: Optional[Iterable]=None
) -> List[str]:
    """
    Simple recursive logic that will traverse a (slotted) object's inheritance
    graph to retrieve a complete set of slotted attributes.
    """
    slots = set(slotted_obj.__slots__)  # type: ignore

    slotted_cls = slotted_obj \
        if inspect.isclass(slotted_obj) \
        else slotted_obj.__class__

    for base_cls in slotted_cls.__bases__:
        if hasattr(base_cls, "__slots__"):
            slots.update(get_slots(base_cls))

    return list(slots) if ignored is None \
        else [i for i in slots if i not in ignored]

