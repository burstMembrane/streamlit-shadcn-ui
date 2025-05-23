from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Select")

with open(Path(__file__).parent.parent / "docs/components/select.md", "r") as f:
    st.markdown(f.read())

choice = ui.select(options=["Apple", "Banana", "Orange"])

st.markdown(f"Currrent value: {choice}")

st.write(ui.select)
