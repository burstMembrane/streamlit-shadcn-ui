from typing import Optional

from .utils import declare_component

_component_func = declare_component("aspect_ratio")


def aspect_ratio(
    src: Optional[str] = None,
    alt: Optional[str] = None,
    ratio: Optional[str] = None,
    class_name: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create an aspect ratio component with an image and a ratio.

    Args:
        src (Optional[str], optional): The source of the image. Defaults to None.
        alt (Optional[str], optional): The alternative text for the image. Defaults to None.
        ratio (Optional[str], optional): The ratio of the aspect ratio. Defaults to None.
        class_name (Optional[str], optional): The class name of the aspect ratio. Defaults to None.
        key (Optional[str], optional): The key of the aspect ratio. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.aspect_ratio(src="https://source.unsplash.com/random/256x256", ratio="16/9")
        ```
    """
    props = {
        "src": src,
        "alt": alt,
        "ratio": ratio,
        "className": class_name,
    }
    component_value = _component_func(comp="aspect_ratio", props=props, key=key)
    return component_value
