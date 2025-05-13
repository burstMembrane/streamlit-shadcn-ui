from typing import Dict, List, Literal, Optional

from .utils import declare_component

_component_func = declare_component("resizable")


def resizable(
    panels: Optional[List[Dict[Literal["content", "defaultSize"], int]]] = None,
    direction: Optional[Literal["horizontal", "vertical"]] = "horizontal",
    key: Optional[str] = None,
):
    """
    Create a resizable component.

    Args:
        panels (List[Dict[Literal["content", "defaultSize"], int]], optional): The panels to display in the resizable component. Defaults to None.
        direction (Literal["horizontal", "vertical"], optional): The direction of the resizable component. Defaults to "horizontal".
        key (str, optional): The key of the resizable component. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    panels=[
    { "content": "One", "defaultSize": 50 },
    { "content": "Two", "defaultSize": 25 },
    { "content": "Three", "defaultSize": 25 },
    ]
    ui.resizable(key="resizable1", direction="horizontal",panels=panels)
    ```
    """
    props = {"panels": panels, "direction": direction}
    component_value = _component_func(comp="resizable", props=props, key=key)
    return component_value
