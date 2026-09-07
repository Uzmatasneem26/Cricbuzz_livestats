# pages/1_Matches.py
import os
import streamlit as st
import utils.path_setup  # ensures root path is available
from utils.db_connection import run_query

st.title(" Matches Overview")

matches = run_query("SELECT * FROM matches;")
if matches.empty:
    st.warning("No matches found.")
else:
    st.dataframe(matches, use_container_width=True)
    selected = st.selectbox("Select Match ID", matches["match_id"].tolist())
    st.markdown(f"**Selected:** {selected}")
    st.write(matches[matches["match_id"] == selected])
