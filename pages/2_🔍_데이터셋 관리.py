import streamlit as st
from PIL import Image
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 한국어 폰트 설정
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


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


select_ds = st.selectbox('데이터셋을 선택하세요', ['예시1', '예시2', '예시3'])


# 데이터셋 불러오기
df = pd.read_csv('기업CB_sample.csv')
numeric_columns = df.select_dtypes(include=['number']).columns
df_style = df.style.format({col: '{}' for col in numeric_columns})

column_list = list(df.columns)

if select_ds == '예시1':
# DataFrame을 Streamlit에 출력
    st.header('데이터셋 예시 1')
    st.dataframe(df_style)

    column = st.selectbox('확인할 열을 선택하세요',column_list)
    for c in column_list:
        if column == c and c in numeric_columns:
            selected_column = df[[c]]
            st.dataframe(selected_column.style.format({}))
        elif column == c:
            st.dataframe(df[c])

    st.header('평가지표')
    col1, col2, col3 = st.columns([1,1,1]) 
    col1.metric('JSD','0.05')  #label, value, delta위치
    col2.metric('pMSE','0.02')
    col3.metric('Corr. Diff','0.01')
    
    graph_column = st.selectbox('비교 그래프', column_list)
    for c in column_list:
        if graph_column == c:
            fig, ax = plt.subplots()
            sns.histplot(df[c], kde=True)
            ax.set_xlabel(str(c))
            plt.xticks(rotation=90)
            
            st.pyplot(fig)