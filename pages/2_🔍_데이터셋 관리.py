import streamlit as st
from PIL import Image
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# markdown = """
# Real Data Echo 홈페이지: <https://realdataecho.kr>

# GitHub Repository: <https://github.com/>
# """

# st.sidebar.title("About")
# st.sidebar.info(markdown)
# logo = Image.open('RDE_logo.png')
# st.sidebar.image(logo)

# st.title("데이터셋 관리")

select_ds = st.sidebar.selectbox('데이터셋을 선택하세요', ['예시1', '예시2', '예시3'])


# 데이터셋 불러오기
iris = load_iris()

# Bunch 객체를 DataFrame으로 변환
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
column_list = list(df.columns)
if select_ds == '예시1':
# DataFrame을 Streamlit에 출력
    st.header('데이터셋 예시 1')
    st.dataframe(df)

    column = st.selectbox('확인할 열을 선택하세요',column_list)
    if column == 'sepal length (cm)':
        st.dataframe(df['sepal length (cm)'])

    st.selectbox('평가지표', ['JSD', 'pMSE', 'Corr.Diff'])
    graph_column = st.selectbox('비교 그래프', column_list)
    
    # if graph_column == '열1':
    #     df.plot(y=['sepal length (cm)'])
        # plt.show()