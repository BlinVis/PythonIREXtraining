import streamlit as st
def calculator (nr1,nr2,operation):
    if operation=='Adittion':
        result=nr1+nr2
    if operation=='Substraction':
        result=nr1-nr2
    if operation=='Multiplication':
        result=nr1*nr2
    if operation=='Divison':
        try:

             result=nr1/nr2
        except ZeroDivisionError:
            result='cannot dividwe by 0'
    return result

def main():
    st.title('simple calculator')
    nr1=st.number_input('enter your first number',step=1)
    nr2 = st.number_input('enter your second number', step=1)
    operation=st.radio('select operation',['Adittion','Substraction','Multiplication','Division'])
    result=calculator(nr1,nr2,operation)
    st.write(f'the result of your calculation is {result}')

if __name__=='__main__':
    main()

