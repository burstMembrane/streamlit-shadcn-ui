from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Radio Group")
with open(Path(__file__).parent.parent / "docs/components/radio_group.md", "r") as f:
    st.markdown(f.read())

# Radio Group Component
radio_options = [
    {"label": "Option A", "value": "A", "id": "r1"},
    {"label": "Option B", "value": "B", "id": "r2"},
    {"label": "Option C", "value": "C", "id": "r3"},
    {"label": "Option D", "value": "D", "id": "r4"},
]
radio_value = ui.radio_group(options=radio_options, default_value="B", key="radio1")
st.write("Selected Radio Option:", radio_value)

st.write(ui.radio_group)
