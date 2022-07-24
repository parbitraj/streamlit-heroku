import streamlit as st

st.title('Finding the Largest Number')
st.subheader('This app finds the largest number among the user entered numbers.')

st.subheader('User Input')
a = st.number_input('Enter 1st number',step=1)
b = st.number_input('Enter 2nd number',step=1)
c = st.number_input('Enter 3rd number',step=1)
result = max(a,b,c)


st.header('Result')
st.write("The largest number is ", result)
