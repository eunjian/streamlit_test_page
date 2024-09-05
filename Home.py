import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
import yaml

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Real Data Echo 홈페이지: <https://realdataecho.kr>

GitHub Repository: <https://github.com/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = Image.open('RDE_logo.png')
st.sidebar.image(logo)

st.markdown(
    """
    회사 소개 및 리얼 데이터 에코의 금융데이터 합성기술에 대한 설명
    """
)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=stauth.SafeLoader)

## yaml 파일 데이터로 객체 생성
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('main')

# authentication_status : 인증 상태 (실패=>False, 값없음=>None, 성공=>True)
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}")
    
    ## 로그인 후 기능들 작성 ##
        
    # Customize page title
    st.title(f"반갑습니다, {name}님 👋")

    st.header("📋 최근 활동 목록")
    markdown = """
    1. 
    """
    st.markdown(markdown)

    st.header("🔔 알림")