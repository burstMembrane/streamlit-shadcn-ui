from typing import Optional

from .utils import declare_component

_component_func = declare_component("calendar")


def calendar(class_name: Optional[str] = None, key: Optional[str] = None):
    """
    Create a calendar component.
    Args:
        class_name (str, optional): The class name of the calendar. Defaults to None.
        key (str, optional): The key of the calendar. Defaults to None.
    """
    props = {
        "className": class_name,
    }
    component_value = _component_func(comp="calendar", props=props, key=key)
    return component_value
