import streamlit as st
#with st.container():
    #st.header('this is a container')
    #st.write('this is inside container')

#st.write('thos is outside container')


st.sidebar.header('sidebar')
st.sidebar.write('this is a sidebar')
st.sidebar.selectbox('choose an option',['opt1','opt2'])
st.sidebar.radio('go to ',['home','data','setting'])


with st.form('myform',clear_on_submit=True):
    name=st.text_input('name')
    age=st.slider('age', min_value=0,max_value=100)
    email=st.text_input('email')
    bio=st.text_area('short bio')
    terms=st.checkbox('i agree to the terms')
    submit_button=st.form_submit_button(label='submit')
if submit_button:
    st.write(name)
    st.write(age)
    if terms:
        st.write('you have agreed yto our terms')
    else:
        st.write('you did not agree to our terms')
