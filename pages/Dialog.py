from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Dialog")

with open(Path(__file__).parent.parent / "docs/components/dialog.md", "r") as f:
    st.markdown(f.read())

fields = [
    {"id": "name", "label": "Name", "defaultValue": "John Doe"},
    {"id": "username", "label": "Username", "defaultValue": "@johndoe"},
]
trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
result = ui.dialog(
    show=trigger_btn,
    title="Edit profile",
    description="Make changes to your profile here. Click save when you're done.",
    fields=fields,
    key="dialog1",
)

st.write(ui.dialog)
if result:
    confirm = result.get("confirm")
    values = result.get("values")
st.write("Dialog Value:", values)
