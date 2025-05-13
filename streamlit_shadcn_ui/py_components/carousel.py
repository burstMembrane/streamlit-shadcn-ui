from typing import List, Optional

from .utils import declare_component

_component_func = declare_component("carousel")


# TODO: update with images?
def carousel(
    content: Optional[List[str]] = None,
    class_name: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a carousel component.
    Args:
        content (List[str], optional): The content of the carousel. Defaults to None.
        class_name (str, optional): The class name of the carousel. Defaults to None.
        key (str, optional): The key of the carousel. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.carousel(content=["1", "2", "3"], class_name=None, key=None)
        ```
    """
    props = {
        "content": content or [],
        "className": class_name,
        "length": len(content),
    }
    component_value = _component_func(comp="carousel", props=props, key=key)
    return component_value
