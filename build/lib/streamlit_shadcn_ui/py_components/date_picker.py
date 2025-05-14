from streamlit_shadcn_ui.py_components.utils.declare import declare_component
from streamlit_extras.stylable_container import stylable_container
from streamlit_shadcn_ui.py_components.utils.session import init_session 
import streamlit as st
from typing import Optional, Literal
import uuid

# Declare components at module level
_trigger_component = declare_component("date_picker_trigger")
_content_component = declare_component("date_picker_content")

def date_picker_trigger(value=None, label=None, open_status=False, key=None, instance_id=None):
    """Render the date picker trigger button"""
    props = {"value": value, "open": open_status, "label": label, "instance_id": instance_id}
    return _trigger_component(comp="date_picker_trigger", props=props, key=key, default={"x": 0, "y": 0, "open": False})

def date_picker_content(x, y, mode, value=None, open=False, key=None, instance_id=None):
    """Render the date picker content"""
    # Create container for positioning the content
    container = stylable_container(
        key=f"cont_{key}", 
        css_styles=f"""
        {{
            position: absolute;
            top: {y}px;
            left: {x}px;
            display: {"block" if open else "none"};
            background-color: transparent;
            z-index: 1000;
        }}
        """
    )
    
    with container:
        props = {"value": value, "mode": mode, "open": open, "instance_id": instance_id}
        return _content_component(comp="date_picker_content", props=props, key=key, default={"value": None, "open": False})

# Function to generate or retrieve a stable instance ID
def get_stable_instance_id(key):
    """Get a stable instance ID for a component, creating one if it doesn't exist."""
    instance_key = f"instance_id_{key}"
    if instance_key not in st.session_state:
        st.session_state[instance_key] = f"dp-{uuid.uuid4().hex[:7]}"
    return st.session_state[instance_key]

def date_picker(
    label: Optional[str] = None, 
    mode: Literal["single", "range"] = "single", 
    default_value: Optional[str] = None, 
    key: Optional[str] = None
):
    """
    Create a date picker component with minimal state changes.
    
    This implementation focuses on reducing Streamlit reruns by handling most of the
    state in the browser. It only uses session state to track the current value and 
    trigger position.
    
    Args:
        label: The label for the date picker
        mode: The mode of the date picker, either "single" or "range"
        default_value: The default value for the date picker
        key: The key for the date picker
        
    Returns:
        The selected date or date range
    """
    # Generate unique keys for this instance
    if key is None:
        key = f"date_picker_{id(label)}_{id(default_value)}"
    
    # Component keys
    trigger_key = f"trigger_{key}"
    content_key = f"content_{key}"
    value_key = f"value_{key}"
    
    # Get or create a stable instance ID
    instance_id = get_stable_instance_id(key)
    
    # Initialize minimal state - just track value and open status
    if value_key not in st.session_state:
        st.session_state[value_key] = default_value
    
    # Create the root container
    with stylable_container(
        key=f"root_{key}", 
        css_styles="""                  
        {
            position: relative;
        }
        """
    ):
        # Step 1: Render trigger to get position
        current_value = st.session_state[value_key]
        trigger_result = date_picker_trigger(
            value=current_value,
            label=label,
            open_status=False,  # Start closed by default
            key=trigger_key,
            instance_id=instance_id
        )
        
        # Step 2: Check if trigger wants to open picker
        should_open = trigger_result.get("open", False)
        
        # Step 3: If open, show content at trigger position
        if should_open:
            x = trigger_result.get("x", 0)
            y = trigger_result.get("y", 0)
            
            content_result = date_picker_content(
                x=x,
                y=y,
                mode=mode,
                value=current_value,
                open=True,
                key=content_key,
                instance_id=instance_id
            )
            
            # Step 4: If content provided a value, update our state
            if content_result.get("value") is not None:
                st.session_state[value_key] = content_result["value"]
        
        # Return the current value
        return st.session_state[value_key]