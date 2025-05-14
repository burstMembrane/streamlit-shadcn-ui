from typing import List, Optional

from .utils import declare_component

_component_func = declare_component("scroll_area")


def scroll_area(
    title: Optional[str] = None,
    tags: Optional[List[str]] = None,
    class_name: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a scroll area component.

    Args:
        title (str, optional): The title of the scroll area. Defaults to None.
        tags (List[str], optional): The tags to display in the scroll area. Defaults to None.
        class_name (str, optional): The tailwind class name of the scroll area. Defaults to None.
        key (str, optional): The key of the scroll area. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.scroll_area(title="Tags", tags=tags, key="scroll_area-1")
    ```

    ```python
    import streamlit_shadcn_ui as ui
    tags = [f"v1.2.0-beta.{50 - i}" for i in range(50)]
    ui.scroll_area(title="Tags", tags=tags, key="scroll_area-1")
    ```
    """
    props = {
        "title": title,
        "tags": tags,
        "className": class_name,
    }
    component_value = _component_func(comp="scroll_area", props=props, key=key)
    return component_value
