# streamlit_app.py
import streamlit as st
import os

st.set_page_config(page_title=" Cricbuzz LiveStats", layout="wide")

ROOT_DIR = os.getcwd()
st.title("Welcome — Cricbuzz LiveStats")
st.write("""
This demo app is a multi-page Streamlit project showing:
- Matches, Players, Scores tables (from SQLite)
- A SQL query interface
- CRUD pages (add/update/delete)
- Visualizations with filters and CSV export

Use the sidebar to navigate to each module.
""")
