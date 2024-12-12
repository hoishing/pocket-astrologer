import streamlit as st
from const import cities_with_code
from datetime import datetime
from natal import Chart, Data
from utils import city_name

sess = st.session_state

DATE_ARGS = {
    "label": "Date",
    "max_value": datetime(2300, 1, 1).date(),
    "min_value": datetime(1800, 1, 1).date(),
    "format": "YYYY-MM-DD",
}

HOUR_ARGS = {
    "label": "Hour",
    "options": range(24),
}

MINUTE_ARGS = {
    "label": "Minute",
    "options": range(60),
    "help": "daylight saving time",
}

CITY_ARGS = {
    "label": "City",
    "options": cities_with_code(),
    "placeholder": "type to search",
    "help": "use nearest city if not found",
}


def birth_data_form():
    """input form for birth data"""
    sess["name1"] = sess.get("name1", "")
    sess["city1"] = sess.get("city1", None)
    sess["date1"] = sess.get("date1", datetime(2000, 1, 1).date())
    sess["hr1"] = sess.get("hr1", 13)
    sess["min1"] = sess.get("min1", 0)
    with st.expander("Birth Data", expanded=True):
        c1, c2 = st.columns(2)
        name = c1.text_input("Name", key="name1")
        city1 = c2.selectbox(key="city1", **CITY_ARGS)
        c1, c2, c3 = st.columns(3)
        c1.date_input(**DATE_ARGS, key="date1")
        c2.selectbox(**HOUR_ARGS, key="hr1")
        c3.selectbox(**MINUTE_ARGS, key="min1")
        city = city_name(city1)
    return name, city


def transit_data_form():
    """input form for transit data"""

    def clear_transit():
        sess.city2 = None

    now = datetime.now()
    sess["city2"] = sess.get("city2")
    sess["date2"] = sess.get("date2", now.date())
    sess["hr2"] = sess.get("hr2", now.hour)
    sess["min2"] = sess.get("min2", now.minute)
    with st.expander("Transit Data", expanded=True):
        c1, c2 = st.columns([2, 1], vertical_alignment="bottom")
        city2 = c1.selectbox(key="city2", **CITY_ARGS)
        c2.button(
            "clear",
            key="clear_transit",
            on_click=clear_transit,
            use_container_width=True,
        )
        c1, c2, c3 = st.columns(3)
        c1.date_input(**DATE_ARGS, key="date2")
        c2.selectbox(**HOUR_ARGS, key="hr2")
        c3.selectbox(**MINUTE_ARGS, key="min2")
    return city_name(city2)


def chart_ui(data1: Data, data2: Data = None):
    chart = Chart(data1=data1, data2=data2, width=600)
    with st.container(key="chart_svg"):
        st.markdown(chart.svg, unsafe_allow_html=True)


