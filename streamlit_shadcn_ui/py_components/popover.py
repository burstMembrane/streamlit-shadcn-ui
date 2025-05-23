from typing import Optional

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from .utils import declare_component, init_session


def popover_trigger(value=None, open_status=False, key=None):
    component_name = "popover_trigger"
    _component_func = declare_component(component_name)
    props = {"value": value, "open": open_status}
    return _component_func(
        comp=component_name,
        props=props,
        key=key,
        default={"x": 0, "y": 0, "open": False},
    )


def popover_content(
    x,
    y,
    content,
    open_status=False,
    key=None,
):
    component_name = "popover_content"
    _component_func = declare_component(component_name)
    container = stylable_container(
        key=f"cont_{key}",
        css_styles=f"""
        {{
            position: absolute;
            bottom: {y}px;
            left: {x}px;
            display: {"block" if open_status else "none"};
            z-index: 1000;
        }}
        """,
    )
    with container:
        props = {"content": content, "open": open_status}
        result = _component_func(
            comp=component_name, props=props, key=key, default={"open": False}
        )
        return result


def popover(
    label: Optional[str] = "Open",
    content: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a popover component.

    Args:
        label (str, optional): The label of the popover. Defaults to "Open".
        content (str, optional): The content of the popover. Defaults to None.
        key (str, optional): The key of the popover. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.popover(key="popover1", label="popover", content="Place content for the popover here.")

    ```
    """
    trigger_key = f"trigger_{key}"
    content_key = f"content_{key}"
    # Initialize session state
    init_session(key=trigger_key, default_value={"x": 0, "y": 0, "open": False})
    init_session(key=content_key, default_value={"open": False})

    open_status = st.session_state[trigger_key]["open"]

    with stylable_container(
        key=f"root_{key}",
        css_styles="""
        {
            position: relative;
        }
        """,
    ):
        # Render the trigger component
        trigger_state = popover_trigger(
            value=label, key=trigger_key, open_status=open_status
        )
        content_state = popover_content(
            x=trigger_state["x"],
            y=trigger_state["y"],
            content=content,
            open_status=trigger_state["open"],
            key=content_key,
        )
        return content_state
