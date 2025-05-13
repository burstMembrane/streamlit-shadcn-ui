from typing import Optional

from .utils import declare_component

_component_func = declare_component("pagination")


def pagination(
    key: Optional[str] = None,
    total_pages: Optional[int] = 3,
    initial_page: Optional[int] = 1,
):
    """
    Create a pagination component.

    Args:
        key (str, optional): The key of the pagination component. Defaults to None.
        total_pages (int, optional): The total number of pages. Defaults to 3.
        initial_page (int, optional): The initial page number. Defaults to 1.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.pagination(key="pagination_1", total_pages=10, initial_page=1)
    ```

    ### Basic Usage

    ```python
    import streamlit as st
    import streamlit_shadcn_ui as ui

    page_value = ui.pagination(key="pagination1", total_pages=10, initial_page=1)

    st.write(page_value)
    ```
    """
    props = {"totalPages": total_pages, "initialPage": initial_page}
    component_value = _component_func(comp="pagination", props=props, key=key)
    return component_value
