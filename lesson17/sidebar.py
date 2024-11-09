import streamlit as st

st.sidebar.header('sidebar')
st.sidebar.write('this is a sidebar')
st.sidebar.selectbox('choose an option',['opt1','opt2'])
st.sidebar.radio('go to ',['home','data','setting'])
