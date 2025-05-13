#!/bin/bash
working_dir=$(pwd)
cd streamlit_shadcn_ui/components/packages/frontend
bun run dev &
cd $working_dir
streamlit run app.py