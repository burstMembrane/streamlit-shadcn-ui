from typing import Dict, List, Literal, Optional

from .utils import declare_component

_component_func = declare_component("breadcrumb")

# define a type for the items
breadcrumb_item_options = Literal["text", "href", "isCurrentPage"]


def breadcrumb(
    breadcrumb_items: List[Dict[breadcrumb_item_options, Optional[str]]],
    class_name: Optional[str] = None,
    key=None,
):
    """
    Create a breadcrumb component with a list of breadcrumb items.
    Args:
        breadcrumb_items (List[Dict[str, Optional[str]]]): The list of breadcrumb items.
        class_name (str, optional): The class name of the breadcrumb. Defaults to None.
        key (str, optional): The key of the breadcrumb. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.breadcrumb(breadcrumb_items=[{"text": "Home", "href": "/home"}])
        ```
    """
    items = [
        {
            "text": item["text"],
            "href": item.get("href"),
            "isCurrentPage": item.get("isCurrentPage", False),
        }
        for item in breadcrumb_items
    ]
    props = {
        "items": items,
        "className": class_name,
    }
    component_value = _component_func(
        comp="breadcrumb", props=props, key=key, default=None
    )
    return component_value
