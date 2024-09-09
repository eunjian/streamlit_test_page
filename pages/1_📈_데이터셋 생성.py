import streamlit as st
from PIL import Image
import time
import pandas as pd

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

# st.sidebar.title("데이터셋 생성기")
tab1, tab2, tab3, tab4 = st.tabs(['데이터셋 업로드', '전처리', '학습', '산출항목 적용'])
with tab1:
    uploaded_file = st.file_uploader('데이터셋 업로드', type=['csv', 'parquet'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(f'데이터셋의 크기: {df.shape}')
        
        st.write(df)
    else:
        st.info('☝️ 파일을 업로드하세요')

with tab2:
    preprocessing = st.multiselect('전처리할 업무를 선택하세요',['데이터 중복 제거','열 타입 변경', '결측치 처리'])
    if '데이터 중복 제거' in preprocessing:
        st.info('중복된 데이터를 확인해주세요')
        st.multiselect('중복을 제거할 데이터를 선택하세요', ['데이터1', '데이터2', '데이터3'])
        b = st.button('중복 제거')
        if b:
            st.info('중복이 제거된 데이터를 확인해주세요.')
    if '열 타입 변경' in preprocessing:
        c = st.selectbox('타입을 변경할 열을 선택해주세요', ['열1', '열2', '열3'])
        t = st.selectbox('해당 열을 변경할 데이터 타입을 선택해주세요', ['타입1', '타입2'])
        if (c is not None) and (t is not None):
            b = st.button('열 타입 변경')
            if b:
                st.info('변경된 데이터를 확인해주세요.')
    if '결측치 처리' in preprocessing:
        c = st.selectbox('결측치 처리할 열을 선택해주세요', ['열1', '열2', '열3'])
        if c is not None:
            st.selectbox('결측치 처리 방식을 선택해주세요.', ['방식1', '방식2'])
            b= st.button('결측치 처리')
            if b:
                st.info('결측치 처리가 완료된 데이터를 확인해주세요.')
with tab3:
    model = st.selectbox('학습 모델을 선택해주세요', ['개인카드 고객 합성 모델(V1.1)', '개인카드 고객 합성 모델(V1.2)','개인카드 고객 합성 모델(V2.1)'])
    lr = st.slider('학습률', 0.000001, 0.1, step=0.00001, format="%.5f")
    epoch = st.slider('epoch 수', 10, 1000)
    batch_size = st.selectbox('배치 크기', [16, 32, 64, 128, 256])
    dropout = st.slider('드롭아웃 비율', 0.1, 0.5)
    if (model and lr and epoch and batch_size and dropout) is not None:
        train_start = st.button('학습 시작')
        if preprocessing and train_start:
            latest_iteration = st.empty()
            bar = st.progress(0)

            for i in range(100):
                # Update the progress bar with each iteration.
                latest_iteration.text(f'학습 중 {i+1} % 완료')
                bar.progress(i + 1)
                time.sleep(0.05)

            st.success('성공적으로 학습이 완료되었습니다.') 
with tab4:
    st.multiselect('적용할 산출 항목을 선택하세요',['항목1', '항목2', '항목3'])
    b= st.button('산출 시작')
    if b:
        st.info('산출 완료된 데이터를 확인해주세요.')


