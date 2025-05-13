from typing import Optional

from .utils import declare_component

_component_func = declare_component("progress")


def progress(
    value: Optional[int] = 0,
    class_name: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a progress component.

    Args:
        value (int, optional): The value of the progress component. Defaults to 0.
        class_name (str, optional): The class name of the progress component. Defaults to None.
        key (str, optional): The key of the progress component. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.progress(value=50, class_name="progress-bar", key="progress_1")
    ```

    You can also just pass a bare int to the component, and it will increment by 1 each time the component is rendered.
    ```python
    import streamlit_shadcn_ui as ui
    for i in range(0, 100, 25):
        ui.progress(i)
    ```
    """
    props = {
        "data": value,
        "className": class_name,
    }
    component_value = _component_func(comp="progress", props=props, key=key)
    return component_value
