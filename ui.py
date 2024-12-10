import streamlit as st
from const import city_names
from datetime import datetime

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
    "options": city_names(),
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
        st.text_input("Name", key="name1")
        c1, c2 = st.columns(2)
        c1.selectbox(**CITY_ARGS, key="city1")
        c2.date_input(**DATE_ARGS, key="date1")
        c1, c2 = st.columns(2)
        c1.selectbox(**HOUR_ARGS, key="hr1")
        c2.selectbox(**MINUTE_ARGS, key="min1")


def transit_data_form():
    """input form for transit data"""
    now = datetime.now()
    sess["name2"] = "Transit"
    sess["city2"] = sess.get("city2", None)
    sess["date2"] = sess.get("date2", now.date())
    sess["hr2"] = sess.get("hr2", now.hour)
    sess["min2"] = sess.get("min2", now.minute)
    with st.expander("Transit Data", expanded=False):
        c1, c2 = st.columns(2)
        c1.selectbox(**CITY_ARGS, key="city2")
        c2.date_input(**DATE_ARGS, key="date2")
        c1, c2 = st.columns(2)
        c1.selectbox(**HOUR_ARGS, key="hr2")
        c2.selectbox(**MINUTE_ARGS, key="min2")
