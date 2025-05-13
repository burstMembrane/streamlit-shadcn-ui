from typing import Literal, Optional

from .utils import declare_component

_component_func = declare_component("toggle")


# TODO: invesigate the different icon types availble, for now just setitng to bold, italic and undeling
def toggle(
    default_checked: Optional[bool] = False,
    icon: Optional[Literal["bold", "italic", "underline"]] = "bold",
    key: Optional[str] = None,
):
    """
    Create a toggle component.

    Args:
        default_checked (bool, optional): Whether the toggle is checked by default. Defaults to False.
        icon (str, optional): The icon of the toggle. Defaults to "bold".

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.toggle(default_checked=True, icon="bold", key="toggle_1")
    ```
    """
    props = {
        "defaultChecked": default_checked,
        "icon": icon,
    }
    component_value = _component_func(
        comp="toggle", props=props, key=key, default=default_checked
    )
    return component_value
