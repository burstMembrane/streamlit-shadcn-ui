from typing import Optional

from .utils import declare_component

_component_func = declare_component("textarea")


def textarea(
    default_value: Optional[str] = "",
    placeholder: Optional[str] = "",
    key: Optional[str] = None,
    class_name: Optional[str] = None,
    **kwargs,
):
    """
    Create a textarea component.

    Args:
        default_value (str, optional): The default value of the textarea. Defaults to "".
        placeholder (str, optional): The placeholder of the textarea. Defaults to None.
        key (str, optional): The key of the textarea. Defaults to None.
        class_name (str, optional): The class name of the textarea. Defaults to None.
        **kwargs: Additional keyword arguments to pass to the textarea component.

    Examples:
    ```python
    import streamlit as st
    import streamlit_shadcn_ui as ui

    # Textarea Component
    textarea_value = ui.textarea(default_value="Type your message here...", placeholder="Enter longer text", key="textarea1")
    st.write("Textarea Value:", textarea_value)
    ```

    """
    props = {
        "defaultValue": default_value,
        "placeholder": placeholder,
        "className": class_name,
        **kwargs,
    }
    component_value = _component_func(
        comp="textarea", props=props, key=key, default=default_value
    )
    return component_value
