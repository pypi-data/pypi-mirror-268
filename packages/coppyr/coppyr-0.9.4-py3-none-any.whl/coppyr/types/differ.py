# -*- coding: utf-8 -*-
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

from coppyr.types import slot


def getattrs(obj: Any) -> List[str]:
    if hasattr(obj, "__slots__"):
        return slot.get_slots(obj)
    else:
        return list(obj.__dict__.keys())


def _diff_tuple(
    left: Any,
    right: Any,
    invert: bool=False
) -> Union[Tuple[Any, Any], None]:
    """
    Basic, atomic diff unit that returns a common tuple format.

    :param left: Any
        Left value
    :param right: Any
        Right value
    :param invert: Boolean
        Whether or not to reverse the left and right treatment of the passed
        values.  This is a convenience parameter so that actual diff logic can
        have consistent handling of tuple construction independent of desired
        orientation.
    :return: Tuple/sub-diff
    """
    if left == right:
        return None
    else:
        return (left, right) if not invert else (right, left)


def _diff_none(
    obj: Any,
    attrs: Optional[Iterable[str]]=None,
    invert: bool=False
) -> Dict[str, Tuple[Any, Any]]:
    """
    If an object is being diffed with `None` then the object is entirely "new"
    so we should return a complete diff of all targeted attributes.
    """
    result = {}

    attrs = attrs if attrs is not None else getattrs(obj)

    for attr in attrs:  # type: ignore
        obj_attr = getattr(obj, attr)
        if isinstance(obj_attr, (list, tuple)):
            result[attr] = [
                _diff_tuple(x, None, invert=invert) for x in obj_attr
            ]
        else:
            result[attr] = _diff_tuple(obj_attr, None, invert=invert)

    return result


def diff(
    left_obj: Any,
    right_obj: Any,
    attrs: Optional[Iterable[str]]=None,
    invert: bool=False
) -> Dict[str, Tuple[Any, Any]]:
    """
    Diff two objects and get a diff structure back which shows left vs. right
    changes.  From this object you can see what things are different, what
    things are added, and what things were removed.

    :param left_obj: Any
    :param right_obj: Any
    :param attrs: Iterable of Strings
        Attribute names of the objects to include in the diff.  Will default to
        __dict__ and/or __slots__ keys.
    :param invert: Boolean
        Whether or not reverse the diff direction.
    :return: Dict[str, Any]
        Attribute map to diff tuples.
    """
    # re-orient
    if invert:
        left_obj, right_obj = right_obj, left_obj
        invert = False

    # If attrs is not explicitly specified, infer them by getting the superset
    # of both object attributes
    if attrs is None:
        attrs = set(getattrs(left_obj))
        attrs = list(attrs.union(getattrs(right_obj)))

    # `None` is a special case, so handle it first
    if left_obj is None and right_obj is None:
        return {}
    if right_obj is None:
        return _diff_none(left_obj, attrs)
    if left_obj is None:
        return _diff_none(right_obj, attrs, invert=True)

    # Check that object types match
    if not issubclass(right_obj.__class__, left_obj.__class__) \
            or left_obj.__class__.__name__ != right_obj.__class__.__name__:
        raise ValueError('Object type mismatch')

    # start diff
    result = {}

    for attr in attrs:
        left = getattr(left_obj, attr)
        right = getattr(right_obj, attr)

        # if they are equal, no diff to show
        if left == right:
            continue
        else:
            result[attr] = _diff_tuple(left, right, invert=invert)

    return result
