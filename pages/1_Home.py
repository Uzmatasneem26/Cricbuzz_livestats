# pages/1_Home.py
import streamlit as st
import os

# --- Sidebar (set once globally in Streamlit_app.py, so no st.set_page_config here) ---

st.sidebar.title(" Cricbuzz LiveStats")
st.sidebar.markdown("Navigate through the app using the menu below ")

# --- Title & Intro ---
st.title(" Cricbuzz LiveStats Dashboard")
st.write("""
Welcome to your cricket analytics project!  

 Use the sidebar to navigate through the app:
- **Matches Overview** → see all matches stored in the database  
- **Players** → explore player info and roles  
- **Scores** → check scorecards by match  
- **SQL Queries** → run custom SQL against the cricket database  
- **CRUD Pages** → add, update, and delete records  
- **Visualizations** → interactive charts and insights  

---
Powered by: **SQLite + SQLAlchemy**, **Streamlit**, **Pandas + Plotly**
""")
