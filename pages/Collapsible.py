from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Collapsible")

with open(Path(__file__).parent.parent / "docs/components/collapsible.md", "r") as f:
    st.markdown(f.read())

ui.collapsible(
    title="@peduarte starred 3 repositories",
    firstItem="@radix-ui/primitives",
    items=["@radix-ui/colors", "@stitches/react"],
    class_name=None,
    key="collapsible1",
)

st.write(ui.collapsible)
