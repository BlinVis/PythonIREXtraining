import streamlit as st

tab1,tab2,tab3=st.tabs(['tab1','tab2','tab3'])

with tab1:
    st.header('tab1')
    st.write('content')
with tab2:
    st.header('tab2')
    st.write('content')
with tab2:
    st.header('tab2')
    st.write('content')

