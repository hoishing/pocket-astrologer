import streamlit as st
from const import cities_df
from datetime import datetime
from natal import Config, Data, HouseSys
from natal.config import Orb
from streamlit.runtime.state.safe_session_state import SafeSessionState

sess = st.session_state


def get_dt(id: int, sess: SafeSessionState = st.session_state) -> datetime:
    date = sess[f"date{id}"]
    hr = sess[f"hr{id}"]
    minute = sess[f"min{id}"]
    return datetime(date.year, date.month, date.day, hr, minute)


def data_obj(name: str, city1: str, city2: str = None) -> tuple[Data, Data]:
    house_sys = HouseSys.Equal
    data1 = Data(
        name=name, city=city1, dt=get_dt(1), config=Config(house_sys=house_sys)
    )

    if sess.get("city2"):
        data2 = Data(name="Transit", city=city2, dt=get_dt(2))
        data1.config.orb = Orb(
            conjunction=2, opposition=2, trine=2, square=2, sextile=1
        )
    else:
        data2 = None

    return data1, data2


def city_name(city: str | None) -> str | None:
    """split city name and country and return city name only"""
    return city.split(" - ")[0] if city else None
