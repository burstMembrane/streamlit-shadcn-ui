from typing import List, Optional

from .utils import declare_component

_component_func = declare_component("toggle_group")


def toggle_group(
    default_values: Optional[List[str]] = None,
    key: Optional[str] = None,
):
    """
    Create a toggle group component.

    Args:
        default_values (List[str], optional): The default values of the toggle group. Defaults to None.
        key (str, optional): The key of the toggle group. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.toggle_group(default_values=["Option 1", "Option 2", "Option 3"], key="toggle_group_1")
    ```
    """
    if default_values is None:
        default_values = []

    props = {
        "defaultValues": default_values,
    }

    component_value = _component_func(
        comp="toggle_group", props=props, key=key, default=default_values
    )

    return component_value
