from typing import Literal, Optional

from .utils import declare_component

_component_func = declare_component("link_button")


def link_button(
    text: Optional[str] = None,
    url: Optional[str] = None,
    variant: Optional[
        Literal["default", "destructive", "outline", "secondary", "ghost", "link"]
    ] = "default",
    class_name: Optional[str] = None,
    key=None,
):
    """
    Create a link button component.

    Args:
        text (str, optional): The text of the link button. Defaults to None.
        url (str, optional): The URL of the link button. Defaults to None.
        variant (str, optional): The variant of the link button. Defaults to "default".
        class_name (str, optional): The class name of the link button. Defaults to None.
        key (str, optional): The key of the link button. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.link_button(text="Link Button", url="https://www.google.com", variant="default", class_name="bg-red-500", key="link_button_1")
    ```
    """
    props = {"text": text, "variant": variant, "url": url, "className": class_name}
