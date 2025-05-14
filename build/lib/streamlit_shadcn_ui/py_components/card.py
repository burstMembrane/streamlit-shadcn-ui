from typing import Optional

from streamlit_shadcn_ui.py_components.base.element import element


def card(
    title: Optional[str] = None,
    content: Optional[str] = None,
    description: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a card component.
    Args:
        title (str, optional): The title of the card. Defaults to None.
        content (str, optional): The content of the card. Defaults to None.
        description (str, optional): The description of the card. Defaults to None.
        key (str, optional): The key of the card. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui

        with ui.card(key="card1"):
            ui.element("span", children=["Email"], className="text-gray-400 text-sm font-medium m-1", key="label1")
            ui.element("input", key="email_input", placeholder="Your email")

            ui.element("span", children=["User Name"], className="text-gray-400 text-sm font-medium m-1", key="label2")
            ui.element("input", key="username_input", placeholder="Create a User Name")
            ui.element("button", text="Submit", key="button", className="m-1")
        ```
    """
    return element(
        name="card", key=key, title=title, content=content, description=description
    )
