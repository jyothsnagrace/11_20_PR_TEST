import streamlit as st
import pandas as pd

df = pd.read_csv(r'/Users/leelajosnakona/Leela/GitHub/11_20_PR_TEST/UADAggs_nat_V2_2.csv')
st.dataframe(df)