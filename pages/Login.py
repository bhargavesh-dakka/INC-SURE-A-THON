import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from time import sleep
st.set_page_config("Earn By Complete","🧑‍💻",initial_sidebar_state="collapsed",menu_items=None)
def link_css():
    with open("style.css","r") as f:
        style_ = f.read()
    st.markdown(f"""
                <style> 
                {style_}
                </style>""",unsafe_allow_html=True)
#____________________________________

st.header("Login")
st.divider()

with st.form(key = 'Login'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    login = st.columns(5)[2].form_submit_button('Login')
    if login:
        if username == 'admin' and password == 'admin':
            st.success("Logged in as admin")
            sleep(2)
            switch_page("Index")
        else:
            st.error("Invalid username or password")
            
            

#____________________________________
link_css()