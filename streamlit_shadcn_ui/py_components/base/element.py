from typing import Any, Dict, List, Optional, Union

from streamlit_shadcn_ui.py_components.utils.declare import declare_component

from .context import get_context

component_func = declare_component("element_renderer")


def init_default_state(key: str = None, default_value: Any = None, **component_state):
    return {
        "st_key": key,
        "value": default_value,
        "event_id": f"{key}_init",
        **component_state,
    }


class UIElement:
    def __init__(
        self,
        name: str,
        props: Optional[Dict[str, Any]] = None,
        key: Optional[str] = None,
        default_value: Any = None,
        default_component_state: Any = {},
        children: List[Union["UIElement", str]] = None,
    ):
        self.key = key
        self.props = props if props is not None else {}
        self.name = name
        if children is not None:
            self.children = children
        else:
            self.children: List[Union["UIElement", str]] = []
        self.parent = None
        default_state = init_default_state(
            key=key, default_value=default_value, **default_component_state
        )
        self.state = default_state
        self.default_state = default_state
        ctx = get_context()
        current_element = ctx.get("current_element")
        if current_element:
            current_element.add_child(self)
            self.parent = current_element

    def render_tree(self, tree: Dict[str, Any]) -> Any:
        self.state = component_func(
            comp="element_renderer",
            props={"tree": tree},
            key=self.key,
            default=self.default_state,
        )
        return self.state

    def render_props(self) -> Dict[str, Any]:
        children = []
        for child in self.children:
            if isinstance(child, UIElement):
                children.append(child.render_props())
            else:
                children.append(child)
        return {"name": self.name, "props": self.props, "children": children}

    def render(self) -> Any:
        return self.render_tree(self.render_props())

    def __enter__(self) -> "UIElement":
        ctx = get_context()
        ctx["current_element"] = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ctx = get_context()
        if self.parent is None:
            self.render_tree(self.render_props())

        # Reset the current element to this element's parent
        ctx["current_element"] = self.parent

    def add_child(self, child: Union["UIElement", str]) -> None:
        child.parent = self
        self.children.append(child)

    def __getattr__(self, item: str) -> Any:
        if item in self.props:
            return self.props[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )

    @property
    def value(self) -> Any:
        return self.state["value"]


def element(
    name: str,
    *args,
    key: Optional[str] = None,
    default_value: Any = None,
    default_component_state: Any = {},
    **props,
) -> UIElement:
    """
    Create a generic UI element. Can be used within a context manager to render a tree of elements.
    Args:
        name (str): The name of the element.
        *args: Child elements to be nested within this element. Can be:
               - Individual UIElement instances
               - Strings (for text content)
               - Lists of UIElements or strings (all will be added as children)
        key (str, optional): The key of the element. Defaults to None.
        default_value (Any, optional): The default value of the element. Defaults to None.
        default_component_state (Any, optional): The default component state of the element. Defaults to {}.
        **props: The properties of the element.

    Examples:
    ```python
    # Basic usage with a context manager
    with ui.element("div", key="div1"):
        ui.element("h1", text="Hello, world!", key="h11")

    # Using *args to pass children directly
    ui.element("div", ui.element("span", "Child text"), ui.element("button", "Click me"), key="div2")

    # Passing a list of children
    children_elements = [ui.element("li", "Item 1"), ui.element("li", "Item 2")]
    ui.element("ul", children_elements, key="list1")

    # Use the element as a context manager to render a tree of elements.
    with ui.element("div", className=cn("flex gap-2", theme), key="buttons_group1"):
        ui.element("button", text="Get Started", className=cn("dark", theme), key="btn1")
        ui.element(
            "link_button",
            text="Github",
            url="https://github.com/ObservedObserver/streamlit-shadcn-ui",
            variant="outline",
            key="btn2",
            className=theme,
        )
    ```
    """
    children = []
    for arg in args:
        if isinstance(arg, (UIElement, str)):
            children.append(arg)
        elif isinstance(arg, list):
            children.extend(arg)

    return UIElement(
        name=name,
        props=props,
        key=key,
        default_value=default_value,
        default_component_state=default_component_state,
        children=children if children else None,
    )
