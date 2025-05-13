from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Popover")

with open(Path(__file__).parent.parent / "docs/components/popover.md", "r") as f:
    st.markdown(f.read())

ui.popover(
    key="popover1", label="popover", content="Place content for the popover here."
)

st.write(ui.popover)
