from typing import Any, Dict, List, Optional

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from streamlit_shadcn_ui.py_components.utils.session import init_session

from .utils import declare_component

_component_func = declare_component("dialog")


def dialog_layer(props, open_status=False, key=None):
    container = stylable_container(
        key=f"dialog_layer_{key}",
        css_styles=f"""
        {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 999992;
            background-color: rgba(255,255,255,0.8);
            backdrop-filter: blur(4px);
            display: {"flex" if open_status else "none"};
            justify-content: center;
            align-items: center;
        }}
        """,
    )
    with container:
        component_value = _component_func(
            comp="dialog", props=props, key=key, default=None
        )
        return component_value


def dialog(
    show: Optional[bool] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    fields: Optional[List[Dict[str, Any]]] = None,
    key: Optional[str] = None,
):
    """
    Create a dialog component.

    Args:
        show (bool, optional): Whether to show the dialog. Defaults to None.
        title (str, optional): The title of the dialog. Defaults to None.
        description (str, optional): The description of the dialog. Defaults to None.
        fields (List[Dict[str, Any]], optional): The fields of the dialog. Defaults to None.
        key (Optional[str], optional): The key of the dialog. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    fields = [
        {"id": "name", "label": "Name", "defaultValue": "John Doe"},
        {"id": "username", "label": "Username", "defaultValue": "@johndoe"},
    ]
    trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
    result = ui.dialog(
        show=trigger_btn,
        title="Edit profile",
        description="Make changes to your profile here. Click save when you're done.",
        fields=fields,
        key="dialog1",
    )
    ```
    """
    props = {"title": title, "description": description, "fields": fields}
    init_session(key=key, default_value={"open": False, "confirm": False})
    if show:
        st.session_state[key]["open"] = True
    component_state = dialog_layer(
        props=props, key=key, open_status=st.session_state[key]["open"]
    )

    return component_state
