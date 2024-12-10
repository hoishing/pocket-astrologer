import streamlit as st
from const import PAGE_CONFIG, site_logo

# move above `import ui` to avoid "not first Streamlit command" error
st.set_page_config(**PAGE_CONFIG)

from ui import birth_data_form, transit_data_form

st.logo(site_logo())


with st.sidebar:
    birth_data_form()
    transit_data_form()
