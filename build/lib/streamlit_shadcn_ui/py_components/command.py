from typing import List, Optional

from .utils import declare_component

_component_func = declare_component("command")


def command(
    class_name: Optional[str] = None,
    items: Optional[List[str]] = None,
    title: Optional[str] = None,
    key: Optional[str] = None,
):
    """
        Create a command component.
        Args:
            class_name (str, optional): The class name of the command component. Defaults to None.
            items (list, optional): The items of the command component. Defaults to None.
            title (str, optional): The title of the command component. Defaults to None.
            key (str, optional): The key of the command component. Defaults to None.

        Examples:
        ```python
    import streamlit as st
    import streamlit_shadcn_ui as ui

    items = [
        {"label": "Calendar"},
        {"label": "Search Emoji"},
        {"label": "Calculator"},
    ]
    value = ui.command(items=items, key="command1", title="Suggestions")
    ```
    """
    props = {"className": class_name, "items": items, "title": title}
    component_value = _component_func(comp="command", props=props, key=key)
    return component_value
