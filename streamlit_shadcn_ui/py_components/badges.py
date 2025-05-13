from typing import List, Literal, Tuple

from .utils import declare_component

_component_func = declare_component("badges")
badge_variant_options = Literal["default", "secondary", "destructive", "outline"]


def badges(
    badge_list: List[Tuple[str, badge_variant_options]],
    class_name: str = None,
    key=None,
):
    """
    Create a badges component with a list of badges.
    Args:
        badge_list (List[Tuple[str, bade_variant]]): The list of badges, the first element is the text and the second element is the variant.
        class_name (str, optional): The tailwind CSS class name of the badges. Defaults to None.
        key (str, optional): The key of the badges. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.badges(badge_list=[("shadcn", "default"), ("in", "secondary"), ("streamlit", "destructive")])
        ```
    """
    bl = [{"text": b[0], "variant": b[1]} for b in badge_list]
    props = {"badges": bl, "className": class_name}
    clicked = _component_func(comp="badges", props=props, key=key, default=False)
    return clicked
