import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv('기숙사수용현황분석')
st.dataframe(data)
st.write('기숙사현황')