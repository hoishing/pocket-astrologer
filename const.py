"""app constants"""

import pandas as pd
import streamlit as st
from natal import Data
from pathlib import Path

SOURCE_CODE = """\
![github](https://api.iconify.design/bi/github.svg?color=%236FD886&width=20) &nbsp;
[source code](https://github.com/hoishing/pocket-astrologer)
"""

ABOUT = f"Personal Astrologer At Your Fingertips\n\n{SOURCE_CODE}"

PAGE_CONFIG = dict(
    page_title="Pocket Astrologer",
    page_icon="static/logo.png",
    layout="wide",
    menu_items={
        "About": ABOUT,
        "Get help": "https://github.com/hoishing/astrobro/issues",
    },
)

STYLE = f"<style>{Path("style.css").read_text()}</style>"


@st.cache_resource
def cities_df() -> pd.DataFrame:
    """cities df with columns: name, pop, timezone, country, lat, lon"""
    # skip the first 25 rows, which are Chinese
    return Data.get_cities().iloc[26:]


@st.cache_resource
def cities_with_code() -> list[str]:
    """list of city's `name - timezone`, sorted by population"""
    df = cities_df()
    return df["name"] + " - " + df["country"]
