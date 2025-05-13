### Basic Usage

```py
import streamlit as st
import streamlit_shadcn_ui as ui

page_value = ui.pagination(key="pagination1",total_pages=10,inital_page=1)

st.write(page_value)
st.write(ui.pagination)
```
