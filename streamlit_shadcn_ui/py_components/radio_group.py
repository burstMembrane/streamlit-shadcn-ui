from typing import Dict, List, Literal, Optional

from .utils import declare_component

_component_func = declare_component("radio_group")


def radio_group(
    options: List[Dict[Literal["label", "value", "id"], str]],
    default_value: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a radio group component.

    Args:
        options (List[Dict[Literal["label", "value", "id"], str]]): The options for the radio group.
        default_value (str, optional): The default value of the radio group. Defaults to None.
        key (str, optional): The key of the radio group. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.radio_group(options=["Option 1", "Option 2", "Option 3"], default_value="Option 1", key="radio_group_1")
    ```

    ```python
    radio_options = [
    {"label": "Option A", "value": "A", "id": "r1"},
    {"label": "Option B", "value": "B", "id": "r2"},
    {"label": "Option C", "value": "C", "id": "r3"},
    {"label": "Option D", "value": "D", "id": "r4"},
    ]
    radio_value = ui.radio_group(options=radio_options, default_value="B", key="radio1")
    ```
    """
    props = {"defaultValue": default_value, "options": options}
    component_value = _component_func(
        comp="radio_group", props=props, key=key, default=default_value
    )
    return component_value
