from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Command")

with open(Path(__file__).parent.parent / "docs/components/command.md", "r") as f:
    st.markdown(f.read())

items = [
    {"label": "Calendar"},
    {"label": "Search Emoji"},
    {"label": "Calculator"},
]
value = ui.command(items=items, key="command1", title="Suggestions")

st.write("value:", value)
st.write(ui.command)
