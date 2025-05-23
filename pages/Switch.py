from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Switch")

with open(Path(__file__).parent.parent / "docs/components/switch.md", "r") as f:
    st.markdown(f.read())

# Switch Component
switch_value = ui.switch(default_checked=False, label="Toggle Switch", key="switch1")
st.write("Switch is On:", switch_value)

st.write(ui.switch)
