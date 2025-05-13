from typing import List, Literal, Optional

from .utils import declare_component

_component_func = declare_component("checkbox")

checkbox_mode = Literal["single", "multiple"]

checkbox_option = Literal["label", "id", "default_checked"]


def checkbox(
    mode: Optional[checkbox_mode] = None,
    options: Optional[List[checkbox_option]] = None,
    key: Optional[str] = None,
):
    """
    Create a checkbox component.
    Args:
        mode (str, optional): The mode of the checkbox. Defaults to None.
        options (List[str], optional): The options of the checkbox. Defaults to None.
        key (str, optional): The key of the checkbox. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.checkbox(mode="single", options=["Option A", "Option B", "Option C"], key="cb1")
        ```
    """
    props = {"options": options, "mode": mode}
    component_value = _component_func(comp="checkbox", props=props, key=key)
    return component_value
