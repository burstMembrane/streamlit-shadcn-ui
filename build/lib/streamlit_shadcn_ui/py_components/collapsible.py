from typing import List, Optional

from .utils import declare_component

_component_func = declare_component("collapsible")


def collapsible(
    title: Optional[str] = None,
    firstItem: Optional[str] = None,
    items: Optional[List[str]] = None,
    class_name: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Create a collapsible component.
    Args:
        title (str, optional): The title of the collapsible component. Defaults to None.
        firstItem (str, optional): The first item of the collapsible component. Defaults to None.
        items (List[str], optional): The items of the collapsible component. Defaults to None.
        class_name (str, optional): The class name of the collapsible component. Defaults to None.
        key (str, optional): The key of the collapsible component. Defaults to None.

    Examples:
    ```python
    ui.collapsible(
    title="@peduarte starred 3 repositories",
    firstItem="@radix-ui/primitives",
    items=["@radix-ui/colors", "@stitches/react"],
    class_name=None,
        key="collapsible1",
    )
    ```
    """
    props = {
        "title": title,
        "fistItem": firstItem,
        "items": items,
        "className": class_name,
    }
    component_value = _component_func(comp="collapsible", props=props, key=key)
    return component_value
