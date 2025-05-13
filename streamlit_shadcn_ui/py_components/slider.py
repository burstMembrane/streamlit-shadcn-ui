from .utils import declare_component

_component_func = declare_component("slider")


def slider(
    default_value=None,
    min_value=0,
    max_value=100,
    step=1,
    label=None,
    key=None,
    className=None,
):
    """
    Create a slider component.

    Args:
        default_value (int, optional): The default value of the slider. Defaults to None.
        min_value (int, optional): The minimum value of the slider. Defaults to 0.
        max_value (int, optional): The maximum value of the slider. Defaults to 100.
        step (int, optional): The step value of the slider. Defaults to 1.
        label (str, optional): The label of the slider. Defaults to None.
        key (str, optional): The key of the slider. Defaults to None.
        className (str, optional): The class name of the slider. Defaults to None.
    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    ui.slider(default_value=50, min_value=0, max_value=100, step=1, label="Slider", key="slider1")
    ```
    """
    props = {
        "defaultValue": default_value,
        "min": min_value,
        "max": max_value,
        "step": step,
        "label": label,
        "className": className,
    }
    component_value = _component_func(
        comp="slider", props=props, key=key, default=default_value
    )
    return component_value
