"""constants"""

from pathlib import Path
import streamlit as st

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


@st.cache_data
def get_logo():
    return (Path(__file__).parent / "static" / "banner.svg").read_text()
