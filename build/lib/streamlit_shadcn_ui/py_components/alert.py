from .utils import declare_component

_component_func = declare_component("alert")


def alert(
    title: str = None, description: str = None, class_name: str = None, key: str = None
):
    """
    Create an alert component with a title and description.

    Args:
        title (str, optional): The title of the alert. Defaults to None.
        description (str, optional): The description of the alert. Defaults to None.
        class_name (str, optional): Additional tailwind CSS class names to apply. Defaults to None.
        key (str, optional): Unique key for the component. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.alert(title="This is an alert", description="This is an alert description")
        ```
    """
    props = {
        "title": title,
        "description": description,
        "className": class_name,
    }
    component_value = _component_func(comp="alert", props=props, key=key)
    return component_value
