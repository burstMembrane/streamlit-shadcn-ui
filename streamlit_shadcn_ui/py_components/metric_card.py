from typing import Optional

from streamlit_shadcn_ui.py_components.base.element import element
from streamlit_shadcn_ui.py_components.utils.declare import declare_component

component_func = declare_component("card")


# TODO; make content able to be an element
def metric_card(
    title: Optional[str] = None,
    content: Optional[str] = None,
    description: Optional[str] = None,
    key=None,
):
    """
    Create a metric card component for displaying metrics.

    Args:
        title (str, optional): The title of the metric card. Defaults to None.
        content (str, optional): The content of the metric card. Defaults to None.
        description (str, optional): The description of the metric card. Defaults to None.
        key (str, optional): The key of the metric card. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.metric_card(title="Metric Card", content="100", description="100", key="metric_card_1")
    ```

    ```python
    import streamlit as st
    import streamlit_shadcn_ui as ui
    cols = st.columns(3)

    with cols[0]:
    ui.metric_card(
        title="Total Revenue",
        content="$45,231.89",
        description="+20.1% from last month",
        key="card1",
    )
    with cols[1]:
        ui.metric_card(
            title="Total Revenue",
            content="$45,231.89",
            description="+20.1% from last month",
            key="card2",
        )
    with cols[2]:
        ui.metric_card(
            title="Total Revenue",
            content="$45,231.89",
            description="+20.1% from last month",
            key="card3",
        )
    ```
    """
    props = {
        "title": title,
        "content": content,
        "description": description,
    }
    return component_func(comp="card", key=key, props=props)
