from pickle import BUILD

import streamlit as st

def main ():
    st.title('Hello from streamlit')

    #per me bo clickable
    if st.button('skibi'):
        st.write('skibidied')

    if st.checkbox('CHECK ME'):
        st.write('youre seeing thsi box becuz u chekced the checkbox')

    user_input_text= st.text_input('enter tet, sample')
    st.write('you entered:', user_input_text)
    user_input_number=st.number_input('enter your age ', min_value=0,max_value=100)
    st.write('you input', user_input_number)

    user_input_text_area= st.text_area('enter your message')
    st.write(f'message : {user_input_text_area}')
    user_input_radio=st.radio('pick one',['opcioni 1','opcioni 2','opcioni 3'])
    st.write(f'you choose:{user_input_radio}')
    if st.button('success'):
        st.success('youve clicked the button successfully')
    try:
        1 / 0
    except Exception:
        st.error('you cant divide by 0')





if __name__=='__main__':
    main()

