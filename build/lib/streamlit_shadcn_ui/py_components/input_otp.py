from typing import Optional

from .utils import declare_component

_component_func = declare_component("input_otp")


def input_otp(
    default_value: Optional[str] = None,
    max_length: Optional[int] = 6,
    key: Optional[str] = None,
):
    """
    Create an input OTP component for inputting a one-time password.

    Args:
        default_value (str, optional): The default value of the input OTP. Defaults to ''.
        max_length (int, optional): The maximum length of the input OTP. Defaults to 6.
        key (str, optional): The key of the input OTP. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.input_otp(default_value='', max_length=6, key="input_otp_1")
    ```
    """
    props = {
        "defaultValue": default_value,
        "maxLength": max_length,
    }

    component_value = _component_func(
        comp="input_otp",
        props=props,
        key=key,
        default=default_value,
    )
    return component_value
