import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")

markdown = """
Real Data Echo 홈페이지: <https://realdataecho.kr>

GitHub Repository: <https://github.com/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = Image.open('RDE_logo.png')
st.sidebar.image(logo)


st.title("도움 및 지원")


