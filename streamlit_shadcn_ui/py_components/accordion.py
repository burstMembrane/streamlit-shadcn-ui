from typing import Dict, List, Literal

from .utils import declare_component

_component_func = declare_component("accordion")
accordion_item_options = Literal["trigger", "content"]


def accordion(
    data: List[Dict[accordion_item_options, str]] = None,
    class_name: str = None,
    key: str = None,
):
    """
    Create an accordion component with a list of items.
    Args:
        data (List[Dict[str, str]]): The list of items to display in the accordion.
        class_name (str, optional): The class name of the accordion. Defaults to None.
        key (str, optional): The key of the accordion. Defaults to None.

    Examples:
        ```python

        data = [
            {
                "trigger": "Is it accessible?",
                "content": "Yes. It adheres to the WAI-ARIA design pattern.",
            },
            {
                "trigger": "Is it styled?",
                "content": "Yes. It comes with default styles that match the other components' aesthetic.",
            },
            {
                "trigger": "Is it animated?",
                "content": "Yes. It's animated by default, but you can disable it if you prefer.",
            },
        ]
        import streamlit_shadcn_ui as ui
        ui.accordion(data=data)
        ```
    """
    props = {
        "data": data,
        "className": class_name,
    }
    component_value = _component_func(comp="accordion", props=props, key=key)
    return component_value
