from const import PAGE_CONFIG, get_logo
import streamlit as st

st.set_page_config(**PAGE_CONFIG)
st.logo(get_logo())
