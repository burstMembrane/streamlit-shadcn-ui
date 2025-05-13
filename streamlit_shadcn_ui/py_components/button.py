from typing import Literal

import streamlit as st

from streamlit_shadcn_ui.py_components.base.element import element, init_default_state
from streamlit_shadcn_ui.py_components.utils.callback import register_callback
from streamlit_shadcn_ui.py_components.utils.session import init_session

from .utils import declare_component

_component_func = declare_component("button")

# variant "default" | "destructive" | "outline" | "secondary" | "ghost" | "link"

variant_options = Literal[
    "default", "destructive", "outline", "secondary", "ghost", "link"
]


def button(
    text: str,
    variant: variant_options = "default",
    class_name: str = None,
    key=None,
    **kwargs,
) -> bool:
    """Create a button component with various style variants.

    Args:
        text (str): The text to display on the button
        variant (Literal["default", "destructive", "outline", "secondary", "ghost", "link"]):
            The button style variant. Defaults to "default".
        class_name (str, optional): Additional CSS class names to apply. Defaults to None.
        key (str, optional): Unique key for the component. Defaults to None.
        **kwargs: Additional props to pass to the button component

    Returns:
        bool: True if the button was clicked, False otherwise

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        # Basic button
        if ui.button("Click me"):
            st.write("Button clicked!")

        # Destructive button with custom class
        if ui.button("Delete", variant="destructive", class_name="my-button"):
            st.write("Delete action triggered")

        # Outline button with key
        if ui.button("Submit", variant="outline", key="submit_btn"):
            st.write("Form submitted")
        ```
    """
    props = {"text": text, "variant": variant, "className": class_name, **kwargs}
    default_state = init_default_state(key, default_value=False)
    non_resettable_state_key = f"{key}__non_resettable_state"
    init_session(key, default_state)
    init_session(non_resettable_state_key, default_value=default_state)

    if (
        st.session_state[non_resettable_state_key]["event_id"]
        != st.session_state[key]["event_id"]
    ):
        st.session_state[non_resettable_state_key]["value"] = st.session_state[key][
            "value"
        ]
        st.session_state[non_resettable_state_key]["event_id"] = st.session_state[key][
            "event_id"
        ]

    else:
        st.session_state[non_resettable_state_key]["value"] = False

    _component_func(comp="button", props=props, key=key, default=default_state)
    clicked = st.session_state[non_resettable_state_key]["value"]
    return clicked
