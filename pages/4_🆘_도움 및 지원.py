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

st.header('FAQ')
faq1 = st.expander('질문1')
faq1.write('답변1')
faq2 = st.expander('질문2')
faq2.write('답변2')
faq3 = st.expander('질문3')
faq3.write('답변3')

st.header('사용 방법 설명 영상')
st.video('hazy_demo.mp4', 'rb')