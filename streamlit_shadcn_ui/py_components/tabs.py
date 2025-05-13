from typing import List, Optional

from .utils import declare_component

_component_func = declare_component("tabs")


def tabs(
    options: List[str],
    default_value: Optional[str] = None,
    key: Optional[str] = None,
    class_name: Optional[str] = None,
    **kwargs,
):
    """
    Create a tabs component.

    Args:
        options (List[str]): The options to display in the tabs.
        default_value (Optional[str], optional): The default value of the tabs. Defaults to None.
        key (Optional[str], optional): The key of the tabs. Defaults to None.
        class_name (Optional[str], optional): The tailwind class name of the tabs. Defaults to None.
        **kwargs: Additional keyword arguments to pass to the tabs component.


    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    value = ui.tabs(
        options=["PyGWalker", "Graphic Walker", "GWalkR", "RATH"],
        default_value="PyGWalker",
        key="kanaries",
    )
    ```
    """
    option_list = list(options)
    props = {
        "options": option_list,
        "defaultValue": default_value,
        "className": class_name,
        **kwargs,
    }
    component_value = _component_func(
        comp="tabs", props=props, key=key, default=default_value
    )
    return component_value
