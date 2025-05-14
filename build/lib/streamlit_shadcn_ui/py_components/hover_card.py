from typing import Optional

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from .utils import declare_component, init_session


def hover_card_trigger(label=None, open_status=False, key=None):
    name = "hover_card_trigger"
    _component_func = declare_component(name)
    props = {"label": label, "open": open_status}
    return _component_func(
        comp=name, props=props, key=key, default={"x": 0, "y": 0, "open": False}
    )


def hover_card_content(
    x, y, content: str, content_type: str, open_status=False, key=None
):
    name = "hover_card_content"
    _component_func = declare_component(name)
    container = stylable_container(
        key=f"cont_{key}",
        css_styles=f"""
        {{
            position: absolute;
            top: {y}px;
            left: {x}px;
            display: {"block" if open_status else "none"};
            z-index: 1000;
        }}
        """,
    )
    with container:
        props = {"content": content, "contentType": content_type, "open": open_status}
        result = _component_func(
            comp=name, props=props, key=key, default={"open": False}
        )
        return result


# TODO: make this accept other elements other than text
def hover_card(
    label: Optional[str] = None,
    content: Optional[str] = None,
    content_type: Optional[str] = "text",
    key: Optional[str] = "ui_card",
):
    """
    Create a hover card component.

    Args:
        label (str): The label of the hover card.
        content (str): The content of the hover card.
        content_type (str, optional): The type of the content. Defaults to "text".
        key (str, optional): The key of the hover card. Defaults to "ui_card".

    Examples:
    ```python
    import streamlit_shadcn_ui as ui

    ui.hover_card(
        label="Hover on me1!",
        content="I am a hover card1!",
        content_type="text",
        key="hover_card_1",
    )

    ```
    """
    trigger_component_key = f"trigger_{key}"
    content_component_key = f"content_{key}"

    init_session(
        key=trigger_component_key, default_value={"x": 0, "y": 0, "open": False}
    )
    init_session(key=content_component_key, default_value={"open": False})
    open_status = st.session_state[trigger_component_key]["open"]
    with stylable_container(
        key=f"root_{key}",
        css_styles="""
        {
            position: relative;
        }
        """,
    ):
        trigger_state = hover_card_trigger(
            label=label, open_status=open_status, key=trigger_component_key
        )

        options_state = hover_card_content(
            x=trigger_state["x"],
            y=trigger_state["y"],
            content=content,
            content_type=content_type,
            open_status=trigger_state["open"],
            key=content_component_key,
        )

        return None
