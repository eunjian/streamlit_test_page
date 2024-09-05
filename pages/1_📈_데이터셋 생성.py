import streamlit as st
from PIL import Image
import time 

st.file_uploader('데이터셋 업로드', type=['csv', 'parquet'])

st.sidebar.title("데이터셋 생성기")
preprocessing = st.sidebar.multiselect('전처리할 업무를 선택하세요',['데이터 중복 제거','열 타입 변경', '결측치 처리'])
st.sidebar.header('학습 파라미터 설정')
st.sidebar.multiselect('numeric 열을 설정하세요', ['열1', '열2', '열3'])
st.sidebar.multiselect('categorical 열을 설정하세요', ['열1', '열2', '열3'])
st.sidebar.slider('max-depth')
postprocessing = st.sidebar.multiselect('후처리할 업무를 선택하세요',['합성데이터 복제', '결측치 항목 복원', 'continuous 열 복원'])

if preprocessing and postprocessing:
    # 방법 1 progress bar 
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'학습 중 {i+1} % 완료')
        bar.progress(i + 1)
        time.sleep(0.05)
        # 0.05 초 마다 1씩증가  