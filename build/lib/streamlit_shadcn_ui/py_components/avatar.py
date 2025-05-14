from .utils import declare_component

_component_func = declare_component("avatar")


def avatar(src: str, fallback: str = None, key=None):
    """
    Create an avatar component with a source and a fallback.

    Args:
        src (str): The source url of the avatar.
        fallback (str, optional): The fallback of the avatar. Defaults to None.
        key (str, optional): The key of the avatar. Defaults to None.

    Examples:
        ```python
        import streamlit_shadcn_ui as ui
        ui.avatar(src="https://ui-avatars.com/api/?name=John+Doe", fallback="AI")
        ```
        ![Avatar](https://ui-avatars.com/api/?name=John+Doe)

    """
    props = {"src": src, "fallback": fallback}
    component_value = _component_func(comp="avatar", props=props, key=key, default=None)
    return component_value
