import streamlit as st

title = st.text_input('Machine name', '')
st.write('Selected machine:', title)

pow = st.slider('Laser power', 0, 100, 50)
st.write('Set power:', pow, 'V')

title = st.text_input('Your name', '')

if st.button("ANSWEAR!") :
    st.write(title)
else :
    pass