import streamlit as st
from const import PAGE_CONFIG, STYLE

# move above `import ui` for conforming "first Streamlit command"
st.set_page_config(**PAGE_CONFIG)


from ui import birth_data_form, chart_ui, transit_data_form
from utils import data_obj

sess = st.session_state

st.logo("static/banner.svg")
st.markdown(STYLE, unsafe_allow_html=True)


with st.sidebar:
    name, city1 = birth_data_form()
    city2 = transit_data_form()

if display := (name and city1):
    data1, data2 = data_obj(name, city1, city2)
    chart_ui(data1, data2)


st.chat_input("Ask me anything about the birth chart", disabled=not display)
