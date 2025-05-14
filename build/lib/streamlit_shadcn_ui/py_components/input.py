from typing import Literal, Optional

from .utils import declare_component

_component_func = declare_component("input")


def input(
    default_value: Optional[str] = None,
    type: Optional[
        Literal["text", "number", "email", "password", "search", "tel", "url"]
    ] = "text",
    placeholder: Optional[str] = None,
    key: Optional[str] = None,
    className: Optional[str] = None,
):
    """
        Create an input component.

    Args:
        default_value (str, optional): The default value of the input. Defaults to None.
        type (str, optional): The type of the input e.g "text", "number", "email", "password". Defaults to "text".
        placeholder (str, optional): The placeholder string of the input. Defaults to None.
        key (str, optional): The key of the input. Defaults to None.
        className (str, optional): The tailwind css class name of the input. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    # Input Component
    input_value = ui.input(default_value="Hello, Streamlit!", type='text', placeholder="Enter text here", key="input1")
    ```


    """
    props = {
        "defaultValue": default_value,
        "type": type,
        "placeholder": placeholder,
        "className": className,
    }
    component_value = _component_func(
        comp="input", props=props, key=key, default=default_value
    )
    return component_value
