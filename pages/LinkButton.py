from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Link Button")

with open(Path(__file__).parent.parent / "docs/components/link_button.md", "r") as f:
    st.markdown(f.read())

ui.link_button(
    text="Go To Github",
    url="https://github.com/ObservedObserver/streamlit-shadcn-ui",
    key="link_btn",
)

st.write(ui.link_button)
