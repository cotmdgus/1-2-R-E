import streamlit as st
import pandas as pd
import numpy as np

with st.sidebar:
    gubun = st.radio(
    "학교 구분",
    ('사립', '국공립'))

    if gubun == '사립':
        st.write(gubun)
    else:
        st.write(gubun)

data = pd.read_csv('기숙사수용현황분석.csv')
#st.dataframe(data)
#st.metric(label="대한민국 대학교 수", value="70 °F", delta="1.2 °F")

st.title("대학 기숙사 현황 분석")

df=data[data["학교종류"]=="대학교"]
num1=len(df["학교"].unique())
num2=len(df[df["설립구분"]!="사립"]["학교"].unique())
num3=len(df[df["설립구분"]=="사립"]["학교"].unique())

col1, col2, col3 = st.columns(3)
strcol2=str(round(num2/num1*100,2))+" %"
strcol3=str(round(num3/num1*100,2))+" %"
col1.metric("대학 수", num1, "")
col2.metric("국공립", num2, strcol2)
col3.metric("공립", num3, strcol3)

#st.write('기숙사현황')