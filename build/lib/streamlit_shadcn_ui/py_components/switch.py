from typing import Optional

from .utils import declare_component

_component_func = declare_component("switch")


def switch(
    default_checked: Optional[bool] = False,
    label: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a switch component.
    Args:
        default_checked (bool, optional): Whether the switch is checked by default. Defaults to False.
        label (str, optional): The label of the switch. Defaults to None.
        key (str, optional): The key of the switch. Defaults to None.
    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.switch(default_checked=True, label="Switch", key="switch1")
    ```
    """
    props = {"defaultChecked": default_checked, "label": label}
    component_value = _component_func(
        comp="switch", props=props, key=key, default=default_checked
    )
    return component_value
