from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Input Component")

with open(Path(__file__).parent.parent / "docs/components/input.md", "r") as f:
    st.markdown(f.read())

# Input Component
input_value = ui.input(
    default_value="Hello, Streamlit!",
    type="text",
    placeholder="Enter text here",
    key="input1",
)
st.write("Input Value:", input_value)

st.write(ui.input)
