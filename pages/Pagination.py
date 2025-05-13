from pathlib import Path

import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Pagination")

with open(Path(__file__).parent.parent / "docs/components/pagination.md", "r") as f:
    st.markdown(f.read())

page_value = ui.pagination(key="pagination1", total_pages=10, initial_page=1)

st.write(page_value)
st.write(ui.pagination)
