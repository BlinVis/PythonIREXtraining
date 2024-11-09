#visualization with streamlit
import pandas as pd
import streamlit as st

df=pd.DataFrame({
    'Name':['Alma','Blin'],
    'Age':[27,17],
    'City':['feriz','poduje']
})
st.dataframe(df)


